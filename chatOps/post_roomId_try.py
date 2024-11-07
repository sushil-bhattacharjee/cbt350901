import requests
import json
from rich import print

# Define the access token and API endpoint
token = "Yzk0ZmQzZWItNDYyMy00NTI0LTgwYWUtODA5ZDcxYjE2ZmRhY2ZkYTFiYmMtYTc4_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
url = "https://webexapis.com/v1/rooms"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

# List of room titles to create
room_titles = ["Marketing", "Development", "Sales", "Support"]

# Iterate over the list and create each room
for title in room_titles:
    payload = json.dumps({"title": title})
    
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Check if the request was successful
        
        response_data = response.json()
        print(f"[green]Room '{title}' created successfully:[/green]\n{response_data}")


    except requests.exceptions.RequestException as e:
        print(f"[red]Failed to create room '{title}': {e}")
