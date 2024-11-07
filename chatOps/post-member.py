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
    title = item["title"]
    if title != "Sushil's space" and title != "CBT-test3":
        roomId = item["id"]
        membership_url = "https://webexapis.com/v1/memberships"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        body = {
            "roomId": f"{roomId}",
            "personEmail": "SB007bot@webex.bot",
            "isModerator": False,
        }
        post_response = requests.post(
            membership_url, headers=headers, data=json.dumps(body)
        )
        post_response.raise_for_status()
        print("Status Code:", post_response.status_code)
        if post_response.status_code == 200:
            print(f"[green]SUCCESS![/green] user:SB007bot@webex.bot added to {title}")
        else:
            print("Error")
    else:
        print(f"[yellow]Skipping room '{title}': No action required.[/yellow]")
 