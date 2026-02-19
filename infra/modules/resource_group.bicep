targetScope =  'subscription' 
param resourceGroupName string
param location string

resource  azResourceGroup 'Microsoft.Resources/resourceGroups@2025-03-01' = {
    name: resourceGroupName
    location: location
}

output location string = azResourceGroup.location

