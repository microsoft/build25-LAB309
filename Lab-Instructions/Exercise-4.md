# Exercise 4: Check logs for monitoring and manage your storage account

> [!Note]
> Goal: Configure and optimize your application running on Auzre.

In this module, we'll configure monitoring and diagnostic tools and work with the GitHub Copilot for Azure for cost optimization.

## Application monitoring overview
- performance, error logging, usage, etc
- cover Azure Monitor and Application Insights

Ask @azure agent "Help me set up monitoring on my application."

## Checking logging settings 

Let's first check if logging is properly set up for the project. Use the following prompt in GHCP for Azure to check your logging configurations. 

`Prompt: Do I have logging enabled for my project?`

This prompt will yield results after thoroughly checking the files in your workspace. 

### Quiz - Use GitHub Copilot for Azure to find answers to these questions 
1. What's the name of the module that sets up Azure Monitor including Log Analytics and Application Insights?
2. Name at least 2 access points for your application logs.
3. How can you enhance the logging setup? 

## Explore monitoring data
Now, let's use the following prompt to identify the name of your Log Analytics Workspace.

`Prompt: Identify the Log Analytics Workspace being used in my current project" 

Once you have the name of your Log Analytics Workspace, try the following prompt to list all tables with data within the Log Analytics Workspace. 

`Prompt: List all the tables with data in my Log Analytics Workspace <your_workspace_name> in my subscription`

## Perform data plane operations on your storage account 

First, identify your storage account using the following prompt in agent mode. 

`Prompt: List all my storage accounts in my subscription`

Then, in the same chat, use the following prompt to get the list of blob containers. 

`Prompt: List all blob containers in my storage account <your_storage_name> in my subscription` 

Add a new blob container to your storage account for media content. 

`Prompt: Add a new blob container named "media" in my storage account`

Verify that the "media" blob storage now exists in your storage account by using the following prompt. 

`Prompt: Verify if there is a blob storage named "media" in my storage account`

## Review
[TODO: Summarize key concepts and steps here]

## Practice
[TODO: add practice prompts]

## Bonus challenge
[TODO: add two short bonus challenges]

## Congratulations!
You started with a basic Python application that had no functionality, you deployed it to Azure and got it running, then added AI Search and AI Chat, and did additional configurations so your applications is running smoothly on Azure.

## Answers
1. monitoring
2. Azure Portal, Container Console, & Azure CLI
3. Python Logging Framework: You don't currently use Python's built-in logging module which would provide more structured logs and log levels/ OpenTelemetry Integration: For more sophisticated tracing and metrics/ Explicit Exception Logging: While you catch exceptions, more detailed logging of errors would be beneficial

## Next
We've added bonus challenges throughout the lab modules so that you can go back through and try your new knowledge if you didn't get a chance to do it in the live lab.

To keep building and experimenting with Azure services and Azure AI Foundry models, check out the collection of [AI templates](https://aka.ms/ai-gallery)

> [!Note]
> When you are experimenting with templates, remember to clean up with `azd down` or `azd down --purge` once you're done so that you don't incur unwanted charges.
