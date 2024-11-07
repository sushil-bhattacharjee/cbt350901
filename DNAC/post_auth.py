import requests

url = "https://10.10.20.85/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28xMjM0IQ=='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
