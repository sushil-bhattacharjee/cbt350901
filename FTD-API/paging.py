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

get_url = "https://10.10.20.65/api/fdm/v6/object/networks"
get_headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

while get_url:
    response = requests.get(get_url, headers=get_headers, params={f"limit": 20}, verify=False)
    response.raise_for_status()
    data = response.json()
    items = data["items"]
    print("\n")
    for item in items:
        name = item["name"]
        subtype = item["subType"]
        value = item["value"]
        print(f"{name} is a {subtype} object with a value of {value}")
    try:
        get_url = data['paging']['next'][0]
        if not get_url:
            break
    except IndexError:
        break