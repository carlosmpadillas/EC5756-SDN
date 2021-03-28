#Autor: Carlos Padilla 
#Carnet: 15-11061
import requests
from pprint import pprint
import json
import time

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload=response.json()
################### SCRIPT EDITADO #############################
data = payload.get('Token')
while True:
  response = requests.get(
      'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
      headers={'X-Auth-Token':data}
      )
################################################
  x=response.text.encode('utf8')

  nameList = []
  nameList = json.loads(x)
  JSONF = {}
  JSONF['response'] = []
  for response in nameList['response']:
    JSONF['response'].append({
        'hostname': response['hostname'],
        'reachabilityStatus': response['reachabilityStatus']})
  with open('JSONF.json', 'w') as file:
      json.dump(JSONF, file, indent=4)
  print('.json file successfully created')
  time.sleep(300)