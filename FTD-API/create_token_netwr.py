import requests
import json
from rich import print

# To turn off certificates warnings
requests.packages.urllib3.disable_warnings()

#Create a token to access Firepower Manager
url = "https://10.10.20.65/api/fdm/v6/fdm/token"
payload = {"grant_type": "password", "username": "admin", "password": "Sbxftd1234!"}
headers = {"Accept": "application/json", "Content-Type": "application/json"}

token_response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
token_response.raise_for_status()
if token_response.status_code == 200:
    print("Token Successfully Received...\n")
    

#Create an Network object using aforesaid token 
token = token_response.json()["access_token"]

url1 = "https://10.10.20.65/api/fdm/v6/object/networks"
payload1 = {
    "name": "JAMESBOND",
    "description": "DEVCORE-FTD1",
    "subType": "NETWORK",
    "value": "7.7.7.0/24",
    "dnsResolution": "IPV4_ONLY",
    "type": "networkobject",
}
headers1 = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": f"Bearer {token}"}

post_response = requests.post(url1, headers=headers1, data=json.dumps(payload1), verify=False)

post_response.raise_for_status()
if post_response.status_code == 200:
    print("[u]SUCCESS: New Object Created")
    
#Send the get requests to check all the network objects

get_response = requests.get(url1, headers=headers1, verify=False)
print(get_response.text)