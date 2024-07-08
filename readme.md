http://aigenty-chatbot.eastus.azurecontainer.io:3000/query_properties

---

# Aigenty Chatbot

This guide explains how to set up repository secrets and configure GitHub Actions for automatic deployment to Azure.

## Step-by-Step Guide

### 1. Log in to Azure (if not already logged in)

```sh
az login
```

### 2. Add Repository Secrets

#### Go to your GitHub repository:

1. Click on `Settings`.
2. In the left sidebar, click on `Secrets and variables`, then `Actions`.
3. Click on `New repository secret`.

#### Add `AZURE_CREDENTIALS` Secret:

- **Name:** `AZURE_CREDENTIALS`
- **Value:** Paste the JSON output from the following Azure CLI command:

  ```sh
  az ad sp create-for-rbac --name "github-actions" --sdk-auth --role contributor --scopes /subscriptions/<subscription-id>/resourceGroups/<your-resource-group>
  ```

#### Add `AZURE_RESOURCE_GROUP` Secret:

- **Name:** `AZURE_RESOURCE_GROUP`
- **Value:** `your-resource-group` //aigenty-portal

#### Add `REGISTRY_USERNAME` Secret:

- **Name:** `REGISTRY_USERNAME`
- **Value:** `your-registry-username`

#### Add `REGISTRY_PASSWORD` Secret:

- **Name:** `REGISTRY_PASSWORD`
- **Value:** Paste the output from the following Azure CLI command

```sh
 az acr credential show --name <your-registry-name> --query "passwords[0].value" --output tsv
```

