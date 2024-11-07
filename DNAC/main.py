import requests
from requests.auth import HTTPBasicAuth
import env_lab
from rich import print
requests.packages.urllib3.disable_warnings()

def get_auth_token():
    #Endpoint URL
    endpoint = '/dna/system/api/v1/auth/token'
    url = 'https://' + env_lab.DNA_CENTRE['host'] + endpoint
    #Make the POST request
    resp = requests.post(url, auth=HTTPBasicAuth(env_lab.DNA_CENTRE['username'], env_lab.DNA_CENTRE['password']), verify=False)
    #Retrive the TOKEN from the returned json
    token = resp.json()['Token']
    #PRINT out the Token
    print("Token Retrived: {}".format(token))
    #Create a return statement to send the token back for later use
    return token

if __name__ == "__main__":
    get_auth_token()