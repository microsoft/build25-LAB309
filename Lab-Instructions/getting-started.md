# Getting started

## Welcome Microsoft Build attendees
The instructions on this page are for Microsoft Build 2025 attendees of Lab309. This assumes you have access to the pre-configured lab environment, which provides an Azure subscription and all the tools you need to complete the workshop.

## Introduction
This workshop is designed to teach you how to build an application with AI Search and AI Chat model working with the GitHub Copilot for Azure agent. The lab exercise modules are designed to be completed in order 1 through 4 building up the application progressively through each exercise.

## Logistics
The lab is 75 minutes. There are two presenters and four proctors, so you will have support throughout the lab.

## Prerequisite Knowledge 
We assume you know the basics of creating and editing files in Visual Studio Code. VS Code isn't very different from other code editors, but if you have never used any code editor you might need a little help. If you need help, please raise your hand and a proctor will explain how to compete these tasks. We're here to help!

## Authenticate with Azure
Navigate to **Resources** in your Skillable VM to locate the user id and password for logging into your Azure account.

## Get the latest Azure Developer CLI (azd) build
Before we get started, let's make sure we have the latest version of azd. Run this PowerShell command.

```powershell
winget upgrade microsoft.azd
```

## Get started with the repo
In this lab, we will start by cloning the lab repository.

1. From the terminal

    Get the LAB content
    ```powershell
    # Clone the repository
    git clone https://github.com/microsoft/build25-LAB309.git
    # Change to the cloned repo directory
    cd build25-LAB309
    # Open in VS Code
    code .
    ```

2. In VS Code

    Open a new Termnial (select PowerShell or Bash depending on preference)

    PowerShell

    ```powershell
    # Change to the src directory
    cd src
    # Create virtual environment
    python -m venv .venv
    # Activate virtual environment
    .\.venv\Scripts\Activate.ps1
    # Install required Python packages
    pip install -r requirements.txt
    # Run the app
    python app.py
    ```
    
    Bash

    ```bash
    # Change to the src directory
    cd src
    # Create virtual environment 
    python -m venv .venv
    # Activate virtual environment
    source .venv/bin/activate
    # Install required Python packages
    pip install -r requirements.txt
    # Run the app
    python app.py
    ```
    Congratulations! You now have your app running locally.
    
    Note: None of the buttons work, but that's expected at this point. We're going to fix those in the exercises.

    Press `ctrl+c` in the Terminal to stop the app.

    ![Screenshot](/Lab-Instructions/Images/app-image.png)

    You are now ready to start. Please continue with Exercise 1.

3. Complete each exercise:
   - [Exercise 1](/Lab-Instructions/Exercise-1.md)
   - [Exercise 2](/Lab-Instructions/Exercise-2.md)
   - [Exercise 3](/Lab-Instructions/Exercise-3.md)
   - [Exercise 4](/Lab-Instructions/Exercise-4.md)
