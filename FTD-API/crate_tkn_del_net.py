import os
import json
from rich import print
import requests

#Disable warnings
requests.packages.urllib3.disable_warnings()

target = input("Enter the Object you wish to delete: ")
clear_screen = "clear"
os.system(clear_screen)

url = "https://10.10.20.65/api/fdm/v6/fdm/token"
payload = {"grant_type": "password", "username": "admin", "password": "Sbxftd1234!"}
headers = {"Accept": "application/json", "Content-Type": "application/json"}

token_response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
token_response.raise_for_status()
if token_response.status_code == 200:
    print("Token Successfully Received.....")
    
token = token_response.json()["access_token"]

url = "https://10.10.20.65/api/fdm/v6/object/networks"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
}
get_response = requests.get(url, headers=headers, verify=False).json()
items = get_response["items"]
name_list = []
for item in items:
    addname = item["name"]
    name_list.append(addname)
    if item["name"] == target:
        targetname = item["name"]
        objectId = item["id"]
        url = f"https://10.10.20.65/api/fdm/v6/object/networks/{objectId}"
        del_response = requests.delete(url, headers=headers, verify=False)
        if del_response.status_code == 204:
            print(f"[green]SUCCESSFUL[/green]: DELETED {targetname} OBJECT")
            
if target not in name_list:
    print(f"[red]ERROR![/red] {target} OBJECT DOES NOT EXIST")
    
#Send the get requests to check all the network objects
url = "https://10.10.20.65/api/fdm/v6/object/networks"
get_response = requests.get(url, headers=headers, verify=False)
print(get_response.text)