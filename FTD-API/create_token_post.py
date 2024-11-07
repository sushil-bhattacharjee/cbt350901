#As First-step, it requires to create a token. Then we use that token for GET/POST networks objectid

import json
import requests

url = "https://10.10.20.65/api/fdm/v6/fdm/token"

payload = json.dumps({
  "grant_type": "password",
  "username": "admin",
  "password": "Sbxftd1234!"
})

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)