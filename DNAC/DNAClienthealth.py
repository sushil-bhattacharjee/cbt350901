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

health_endpoint = "/intent/api/v1/client-health"
client_health = requests.get(url=f"{base_url}{health_endpoint}",
                     headers=req_headers, verify=False).json()
print(json.dumps(client_health, indent=2))

##Client Health analysis
scores = client_health['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == "WIRED":
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == "WIRELESS":
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(
                f"  {score_value['scoreCategory']['value']}: {score_value['clientCount']}")