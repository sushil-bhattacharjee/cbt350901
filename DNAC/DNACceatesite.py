import env_lab
import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3
from rich import print

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

auth_req = requests.post(url=f"{base_url}{auth_endpoint}", auth=HTTPBasicAuth(username, password), headers=auth_headers, verify=False)
auth_response = auth_req.json()
token = auth_response['Token']
print(token)

# Get Sites information
req_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-auth-token": token
}

sites_endpoint = "/intent/api/v1/topology/site-topology"
sites = requests.get(url=f"{base_url}{sites_endpoint}",
                     headers=req_headers, verify=False).json()['response']
print(json.dumps(sites, indent=2))

print(f"[blue]\n Print the fist site",sites['sites'][0])

# #Create Sites
# site_endpoint = '/intent/api/v1/site'
# payload = {
#     "type": "area",
#     "site": {
#         "area": {
#             "name": "Melbourne",
#             "parentName": "Global"
#         }
#     }
# }

# site_response = requests.post(url=f"{base_url}{site_endpoint}",headers=req_headers,data=json.dumps(payload),verify=False)
# result = site_response.json()
# print(json.dumps(result, indent =2))