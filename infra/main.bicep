targetScope =  'subscription'  

@description('SubscriptionId.')
param subscriptionId string

@description('Required. The name of the Spoke resource group containing core resources')
param resourceGroupName string


@description('Required. The location of the azure resource group and resources contained within')
param location string 


param zone string 
 
@description('Required. The networking address prefix for the Subnets')
param addressPrefix001 string 

@allowed([
    'dev'
    'uat'
    'prd'
])
@description('Required. Environment of the spoke landing zone')
param environment string

@allowed([
    'dev'
    'uat'
    'prd'
])
@description('All spoke environments will use default use production hub connectivity vnet')
param hubEnvironment string  

@description('Required. Databricks Route Table Name')
param rt001 string

@description('Databricks NSG')
param nsg002 string

@description('Default NSG')
param nsg003 string 

@description('AI Spoke Vnet Name')
param vnet001 string

@description('The databricks route table resource id.')
param databricksRouteTableResourceId string = resourceId(subscriptionId, resourceGroupName,'Microsoft.Network/routeTables', rt001)

@description('The databricks network security group resource id.')
param databricksNsgResourceId string = resourceId(subscriptionId, resourceGroupName,'Microsoft.Network/networkSecurityGroups', nsg002)


param snet004 string 
@description('The default network security group resource id.')
param defaultNetworkSecurityGroupId string = resourceId(subscriptionId, resourceGroupName,'Microsoft.Network/networkSecurityGroups', nsg003)

param hubResourceGroupName string

param hubVnetName string

param dbwName string

param dbwMrgName string

param dbwStorageConfig object 

param containerNames array 

param shouldCreateContainers bool

param hubSubscriptionId string


param bu string

param project string

@description('The name of the storage account to be used by the databricks workspace.')
param dbwStorageAccountName string

var hubVnetId = resourceId(hubSubscriptionId, hubResourceGroupName, 'Microsoft.Network/virtualNetworks', hubVnetName)

var hubSubnetId = resourceId(hubSubscriptionId, hubResourceGroupName, 'Microsoft.Network/virtualNetworks/subnets',hubVnetName ,snet004) // default subnet

var hubPrivateDnsZoneResourceId = resourceId(hubSubscriptionId, hubResourceGroupName, 'Microsoft.Network/privateDnsZones', 'privatelink.azuredatabricks.net')


@description('Required. An Array of subnets to deploy to the Virtual Network.')
var subnets  = [
  {
    addressPrefix: cidrSubnet(addressPrefix001, 26, 1)
    name:  'snet-${zone}-${bu}-${project}-${environment}-corp-${location}-002' // This is the public subnet for the databricks workspace
    privateLinkServiceNetworkPolicies: 'Enabled'
    privateEndpointNetworkPolicies: 'Enabled'
    routeTableResourceId: databricksRouteTableResourceId
    networkSecurityGroupResourceId: databricksNsgResourceId
    delegation: 'Microsoft.Databricks/workspaces'
  }
  {
    addressPrefix: cidrSubnet(addressPrefix001, 26, 2)
    name:  'snet-${zone}-${bu}-${project}-${environment}-corp-${location}-003' // This is the private subnet for the databricks workspace
    privateLinkServiceNetworkPolicies: 'Enabled'
    privateEndpointNetworkPolicies: 'Enabled'
    routeTableResourceId: databricksRouteTableResourceId
    networkSecurityGroupResourceId: databricksNsgResourceId
    delegation: 'Microsoft.Databricks/workspaces'
  }
  {
    addressPrefix: cidrSubnet(addressPrefix001, 26, 3)
    name: 'snet-${zone}-${bu}-${project}-${environment}-corp-${location}-004' // This is the default subnet for the spoke
    privateLinkServiceNetworkPolicies: 'Enabled'
    privateEndpointNetworkPolicies: 'Enabled'
    networkSecurityGroupResourceId: defaultNetworkSecurityGroupId
    delegation: ''
  }
  {
    addressPrefix: cidrSubnet(addressPrefix001, 26, 0)
    name: 'snet-${zone}-${bu}-${project}-${environment}-corp-${location}-001'
    privateLinkServiceNetworkPolicies: 'Enabled'
    privateEndpointNetworkPolicies: 'Enabled'
    delegation: 'Microsoft.DevOpsInfrastructure/pools'
  }
]

