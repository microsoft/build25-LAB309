import os
import json

from flask import Flask, render_template, request, jsonify
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential, AzureDeveloperCliCredential, get_bearer_token_provider
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    SearchFieldDataType,
    SearchableField,
    SearchIndex,
    SimpleField,
)
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from openai import AzureOpenAI
from openai.lib.azure import AzureADTokenProvider

app = Flask(__name__, 
    static_folder="static",
    template_folder="api/templates")

scopes = "https://cognitiveservices.azure.com/.default"

credential = DefaultAzureCredential()
# tenant_id = os.environ.get('AZURE_TENANT_ID')
# credential = AzureDeveloperCliCredential(tenant_id=tenant_id)
token_provider: AzureADTokenProvider = get_bearer_token_provider(credential, scopes)

search_endpoint = os.environ.get('AZURE_AI_SEARCH_ENDPOINT')
openai_endpoint = os.environ.get('AZURE_OPENAI_ENDPOINT')
project_connection_string=os.environ.get('AZURE_AI_PROJECT_CONNECTION_STRING')

openai_model_name = "gpt-4o"
foundry_model_name = "gpt-4o-mini"
index_name = "hotels-quickstart"

# Load documents dynamically from the JSON file
def load_documents():
    with open('documents.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Replace the hardcoded documents with a call to load_documents
documents = load_documents()

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

def get_openai_client():
    return AzureOpenAI(
        api_version="2024-06-01",
        azure_endpoint=openai_endpoint,
        azure_ad_token_provider=token_provider,
        )

def get_ai_chat_completion_client():
    project = AIProjectClient.from_connection_string(conn_str=project_connection_string, credential=credential)
    return project.inference.get_chat_completions_client()

def get_index_client(hub: bool):
    if not hub:
        return SearchIndexClient(endpoint=search_endpoint, credential=credential)
    
    project = AIProjectClient.from_connection_string(conn_str=project_connection_string, credential=credential)
    search_connection = project.connections.get_default(
        connection_type=ConnectionType.AZURE_AI_SEARCH,
        include_credentials=True)

    index_client = SearchIndexClient(
        endpoint=search_connection.endpoint_url,
        credential=AzureKeyCredential(key=search_connection.key)
    )

    return index_client

def get_search_client(hub: bool):
    if not hub:
        return SearchClient(endpoint=search_endpoint, index_name=index_name, credential=credential)

    project = AIProjectClient.from_connection_string(conn_str=project_connection_string, credential=credential)
    search_connection = project.connections.get_default(
        connection_type=ConnectionType.AZURE_AI_SEARCH,
        include_credentials=True)

    search_client = SearchClient(
        index_name=index_name,
        endpoint=search_connection.endpoint_url,
        credential=AzureKeyCredential(key=search_connection.key)
    )
    return search_client

@app.route('/api/create_index')
def create_index():
    """API endpoint to create search index"""
    use_hub = request.args.get('hub', 'False').lower() == 'true'

    try:
        index_client = get_index_client(use_hub)

        fields = [
                SimpleField(name="HotelId", type=SearchFieldDataType.String, key=True),
                SearchableField(name="HotelName", type=SearchFieldDataType.String, sortable=True),
                SearchableField(name="Description", type=SearchFieldDataType.String, analyzer_name="en.lucene"),
                SearchableField(name="Description_fr", type=SearchFieldDataType.String, analyzer_name="fr.lucene"),
                SearchableField(name="Category", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),

                SearchableField(name="Tags", collection=True, type=SearchFieldDataType.String, facetable=True, filterable=True),

                SimpleField(name="ParkingIncluded", type=SearchFieldDataType.Boolean, facetable=True, filterable=True, sortable=True),
                SimpleField(name="LastRenovationDate", type=SearchFieldDataType.DateTimeOffset, facetable=True, filterable=True, sortable=True),
                SimpleField(name="Rating", type=SearchFieldDataType.Double, facetable=True, filterable=True, sortable=True),

                ComplexField(name="Address", fields=[
                    SearchableField(name="StreetAddress", type=SearchFieldDataType.String),
                    SearchableField(name="City", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
                    SearchableField(name="StateProvince", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
                    SearchableField(name="PostalCode", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
                    SearchableField(name="Country", type=SearchFieldDataType.String, facetable=True, filterable=True, sortable=True),
                ])
            ]

        scoring_profiles = []
        suggester = [{'name': 'sg', 'source_fields': ['Tags', 'Address/City', 'Address/Country']}]

        # Create the search index=
        index = SearchIndex(name=index_name, fields=fields, suggesters=suggester, scoring_profiles=scoring_profiles)
        result = index_client.create_or_update_index(index)
        print(f' {result.name} created')

        return jsonify({"index": result.name})
    except Exception as ex:
        return jsonify({
            "error": "Create index failed", 
            "message": str(ex)
        }), 500

@app.route('/api/upload_documents')
def upload_documents():
    """API endpoint to upload documents to the index"""
    use_hub = request.args.get('hub', 'False').lower() == 'true'
    try:
        search_client = get_search_client(use_hub)
        result = search_client.upload_documents(documents=documents)
        print("Upload of new document succeeded: {}".format(result[0].succeeded))
        return jsonify({"result": result[0].succeeded})
    except Exception as ex:
        return jsonify({"error": "Upload failed", "message": str(ex)}), 500

@app.route('/api/search')
def search():
    """API endpoint to perform search with a query"""
    use_hub = request.args.get('hub', 'False').lower() == 'true'
    
    try:
        search_client = get_search_client(use_hub)
        # Get query parameter from request, default to "*" if not provided
        search_query = request.args.get('query', '*')
        # Run a search with the provided query
        results = search_client.search(
            query_type='simple',
            search_text=search_query,
            select='HotelName,Description,Tags',
            include_total_count=True
        )

        response_data = {
            'total_count': results.get_count(),
            'results': []
        }
        
        for result in results:
            response_data['results'].append({
                'score': result["@search.score"],
                'hotel_name': result["HotelName"],
                'description': result["Description"],
                'tags': result.get("Tags", [])
            })
        
        return jsonify(response_data)
    except Exception as ex:
        return jsonify({
            "error": "Search failed", 
            "message": str(ex)
        }), 500

@app.route('/api/empty_query')
def empty_query():
    use_hub = request.args.get('hub', 'False').lower() == 'true'

    try:
        search_client = get_search_client(use_hub)
        # Run an empty query (returns selected fields, all documents)
        results = search_client.search(query_type='simple',
            search_text="*",
            select='HotelName,Description',
            include_total_count=True)

        response_data = {
            'total_count': results.get_count(),
            'results': []
        }
        
        for result in results:
            response_data['results'].append({
                'score': result["@search.score"],
                'hotel_name': result["HotelName"],
                'description': result["Description"]
            })
        
        return jsonify(response_data)
    except Exception as ex:
        return jsonify({
            "error": "Empty query search failed", 
            "message": str(ex),
        }), 500

@app.route('/api/recommend')
def recommend():
    """API endpoint to get AI recommendations based on search results"""
    use_hub = request.args.get('hub', 'False').lower() == 'true'
    use_search = request.args.get('search', 'False').lower() == 'true'

    # Get query parameter from request
    query = request.args.get('query', '')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    try:
        sources_formatted = ""
        search_results = []
        if use_search:
            search_client = get_search_client(use_hub)
            # Search for relevant hotels
            search_results = search_client.search(
                search_text=query,
                top=5,
                select="Description,HotelName,Tags"
            )
            search_results = list(search_results)
            
            # Format search results as sources
            sources_formatted = "\n".join([
                f'{document["HotelName"]}:{document["Description"]}:{document.get("Tags", [])}' 
                for document in search_results
            ])

        # Grounding prompt
        grounding_prompt = """
        You are a friendly assistant that recommends hotels based on activities and amenities.
        Answer the query using only the sources provided below in a friendly and concise bulleted manner.
        Answer ONLY with the facts listed in the list of sources below.
        If there isn't enough information below, say you don't know.
        Do not generate answers that don't use the sources below.
        Query: {query}
        Sources:
        {sources}
        """

        messages = [
            {
            "role": "user",
            "content": grounding_prompt.format(query=query, sources=sources_formatted)
            }
        ]

        if use_hub:
            chat_client = get_ai_chat_completion_client()
            response = chat_client.complete(
                model=foundry_model_name,
                messages=messages,
                max_tokens=100,
            )
        else:
            openai_client = get_openai_client()
            response = openai_client.chat.completions.create(
                model=openai_model_name,
                messages=messages,
                max_tokens=100,
            )

        recommendation = response.choices[0].message.content

        return jsonify({
            'recommendation': recommendation,
            'sources_count': len(search_results),
        })

    except Exception as ex:
        return jsonify({
            "error": "Recommendation failed", 
            "message": str(ex),
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)