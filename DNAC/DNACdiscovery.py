import env_lab
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3
from rich import print
from colorama import Fore, Style

#Disable wanrings
urllib3.disable_warnings()

#Headers and credentials
base_url = "https://10.10.20.85:443/dna"
auth_endpoint = "/system/api/v1/auth/token"

username = 'admin'
password = 'Cisco1234!'


#Get Token
auth_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

auth_req = requests.post(url=f"{base_url}{auth_endpoint}", 
                         auth=HTTPBasicAuth(username, password), 
                         headers=auth_headers, verify=False)
auth_response = auth_req.json()
token = auth_response['Token']
print(token)

#POST cli credentials
# cli_url = '/intent/api/v1/global-credential/cli'
# payload = json.dumps([
#     {
#         "comments": "Cli_password",
#         "credentialType": "GLOBAL",
#         "description": "Cli_password",
#         "enablePassword": "Cisco123!",
#         "password": "Cisco123!",
#         "username": "admin"
#     }
# ])
# req_headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "X-auth-token": token
# }
# response_cli = requests.post(url=f"{base_url}{cli_url}",
#                              headers=req_headers, data=payload, verify=False)

#POST snmp write community credentials
# snmp_url = '/intent/api/v1/global-credential/snmpv2-write-community'
# payload = json.dumps([
#     {
#         "comments": "snmpv2_wr_com",
#         "credentialType": "GLOBAL",
#         "description": "snmpv2_wr_com",
#         "writeCommunity": "admin"
#     }
# ])
# req_headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "X-auth-token": token
# }
# response_cli = requests.post(url=f"{base_url}{snmp_url}",
#                              headers=req_headers, data=payload, verify=False)


#GET all global credentials
global_endpoint = '/intent/api/v2/global-credential'
req_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-auth-token": token
}

global_credentials = requests.get(url=f"{base_url}{global_endpoint}",
                               headers=req_headers, verify=False).json()
result = json.dumps(global_credentials, indent=2)
print(f"[blue]All the GLOBAL CREDENTIALS: {result}\n")

#GET individual credentials
cli_endpoint = '/intent/api/v1/global-credential?credentialSubType=CLI'
req_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-auth-token": token
}

cli_credentials = requests.get(url=f"{base_url}{cli_endpoint}",
                               headers=req_headers, verify=False).json()
print(f"[red]Print the CLI CREDENTIALS: {json.dumps(cli_credentials, indent=2)}\n")
cli_cred_id = cli_credentials['response'][0]['id']


snmp_wr_endpoint = '/intent/api/v1/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY'
snmp_wr_credentials = requests.get(url=f"{base_url}{snmp_wr_endpoint}",
                               headers=req_headers, verify=False).json()
print(f"[green] Print the SNMPv2_WR-COMM: {json.dumps(snmp_wr_credentials, indent=2)}")
snmp_wr_id = snmp_wr_credentials['response'][0]['id']


##GET Discovery
payload = {
    "name": "Fusion Router Discovery",
    "discoveryType": "Range",
    "ipAddressList": "10.10.20.175-10.10.20.178",
    "timeout": 1,
    "protocolOrder": "ssh,telnet",
    "preferredMgmtIPMethod": "None",
    "globalCredentialIdList": [cli_cred_id, snmp_wr_id]
}

discovery_endpoint = "/intent/api/v1/discovery"
disc_response = requests.post(url=f"{base_url}{discovery_endpoint}",
                              headers=req_headers, data=json.dumps(payload), verify=False).json()
print(json.dumps(disc_response, indent=2))