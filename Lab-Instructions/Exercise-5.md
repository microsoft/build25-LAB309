# Exercise 5: Cost management and optimization 

> [!Note]
> Goal: Check the usage cost of your project and learn about cost optimization tips 

In this module, we'll configure monitoring and diagnostic tools and work with the GitHub Copilot for Azure for cost optimization.

## Module overview

In [Exercise-4](/Lab-Instructions/Exercise-4.md), you used GitHub Copilot for Azure to understand the logging setting on your application, review monitoring data, and perform data plane operations on your storage account.

In this module, you are going to use GitHub Copilot for Azure to check the usage cost of your project and learn about cost optimization tips.  

Time to complete: 10 minutes

## Checking the usage cost  

Let's first check the cost breakdown of your subscription by service asking the following prompt in **Ask mode**. Cost Management is currently only supported in Ask mode.

`Prompt: @azure Give me a cost breakdown for my subscription`

This prompt will scope your request to the selected subscription and query the cost management api for actual charges on each of the services hosted on your subscription.

## Check the pricing tier and sku of your resources

Now, switch the mode to **Agent mode** to check the pricing tiers and skus of your resources. For this scenario, using agent mode is recommended as GitHub Copilot makes a series of tool calls to understand the resources being used in your project and your application's functionality to provide cost optimization solutions.

`Prompt: help me review the pricing tiers and SKUs of the resources in my subscription.`

## Getting tips on cost optimization 

Stay on **Agent mode** and get tailored recommendations on optimizing the cost of your project. For this scenario, using agent mode is recommended as GitHub Copilot makes a series of tool calls to understand the resources being used in your project and your application's functionality to provide cost optimization solutions. 

`Prompt: How do I optimize the cost of my current project?`

## Congratulations!
Congratulations. You have now successfully completed the lab. 
