
# Virtual Machine Requirements

### Link to the VM

[Skillable VM Image](https://labondemand.com/LabProfile/185838)

### This is a list of dependencies that must be installed on the Lab VMs:

- Git
- Docker Desktop
- VS Code
- VS Code extensions
    - GitHub Copilot for Azure
    - Azure Developer CLI (azd)
    - Bicep
    - **Azure Tools extension pack**
    - **Python**
- Azure Developer CLI (azd) (`winget install Microsoft.Azd --version 1.17.100`)
- **Azure CLI (az) (`winget install Microsoft.AzureCLI`)**
- Python3 (and create venv) (`winget install Python.Python.3.12` unless there a different version is needed)
- **PowerShell 7.5.1 (`winget install Microsoft.Powershell`)**
- **Windows Terminal (`winget install Microsoft.WindowsTerminal`)**

### Each participant needs access to:
- An active Azure account
- Owner or Contributor access to the Azure subscription
- Permission to create and Azure AI Foundry project (to add AI Search and AI Models)
- AI quota
- GitHub Copilot license