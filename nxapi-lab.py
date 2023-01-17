import requests
import json

switchUser = 'admin'
switchPassword = 'admin'

url = 'https://192.168.1.68/ins'

myHeader = {'content-type': 'application/json'}

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp neighbor",
        "output_format": "json"
    }
}

response = requests.post(url, data=json.dumps(payload), headers=myHeader, auth=(
    switchUser, switchPassword), verify=False).json()

##############  LOGIN WITH NX-API REST ##############

auth_url = 'https://192.168.1.68/api/mo/aaaLogin.json'
auth_body = {'aaaUser': {"attributes": {
    "name": switchUser, "pwd": switchPassword}}}

auth_response = requests.post(auth_url, data=json.dumps(
    auth_body), timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

cookies = {}
cookies['APIC-cookie'] = token
print(cookies)
