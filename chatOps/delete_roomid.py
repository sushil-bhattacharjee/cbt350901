import requests
import json
from rich import print

# Set the token and base URL
token = "Yzk0ZmQzZWItNDYyMy00NTI0LTgwYWUtODA5ZDcxYjE2ZmRhY2ZkYTFiYmMtYTc4_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
base_url = "https://webexapis.com/v1/rooms"
headers = {"Authorization": f"Bearer {token}"}

# Get the rooms
response = requests.get(base_url, headers=headers)
response_data = response.json()
print(response_data)

# # Loop through the rooms and delete those not matching specified titles
# for room in response_data.get("items", []):
#     room_title = room.get("title")
    
#     # Check if the room title is not in the exclusion list
#     if room_title not in ["Sushil Devnetbot", "CBT-test3"]:
#         room_id = room.get("id")
#         room_url = f"{base_url}/{room_id}"
        
#         # Delete the room
#         del_response = requests.delete(room_url, headers=headers)
#         del_response.raise_for_status()
        
#         # Check the response and print a success message
#         if del_response.status_code == 204:
#             print(f"Room '{room_title}': [red]DELETED[/red]")

items = response_data["items"]
for item in items:
    title = item["title"]
    if title != "Sushil Devnetbot" and title !="CBT-test3":
        roomId = item["id"]
        roomId_url = f"https://webexapis.com/v1/rooms/{roomId}"
        headers = {"Authorization": f"Bearer {token}"}
        del_response = requests.delete(roomId_url, headers=headers)
        del_response.raise_for_status()
        if del_response.status_code == 204:
            print(f"Room {title}: [red]DELETED[/red]")

# Get the rooms
print("[green]PRINT THE ROOMS AFTER DELETION")
response = requests.get(base_url, headers=headers)
response_data = response.json()
print(response_data)
