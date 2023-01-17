####################################################
# VIEW THE INTERFACE STATUS / DETAILS VIA RESTCONF #
####################################################

import requests
import json
from pprint import pprint

sandboxURL = "sandbox-iosxe-recomm-1.cisco.com"
sandboxPort = "443"
sandboxUser = "developer"
sandboxPass = "C1sco12345"

# Router
router = {
    "host": sandboxURL,
    "port": sandboxPort,
    "username": sandboxUser,
    "password": sandboxPass
}

# REST API Headers
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# Request URL
url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(
    url,
    headers=headers,
    auth=(router["username"], router["password"]),
    verify=False
)

api_data = response.json()
print("/" * 50)
pprint(api_data)
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print('Interface is UP')
