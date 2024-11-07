import json
import requests

url = "https://10.10.20.65/api/fdm/v6/object/networks"

#To send get requests for particular network id
url1 = "https://10.10.20.65/api/fdm/v6/object/networks/3967d614-7504-11ef-903a-29b863e27da2"

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjY1ODQ5NDUsInN1YiI6ImFkbWluIiwianRpIjoiZWIxOWNiYzktNzUwNC0xMWVmLTkwM2EtYzkxNDc3MmVjOGRjIiwibmJmIjoxNzI2NTg0OTQ1LCJleHAiOjE3MjY1ODY3NDUsInJlZnJlc2hUb2tlbkV4cGlyZXNBdCI6MTcyNjU4NzM0NTY0MywidG9rZW5UeXBlIjoiSldUX0FjY2VzcyIsInVzZXJVdWlkIjoiMjA2NjgzODQtOTk1Mi0xMWVjLWJlMjQtYTViMTQxNjFmMzA3IiwidXNlclJvbGUiOiJST0xFX0FETUlOIiwib3JpZ2luIjoicGFzc3dvcmQiLCJ1c2VybmFtZSI6ImFkbWluIn0.HK7MiP9-TUmszN29L2ei9-Y8Uh0UadoNTmsk6EYQuOE'
}

response1 = requests.request("DELETE", url1, headers=headers, verify=False)

print(response1.text)

#Print the networks after delete operation
response = requests.request("GET", url, headers=headers, verify=False)
print(response.text)