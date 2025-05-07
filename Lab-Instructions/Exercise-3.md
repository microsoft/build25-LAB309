# Exercise 3: Add AI Chat to your application

Find the best model for this AI scenario using GitHub Copilot for Azure.

## Step 1: Open GitHub Copilot for Azure in VS Code 
1. Locate the GitHub Copilot icon in the top command bar or use the shortcut **Ctrl + Alt + I** to open the chat pane.
2. When prompted to sign in, use the GitHub Enterprise Username and Password found in the **Instructions** tab within the Skillable VM.

## Step 2: Find the best model for this lab's scenario with GitHub Copilot for Azure
1. Make sure you have the mode set to **Ask** and start your prompts with **@azure** to invoke GitHub Copilot for Azure.
2. If necessary, ask follow-up questions and clarifying questions to identify the model to use.

## Step 3: Add AI chat model
We will be using the OpenAI Chat GPT-4o model. The Azure OpenAI Chat GPT-4o model is a powerful language model available through the Azure OpenAI Service. This model is designed for advanced conversational AI tasks.

The Chat GPT-4o model is integrated with Azure's capabilities, providing scalability, security, and enterprise features. There are different variants like GPT-4o Mini, which is a lighter version, and GPT-4 Turbo with Vision, which includes vision capabilities, that you can use for your use case.

## TODO verify that this the model we want to use
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

## Step 4: Add grounding data

## Step 5: Redeploy

## Next
[Exercise 4](/Lab-Instructions/Exercise-4.md)
