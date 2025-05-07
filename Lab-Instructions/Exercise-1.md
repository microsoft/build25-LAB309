# Exercise 1: Get started with AI app development

In this lab module, you learn about working with the Azure Developer CLI (azd), Infrastruture as Code (IaC), and preparing to add AI features to your sample hotel search app.

## Working with the Azure Developer CLI (azd)

[Azure Developer CLI (azd)](https://aka.ms/azd) is an open-source command line tool that provides higher-level, developer-friendly commands that can help you build, deploy, and manage your application on Azure. 

## Module overview

You ran the Python app locally in [Getting Started](getting-started.md). In this module, you are going to run `azd init` and `azd up` to deploy the app to Azure Container App (ACA.)

Time to complete: 10 minutes.

## Instructions
1. In a VS Code terminal, make sure you are in the **/src** directory. 
1. Run `azd config set alpha.compose on` to enable the feature since azd Compose is an alpha feature.
1. Run `azd init` to initialize the project.
    * Select "Use code in the current directory"
    * Select "Confirm and continue initializing my app"

    What happened?
    * an azure.yaml file is added in the **/src** directory
    * a **next-steps.md** is also generated.

1. Run azd up to deploy the app to Azure.
    * Provide any name when you are asked for an environment name.
    * Select the subscription you want to use
    * Provide a location, you can use for examples, **East US 2**.
1. Once provision and deployment is complete, click the endpoint to check out the app running on Azure.

    ![azd up](/Lab-Instructions/Images/1.azd-up-done.png)

    
## Lab challenges

1. Can you tell us if zone redundancy is enabled for the Azure Container app?
1. In azure.yaml, can you explain how `azd` know to open port 5000 on the Azure Container App?

**Hints**: 
* azd Compose uses Bicep. All IaC files are generated in memory. To get the Bicep code:
    * run `azd config set alpha.infrasynth on` to enable the feature (infrasynth is also an alpha feature.)
    * run `azd infra synth` to get the /infra folder and all Bicep files generated under /infra.
* azd Compose uses [Azure Verified Module (AVM)](https://aka.ms/AVM). With Bicep VS Code extension, you can mouse-over e.g.,  hit F12 to learn more about the AVM module azd is referencing.
![Mouse over module name](/Lab-Instructions/Images/1.mouse-over-avm.png)
* Or, you can just ask GitHub Copilot to find the answer for you!

## Next
[Exercise 2](/Lab-Instructions/Exercise-2.md)
 