var databricksWorkspaceRouteTableRoutes  = [
  {
    name: 'adb-servicetag'
    properties: {
      addressPrefix: 'AzureDatabricks'
      nextHopType: 'Internet'
      nextHopIpAddress: ''
    }
  }
  {
    name: 'adb-metastore'
    properties: {
      addressPrefix: 'Sql.UKSouth'
      nextHopType: 'Internet'
      nextHopIpAddress: ''
    }
  }
  {
    name: 'adb-storage'
    properties: {
      addressPrefix: 'Storage.UKSouth'
      nextHopType: 'Internet'
      nextHopIpAddress: ''
    }
  }
  {
    name: 'default'
    properties: {
      addressPrefix: '0.0.0.0/0'
      nextHopType: 'VirtualAppliance'
      nextHopIpAddress: '10.9.6.4' // URGENT : This was inserted manually after platform-core deployment. the process should be automated.
  }
 }
]

var dbrNsgRules = [
  {
    name: 'Microsoft.Databricks-workspaces_UseOnly_databricks-worker-to-worker-inbound'
    properties: {
      description: 'Required for worker nodes communication within a cluster.'
      protocol: '*'
      sourcePortRange: '*'
      destinationPortRange: '*'
      sourceAddressPrefix: 'VirtualNetwork'
      destinationAddressPrefix: 'VirtualNetwork'
      access: 'Allow'
      direction: 'Inbound'
      priority: 100
      sourcePortRanges: []
      destinationPortRanges: []
      sourceAddressPrefixes: []
      destinationAddressPrefixes: []
    }
  }
  {
    name: 'Microsoft.Databricks-workspaces_UseOnly_databricks-worker-to-worker-outbound'
    properties: {
      description: 'Required for worker nodes communication within a cluster.'
      protocol: '*'
      sourcePortRange: '*'
      destinationPortRange: '*'
      sourceAddressPrefix: 'VirtualNetwork'
      destinationAddressPrefix: 'VirtualNetwork'
      access: 'Allow'
      direction: 'Outbound'
      priority: 100
      sourcePortRanges: []
      destinationPortRanges: []
      sourceAddressPrefixes: []
      destinationAddressPrefixes: []
    }
  }
  {
    name: 'Microsoft.Databricks-workspaces_UseOnly_databricks-worker-to-sql'
    properties: {
      description: 'Required for workers communication with Azure SQL services.'
      protocol: 'Tcp'
      sourcePortRange: '*'
      destinationPortRange: '3306'
      sourceAddressPrefix: 'VirtualNetwork'
      destinationAddressPrefix: 'Sql'
      access: 'Allow'
      direction: 'Outbound'
      priority: 101
      sourcePortRanges: []
      destinationPortRanges: []
      sourceAddressPrefixes: []
      destinationAddressPrefixes: []
    }
  }
  {
    name: 'Microsoft.Databricks-workspaces_UseOnly_databricks-worker-to-storage'
    properties: {
      description: 'Required for workers communication with Azure Storage services.'
      protocol: 'Tcp'
      sourcePortRange: '*'
      destinationPortRange: '443'
      sourceAddressPrefix: 'VirtualNetwork'
      destinationAddressPrefix: 'Storage'
      access: 'Allow'
      direction: 'Outbound'
      priority: 102
      sourcePortRanges: []
      destinationPortRanges: []
      sourceAddressPrefixes: []
      destinationAddressPrefixes: []
    }
  }
  {
    name: 'Microsoft.Databricks-workspaces_UseOnly_databricks-worker-to-eventhub'
    properties: {
      description: 'Required for worker communication with Azure EventHb services.'
      protocol: 'Tcp'
      sourcePortRange: '*'
      destinationPortRange: '9093'
      sourceAddressPrefix: 'VirtualNetwork'
      destinationAddressPrefix: 'EventHub'
      access: 'Allow'
      direction: 'Outbound'
      priority: 103
      sourcePortRanges: []
      destinationPortRanges: []
      sourceAddressPrefixes: []
      destinationAddressPrefixes: []
    }
  }
  // I suspect we will need something for Azure DevOps Services, to allow repos and artifact
]

