# Exercise 4: Monitor your application and manage your storage account

> [!Note]
> Goal: Check logs in your Log Analytics Workspace and perform data plane operations on your storage account

In this module, we'll configure monitoring and diagnostic tools and work with the GitHub Copilot for Azure for cost optimization.

## Module overview

In [Exercise-3](/Lab-Instructions/Exercise-3.md), you used `azd add` to add Azure Open AI so that you can learn how your chat result is affected when you add grouding data to chat.

In this module, you are going to use GitHub Copilot for Azure to understand the logging setting on your application, review monitoring data, and perform data plane operations on your storage account. 

Time to complete: 15 minutes

## Checking logging settings 

Let's first check if logging is properly set up for the project. Use the following prompt in GHCP for Azure to check your logging configurations. 

`Prompt: Do I have logging enabled for my project?`

This prompt will yield results after thoroughly checking the files in your workspace. 

### Bonus challenge - Use GitHub Copilot for Azure to find answers to these questions. The answers can be found in the end of this module. 
1. What's the name of the module that sets up Azure Monitor including Log Analytics and Application Insights?
2. Name at least 2 access points for your application logs.
3. How can you enhance the logging setup? 

## Explore monitoring data
Now, let's use the following prompt to identify the name of your Log Analytics Workspace.

`Prompt: Identify the Log Analytics Workspace being used in my current project" 

Once you have the name of your Log Analytics Workspace, try the following prompt to list all tables with data within the Log Analytics Workspace. 

`Prompt: List all the tables with data in my Log Analytics Workspace <your_workspace_name> in my subscription`

Now, explore the schema of each table using the following prompt. 

`Prompt: Show me the schema for <your_table_name>`

## Perform data plane operations on your storage account 

First, identify your storage account using the following prompt in agent mode. 

`Prompt: List all my storage accounts in my subscription`

Then, in the same chat, use the following prompt to get the list of blob containers. 

`Prompt: List all blob containers in my storage account <your_storage_name> in my subscription` 

Add a new blob container to your storage account for media content. 

`Prompt: Add a new blob container named "media" in my storage account`

Verify that the "media" blob storage now exists in your storage account by using the following prompt. 

`Prompt: Verify if there is a blob storage named "media" in my storage account`

## Bonus challenge Answers
1. monitoring
2. Azure Portal, Container Console, & Azure CLI
3. Python Logging Framework: You don't currently use Python's built-in logging module which would provide more structured logs and log levels/ OpenTelemetry Integration: For more sophisticated tracing and metrics/ Explicit Exception Logging: While you catch exceptions, more detailed logging of errors would be beneficial

## Congratulations!
You started with a basic Python application that had no functionality, you deployed it to Azure and got it running, then added AI Search and AI Chat, and did additional configurations so your applications is running smoothly on Azure.

## Next
Now that you've explored the monitoring data of your application and managed your storage account, head over to [Exercise 5](/Lab-Instructions/Exercise-5.md) to learn about cost optimization.
