param dbwStorageAccountName string
param location string
param dbwStorageConfig object
param shouldCreateContainers bool = true
param containerNames array


resource adls 'Microsoft.Storage/storageAccounts@2021-08-01' =  {    
  name: dbwStorageAccountName
    location: location
    kind: dbwStorageConfig.kind
    sku: {
      name: dbwStorageConfig.sku_name
    }
    properties: {
      allowBlobPublicAccess: dbwStorageConfig.allowBlobPublicAccess
      isHnsEnabled: dbwStorageConfig.isHnsEnabled
      accessTier: dbwStorageConfig.accessTier
      publicNetworkAccess: 'Disabled'
      
    }

    // Nested Resource Deployment - Containers within Storage Account
    resource blobServices 'blobServices' = {
      name: 'default'
      resource containersCreate 'containers' = [for ContainerName in containerNames: if (shouldCreateContainers) {
        name: ContainerName
        properties: {
          publicAccess: 'None'
        }
      }]
    }
}
