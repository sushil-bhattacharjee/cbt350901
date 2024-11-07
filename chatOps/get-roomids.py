import requests
import json
from rich import print

token = "Yzk0ZmQzZWItNDYyMy00NTI0LTgwYWUtODA5ZDcxYjE2ZmRhY2ZkYTFiYmMtYTc4_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
url = "https://webexapis.com/v1/rooms"
headers = {"Authorization": f"Bearer {token}"}
get_response = requests.get(url, headers=headers).json()

print(get_response)

items = get_response["items"]
for item in items:
    roomId = item["id"]
    roomName = item["title"]
    print(f"Room {roomName} has an ID od {roomId}")
    
    
#If you want to use environment variable for Token, then delete line 5, token
#Store your Token in environment varible file like, myToken.sh
#Before running this python file following -
#step-1: in the bash type [source myToken.sh]
#Step-2: in the bash type [python3 get-roomids.py]