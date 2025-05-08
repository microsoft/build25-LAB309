# Exercise 2: Add AI Search

Add AI search and add data for the search, then redeploy. 

## Module overview

In [Exercise-1](/Lab-Instructions/Exercise-1.md), you deploy a Python app to ACA. 

In this module, you are going to run `azd add` to add Azure AI Search, create an index and upload built-in sample data. 

Time to complete: 15 minutes.

## Working with azd Compose

[azd Compose](https://aka.ms/azd-compose) is an alpha feature that allows you to progressively add Azure resources. You can run a new command called `azd add` and build up your app in a step-by-step manner as you learn.

## Instructions

1. Make sure you are still in the **/src** folder
1. Run `azd add`
    * Select "AI".
    * Select "Azure AI Search".
    * Make sure your service uses the newly added resource by typing <space> to select.
    ![Connect service to searach](/Lab-Instructions/Images/2.ConnectServicetoSearch.png)
    * Type "Y" or simply hit <enter> to accept changes to azure.yaml    
1. If the **infra** folder exists, run azd provision to provision the newly added resource. **Note**: you see this because have run `azd infra synth`, delete the **infra** folder and then run `azd provision` or run `azd infra synth` again to re-sythesize the infrastructure before running `azd provision`.
1. Otherwise, select either Yes to provision the changes.

## Running the app and redeploy to Azure

1. Let's run the app locally to make sure everything is fine. Run `azd show search` to get the environment variable to set.
1. Run 
    ```powershell
    $env:AZURE_AI_SEARCH_ENDPOINT="https://XXX.search.windows.net"
    ```
    Replace XXX with your search service endpoint.
1. Run `python app.py`
1. Click **Create Index** button to create an index
1. Click **Upload Documents** to upload the sample hotel data.

    ![Index Management](/Lab-Instructions/Images/2.index-management.png)
1. You can now click the **Search** button. If you leave the search query empty, you should get 4 results/hotels. 

What happened and why did this work? 

* If you refer to line 32 in [app.py](/src/app.py), the Python app is using the environment variable AZURE_AI_SEARCH_ENDPOINT to connect to the Azure AI Search you just added. So as long as you set the environment variable  in your local machine, you will be able to reach the Search service.
    ```
    search_endpoint = os.environ.get('AZURE_AI_SEARCH_ENDPOINT')
    ```

### Deploy to Azure
Since you didn't change any of the app code, you do not need to run `azd deploy`. If you visit your service endpoint, you will see that clicking search returns all 4 hotels just like the app did when running locally.

## The Code

At this point, your azure.yaml should look like this:

``` yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/Azure/azure-dev/main/schemas/alpha/azure.yaml.json
name: src
metadata:
  template: azd-init@xxxx
services:
  src:
    project: .
    host: containerapp
    language: python
    docker:
      path: Dockerfile
resources:
  src:
    type: host.containerapp
    port: 5000
    uses:
      - search
  search:
    type: ai.search
```

## Lab challenges

1. Can you add another hotel to the built-in sample data; deploy the app to Azure and upload document using the app running in Azure?  

**Hints**: 
* Perhaps ask your copilot where the **Upload Documents** button is getting the sample data?

## Next
[Exercise 3](/Lab-Instructions/Exercise-3.md)