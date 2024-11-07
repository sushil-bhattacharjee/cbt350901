import json
import requests

url = "https://10.10.20.65/api/fdm/v6/object/networks"

#To send get requests for particular network id
url1 = "https://10.10.20.65/api/fdm/v6/object/networks/3967d614-7504-11ef-903a-29b863e27da2"

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjY1ODY2NjQsInN1YiI6ImFkbWluIiwianRpIjoiZWI2NTdlMDUtNzUwOC0xMWVmLTkwM2EtZjExMzI2NmZkYjk3IiwibmJmIjoxNzI2NTg2NjY0LCJleHAiOjE3MjY1ODg0NjQsInJlZnJlc2hUb2tlbkV4cGlyZXNBdCI6MTcyNjU4OTA2NDEyNiwidG9rZW5UeXBlIjoiSldUX0FjY2VzcyIsInVzZXJVdWlkIjoiMjA2NjgzODQtOTk1Mi0xMWVjLWJlMjQtYTViMTQxNjFmMzA3IiwidXNlclJvbGUiOiJST0xFX0FETUlOIiwib3JpZ2luIjoicGFzc3dvcmQiLCJ1c2VybmFtZSI6ImFkbWluIn0.z5gAdfYCOKAMfOFiEpanIZfD9QniQuvHvd72yxvnrkA'
}

response = requests.request("GET", url, headers=headers, verify=False)

print(response.text)