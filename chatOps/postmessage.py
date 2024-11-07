import sys
import requests
import json
from rich import print

#Token for the Bot, not the personal token
token = "YjViNTExM2EtMzdiYS00MjRjLWI5ODAtZDA2NjA5ZGU1ZGJkMWZkYWU2ODYtZWE2_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
url = "https://webexapis.com/v1/rooms"
headers = {"Authorization": f"Bearer {token}" }
get_response = requests.get(url, headers=headers)
response_data = get_response.json()
# print(response_data)


items = response_data["items"]
print(items)
for item in items:
    title = item["title"]
    if title == "Marketing":
        roomId = item["id"]

message = sys.argv[1]

def send_message():
    header = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"roomId": f"{roomId}", "text": message}
    return requests.post(
        "https://webexapis.com/v1/messages",
        headers=header,
        data=json.dumps(data),
        verify=True,
    )
    
send_message()

# when you are running the file, you have to type [python3 postmessage.py "Hello! You are sexy!"]

# In Python, sys.argv is a list that contains command-line arguments passed to a script. Here's what each part means:

# sys.argv[0]: This is the name of the script being executed.
# sys.argv[1]: This represents the first argument passed after the script name.
# So, message = sys.argv[1] means that the first command-line argument after the script's name will be assigned to the variable message.

# For example, if you run the script like this:

# bash

# python script.py "Hello, World!"
# sys.argv[0] will be "script.py".
# sys.argv[1] will be "Hello, World!".
# In this case, message will contain the string "Hello, World!". 
# If you don't pass an argument, trying to access sys.argv[1] will raise an IndexError because that element does not exist in sys.argv.