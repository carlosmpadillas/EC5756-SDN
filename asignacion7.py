import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload=response.json()
<<<<<<< HEAD
pprint(payload)
response.raise_for_status()
=======
pprint(payload) 
################### SCRIPT EDITADO #############################
data = payload.get('Token')
response = requests.get(
'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
headers={'X-Auth-Token':data}
)
################################################
x=response.text.encode('utf8')
nameList = []
nameList = json.loads(x)
################### TABLA DE DATOS #############################
for response in nameList['response']:
  print('family:', response['family'])
  print('hostname:', response['hostname'])
  print('managementIpAddress:', response['managementIpAddress'])
  print('lastUpdated:', response['lastUpdated'])
  print('reachabilityStatus:', response['reachabilityStatus'])
  print('')

>>>>>>> sandbox