var defaultNsgRule = [
 
]

 module rg 'modules/resource_group.bicep' = {
    name: 'rg'
    params: {
        resourceGroupName: resourceGroupName
        location: location
    }
}

module pdnsZone 'br/public:avm/res/network/private-dns-zone:0.4.0' = {
  scope: resourceGroup(resourceGroupName)
  name: 'pdnsZone'
  params: {
    name: 'privatelink.azuredatabricks.net'
     virtualNetworkLinks: [
      {
        virtualNetworkResourceId: vnet.outputs.resourceId
      }     
    ]
  }
}

module databricksWorkspaceRouteTable 'br/public:avm/res/network/route-table:0.2.2' = {
  scope: resourceGroup(resourceGroupName)
  name: 'databricksWorkspaceRouteTable'
  params: {
    name: rt001
    location: location
    routes: databricksWorkspaceRouteTableRoutes
    //tags: tags
  }
  dependsOn: [
    rg
  ]
}

module databricksWorkspaceNetworkSecurityGroup 'br/public:avm/res/network/network-security-group:0.2.0' = {
  scope: resourceGroup(resourceGroupName)
  name: 'databricksWorkspaceNetworkSecurityGroup'
  params: {
    name: nsg002
    location: location
    //tags: tags
    securityRules: dbrNsgRules
  }
  dependsOn: [
    rg
  ]
}

module defaultNsg 'br/public:avm/res/network/network-security-group:0.2.0' = {
  scope: resourceGroup(resourceGroupName)
  name: 'defaultNsg'
  params: {
    name: nsg003
    location: location
    //tags: tags
    securityRules: defaultNsgRule
  }
  dependsOn: [
    rg
  ]
}

module vnet 'br:mcr.microsoft.com/bicep/avm/res/network/virtual-network:0.7.0' =  {
  scope: resourceGroup(resourceGroupName)
  name: 'vnet' 
  params: {
    name: vnet001
    addressPrefixes: [addressPrefix001]
    subnets: subnets
    // peerings: [
    //   {
    //     remoteVirtualNetworkId: hubVnetId
    //     allowForwardedTraffic: true
    //     allowGatewayTransit: false
    //     allowVirtualNetworkAccess: true
    //     remotePeeringAllowForwardedTraffic: true
    //     remotePeeringAllowVirtualNetworkAccess: true
    //     remotePeeringEnabled: true
    //     remotePeeringName: 'hub-spoke'
    //     useRemoteGateways: false
    //   }
    // ]
  }
  dependsOn: [
    rg
    databricksWorkspaceNetworkSecurityGroup
    databricksWorkspaceRouteTable
    defaultNsg
  ]
}

// Do we need to peer with vnet-a-bi-dev/uat/prd-corp-uksouth-001 - ie vnet containing the managed devops agent pool that does the deployments...

// Peering must be successfully deployed bi-directionally. if not it will remain in the 'Initiated' state.
module SpokeToHubPeering 'modules/vnet_peering.bicep' = {
  scope: resourceGroup(subscriptionId, resourceGroupName)
  name: 'SpokeToHub'
  params: {
    localVirtualNetworkName: vnet.outputs.name
    remoteVirtualNetworkName: hubVnetName
    remoteVirtualNetworkResourceGroupName: hubResourceGroupName
    remoteSubscriptionId: hubSubscriptionId
  }
  dependsOn: [
    vnet
  ]
}

