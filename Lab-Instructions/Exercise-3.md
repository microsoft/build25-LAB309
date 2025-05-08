# Exercise 3: Add AI Chat to your application

Add Azure Open AI(AOAI) and connect chat interface in your app to AOAI.

## Module overview

In [Exercise-2](/Lab-Instructions/Exercise-2.md), you added Azure Search AI and made sure your app can connect to the Search service end point. You have also created an index and uploaded some sample data to the Search service.

In this module, you are going to run `azd add` to add Azure Open AI so that you can learn how your chat result is affected when you add grouding data to chat.

Time to complete: 25 minutes.

## Working with GitHub Copilot for Azure

Find the best model for this AI scenario using GitHub Copilot for Azure.

### Step 1: Open GitHub Copilot for Azure in VS Code 
1. Locate the GitHub Copilot icon in the top command bar or use the shortcut **Ctrl + Alt + I** to open the chat pane.
2. When prompted to sign in, use the GitHub Enterprise Username and Password found in the **Instructions** tab within the Skillable VM.

### Step 2: Find the best model for this lab's scenario with GitHub Copilot for Azure
1. Make sure you have the mode set to **Ask** and start your prompts with **@azure** to invoke GitHub Copilot for Azure.
2. If necessary, ask follow-up questions and clarifying questions to identify the model to use.

### Step 3: Add AI chat model
We will be using the OpenAI Chat GPT-4o model. The Azure OpenAI Chat GPT-4o model is a powerful language model available through the Azure OpenAI Service. This model is designed for advanced conversational AI tasks.

The Chat GPT-4o model is integrated with Azure's capabilities, providing scalability, security, and enterprise features. There are different variants like GPT-4o Mini, which is a lighter version, and GPT-4 Turbo with Vision, which includes vision capabilities, that you can use for your use case.

### TODO verify that this the model we want to use
```
    type: ai.search
  gpt-4o:
    type: ai.openai.model
    model:
      name: gpt-4o
      version: "2024-08-06"
  ai-project:
    type: ai.project
    models:
      - name: gpt-4o-mini
        version: "2024-07-18"
        format: OpenAI
        sku:
          name: GlobalStandard
          usageName: OpenAI.GlobalStandard.gpt-4o-mini
          capacity: 10
```
## Instructions

1. Make sure you are still in the **/src** folder
1. Run `azd add`
    * Select "AI".
    * Select "Azure OpenAI model".
    * Select "Chat (GPT)"
    * Select "gpt-40     2024-11-20"
    * Provide a name for this model; you can hit enter to select the default value.
    * Make sure your service uses the newly added resource by typing <space> to select.
    ![Connect service to gpt-4o](/Lab-Instructions/Images/3.ConnectServicetoAOAI.png)
    * Type "Y" or simply hit <enter> to accept changes to azure.yaml    
1. If the **infra** folder exists, run azd provision to provision the newly added resource. **Note**: you see this because have run `azd infra synth`, delete the **infra** folder and then run `azd provision` or run `azd infra synth` again to re-sythesize the infrastructure before running `azd provision`.
1. Otherwise, select either Yes to provision the changes.

## Running the app and redeploy to Azure

We will skip running app locally but similar to previous exercise, if you want to do that, run `azd show gpt-4o` and set the environment variable. Reminder: Line 33 in app.py.

![app.py](/Lab-Instructions/Images/3.appcode.png)

## Running the app
If you didn't change any of the app code, you do not need to run `azd deploy`. 

**Hint**: you can always run `azd show` to get the end point of your app running on Azure if you don't already have it open.

1. Go to your app end point.
2. Under AI Hotel Recommendations, click the "Get Recommendations" button. Chat will say "I don't know".
3. Switch the "Use grounding with AI Search" toggle to on and click "Get Recommendations" button and you will see:

![Chat with grounding data](/Lab-Instructions/Images/3.chat-grounding.png)

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
      - gpt-4o
  search:
    type: ai.search
  gpt-4o:
    type: ai.openai.model
    model:
      name: gpt-4o
      version: "2024-11-20"
```

## Lab challenges

The app has a toggle at the top right corner that allow you to switch the model to a Foundry model. 

![Foundary toggle](/Lab-Instructions/Images/3.foundrytoggle.png)

Can you use `azd add` and try and see how using a different model affect chat result? 

**Hints**: when you run `azd add`:
* Azure AI services model under the AI category is Foundry model. 
* app.py has hardcoded the model to be Phi-4 for Foundary model so make sure you select Phi-4
* Select AIServices for deployment kind.
* Select 7 for version.

If you successfully add a Foundry model, you can compare and see the difference!
![Comparison of models](/Lab-Instructions/Images/3.Comparision.png)

## Next
[Exercise 4](/Lab-Instructions/Exercise-4.md)
