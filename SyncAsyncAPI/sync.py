import requests
base_url = 'http://httpbin.org'
from rich import print as rprint
def get_delay(seconds):
    endpoint = f'/delay/{seconds}'
    print(f'Getting with {seconds} delay ...')
    resp = requests.get(base_url+endpoint)
    data = resp.json()
    rprint(data)
    
    
get_delay(5)

print('Okay! All finished getting.')