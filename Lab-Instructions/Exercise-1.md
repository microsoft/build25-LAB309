# Exercise 1: Get started with AI app development

> [!Note]
> Goal: Deploy your application to Azure.

## Module overview

In this lab module, you learn about working with the Azure Developer CLI (azd), Infrastruture as Code (IaC), and preparing to add AI features to your sample hotel search app.

You ran the Python app locally in [Getting Started](getting-started.md). In this module, you are going to run `azd init` and `azd up` to deploy the app to Azure Container Apps (ACA).

Once you complete this exercise, you will have your application deployed to Azure and ready to add AI features.

> [!NOTE]
> Time to complete: 10 minutes

## Working with the Azure Developer CLI (azd)

[Azure Developer CLI (azd)](https://aka.ms/azd) is an open-source command line tool that provides high-level, developer-friendly commands that can help you build, deploy, and manage your application on Azure. 

If you would like to learn more about azd or the app in /src, use the link above or use `ctrl+alt+i` to open Copilot Chat, select `Ask` mode and ask `@azure` your questions.

## Instructions
1. In a VS Code terminal, make sure you are in the **/src** directory. 
1. Run `azd config set alpha.compose on` to enable the feature since azd Compose is an alpha feature.
1. Run `azd init` to initialize the project.
    * Select "Use code in the current directory".
    * Select "Confirm and continue initializing my app".

    What happened?
    * An azure.yaml file is added in the **/src** directory.
    * A **next-steps.md** file is also generated.

1. Run azd up to deploy the app to Azure.
    * Provide any name when you are asked for an environment name.
    * Select the subscription you want to use.
    * Provide a location, you can use for examples, **East US 2**.
1. Once provision and deployment is complete, click the endpoint to check out the app running on Azure.

    ![azd up](/Lab-Instructions/Images/1.azd-up-done.png)

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
```

## Lab challenges

1. Can you tell us if zone redundancy is enabled for the Azure Container app?
1. In azure.yaml, can you explain how `azd` know to open port 5000 on the Azure Container App?
1. Try using Copilot Chat in `Agent` mode:
    - Tell Copilot "I want to deploy the app in \src to Azure as a Container App using azd. Put the azure.yaml and the \infra folder in the \src directory. Always use the latest bicep schema." 
    - Note: After each turn, you may need to click the `Keep` button so the files are written to disk.
    - If Copilot wants you to manually run the azd commands to deploy the app, just tell it "why don't you deploy this for me".
    - If you get an error in the terminal, paste it back into Copilot Chat to get some help.

**Hints**: 
* azd Compose uses Bicep. All IaC files are generated in memory. To get the Bicep code:
    * Run `azd config set alpha.infrasynth on` to enable the feature (infrasynth is also an alpha feature.)
    * Run `azd infra synth` to get the /infra folder and all Bicep files generated under /infra.

> [!Note]
> If you run `azd infra synth`, make sure you delete the /infra folder before you proceed with subsequent exercises. Otherwise, every time you add a new resource using `azd add`, you need to run `azd infra synth` to re-synthesize Bicep code written on disk. 

* azd Compose uses [Azure Verified Module (AVM)](https://aka.ms/AVM). With Bicep VS Code extension, you can mouse-over a module.

    ![Mouse over module name](/Lab-Instructions/Images/1.mouse-over-avm.png)
    
    or hit F12 to learn more about the AVM module azd is referencing.
* Or, you can just ask GitHub Copilot to find the answer for you!

## Next
Now that you've got your application deployed to Azure, head over to [Exercise 2](/Lab-Instructions/Exercise-2.md) to coninue building your application and adding AI functionality.