module HubToSpokePeering 'modules/vnet_peering.bicep' = {
  scope: resourceGroup(hubSubscriptionId, hubResourceGroupName)
  name: 'HubToSpoke'
  params: {
    localVirtualNetworkName: hubVnetName //vnet.outputs.name
    remoteVirtualNetworkName: vnet.outputs.name //hubVnetName
    remoteVirtualNetworkResourceGroupName: resourceGroupName //hubResourceGroupName
    remoteSubscriptionId: subscriptionId //hubSubscriptionId
  }
  dependsOn: [
    vnet
  ]
}

module databricksWorkspace 'br/public:avm/res/databricks/workspace:0.11.2'= {
  scope: resourceGroup(resourceGroupName)
  name: 'databricksWorkspace'
  params: {
    name: dbwName
    location: location
    //tags: tags
    skuName: 'premium'
    managedResourceGroupResourceId: subscriptionResourceId(subscriptionId, 'Microsoft.Resources/resourceGroups', dbwMrgName)
    requireInfrastructureEncryption: true
    publicNetworkAccess: 'Disabled'
    requiredNsgRules: 'NoAzureDatabricksRules'
    roleAssignments: [
    ]
    disablePublicIp: true
    customPrivateSubnetName: vnet.outputs.subnetNames[1]
    customPublicSubnetName: vnet.outputs.subnetNames[0]
    customVirtualNetworkResourceId: vnet.outputs.resourceId
    diagnosticSettings: [
    ]
  }
  dependsOn: [
    rg
  ]
}

module dbwDataLake 'modules/data_lake.bicep' = {
  scope: resourceGroup(resourceGroupName)
  name: 'dbwDataLake'
  params: {
    location: location
    containerNames: containerNames
    dbwStorageAccountName: dbwStorageAccountName
    dbwStorageConfig: dbwStorageConfig
    shouldCreateContainers: shouldCreateContainers
  }
  dependsOn: [
    databricksWorkspace
    rg
  ]
}


// Backend private endpoiunt.
// Allow communication between the control plane and the data plane over private link.
module databricksWorkspaceBEPrivateEndpoint 'br/public:avm/res/network/private-endpoint:0.4.1' = {
  scope: resourceGroup(resourceGroupName)
  name: 'databricksWorkspaceBEPrivateEndpoint'
  params: {
    name: 'pe-be-${dbwName}'
    subnetResourceId: vnet.outputs.subnetResourceIds[2]
    privateDnsZoneResourceIds: [
       pdnsZone.outputs.resourceId
    ]
    privateLinkServiceConnections: [
      {
       name: 'pe-be-${databricksWorkspace.outputs.name}'
       properties: {
         groupIds: ['databricks_ui_api']
         privateLinkServiceId: databricksWorkspace.outputs.resourceId
       }
      }
    ]
  }
  dependsOn: [
    databricksWorkspace
  ]
}


// Frontend private endpoint. 
// Allow communication between the user (bastion vm) and the control plane over private link. 
 
module databricksWorkspaceFEPrivateEndpoint 'br/public:avm/res/network/private-endpoint:0.4.1' = {
  scope: resourceGroup(hubSubscriptionId, hubResourceGroupName)
  name: 'databricksWorkspaceFEPrivateEndpoint'
  params: {
    name: 'pe-fe-${dbwName}'
    subnetResourceId: hubSubnetId
    privateDnsZoneResourceIds: [
      hubPrivateDnsZoneResourceId
    ]
    privateLinkServiceConnections: [
      {
       name: 'pe-fe-${databricksWorkspace.outputs.name}'
       properties: {
         groupIds: ['databricks_ui_api']
         privateLinkServiceId: databricksWorkspace.outputs.resourceId
       }
      }
    ]
  }
  dependsOn: [
    databricksWorkspace
    databricksWorkspaceBEPrivateEndpoint
  ]
}


