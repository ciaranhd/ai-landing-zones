param localVirtualNetworkName string
param remoteVirtualNetworkName string
param remoteVirtualNetworkResourceGroupName string
param remoteSubscriptionId string 

resource peering 'Microsoft.Network/virtualNetworks/virtualNetworkPeerings@2024-07-01' = {
  name: '${localVirtualNetworkName}/peerTo${remoteVirtualNetworkName}'
  properties: {
    allowVirtualNetworkAccess: true
    allowForwardedTraffic: true
    allowGatewayTransit: false
    useRemoteGateways: false  
    remoteVirtualNetwork: {
      id:  resourceId( remoteSubscriptionId, remoteVirtualNetworkResourceGroupName, 'Microsoft.Network/virtualNetworks',remoteVirtualNetworkName)
    }
  }
}
