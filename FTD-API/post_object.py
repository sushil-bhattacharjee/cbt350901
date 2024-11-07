import requests
import json

url = "https://10.10.20.65/api/fdm/v6/object/networks"

payload = json.dumps({
  "name": "SUSHIL007",
  "description": "CBT007",
  "subType": "HOST",
  "value": "1.0.0.1",
  "dnsResolution": "IPV4_ONLY",
  "type": "networkobject"
})
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjY1ODQ5NDUsInN1YiI6ImFkbWluIiwianRpIjoiZWIxOWNiYzktNzUwNC0xMWVmLTkwM2EtYzkxNDc3MmVjOGRjIiwibmJmIjoxNzI2NTg0OTQ1LCJleHAiOjE3MjY1ODY3NDUsInJlZnJlc2hUb2tlbkV4cGlyZXNBdCI6MTcyNjU4NzM0NTY0MywidG9rZW5UeXBlIjoiSldUX0FjY2VzcyIsInVzZXJVdWlkIjoiMjA2NjgzODQtOTk1Mi0xMWVjLWJlMjQtYTViMTQxNjFmMzA3IiwidXNlclJvbGUiOiJST0xFX0FETUlOIiwib3JpZ2luIjoicGFzc3dvcmQiLCJ1c2VybmFtZSI6ImFkbWluIn0.HK7MiP9-TUmszN29L2ei9-Y8Uh0UadoNTmsk6EYQuOE'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
