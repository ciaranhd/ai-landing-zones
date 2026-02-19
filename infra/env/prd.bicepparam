using '../main.bicep'
param zone = 'a'
param resourceGroupName = 'rg-${zone}-bk-fgh-${environment}-corp-${location}-001'
param location = 'uksouth'
param project = 'mlops'  
param environment = 'prd'
param bu = 'pr'
param hubEnvironment = 'prd'
param vnet001  = 'vnet-${zone}-${bu}-${project}-${environment}-corp-${location}-001'
param snet004 = 'snet-p-${hubEnvironment}-connect-${location}-004'  
param addressPrefix001 = '10.8.0.0/18'
param rt001 = 'rt-${zone}-${bu}-${project}-${environment}-corp-${location}-001'
param nsg002 = 'nsg-${zone}-${bu}-${project}-${environment}-corp-${location}-002'
param nsg003 = 'nsg-${zone}-${bu}-${project}-${environment}-corp-${location}-003'
param hubResourceGroupName = 'rg-p-${hubEnvironment}-connect-${location}-001'
param hubVnetName  = 'vnet-p-${hubEnvironment}-connect-${location}-001' 
param dbwName = 'dbw-${zone}-${bu}-${project}-${environment}-corp-${location}-001'
param dbwMrgName = 'mrg-${zone}-${bu}-${project}-${environment}-corp-${location}-001'
param dbwStorageAccountName = 'st${zone}${bu}${project}${environment}${location}01'
param containerNames = [
    'raw'
    'processed'
    'curated'
]
param shouldCreateContainers = true
param dbwStorageConfig = {
  kind: 'StorageV2'
  sku_name: 'Standard_LRS'
  allowBlobPublicAccess: false
  isHnsEnabled: true
  accessTier: 'Hot'
}
param subscriptionId = ''
param hubSubscriptionId = '7ce7a560-ee30-4e97-bf6c-7d55fdb53489' 
