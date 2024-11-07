import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

#Disable warnings
requests.packages.urllib3.disable_warnings()

def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = f'https://{DNAC_IP}:{DNAC_PORT}/dna/system/api/v1/auth/token'  # Use the configured IP and port
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)  # Make the POST Request
    token = resp.json()['Token']  # Retrieve the Token 
    return token  # Return the Token

def get_device_list():
    """
    Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint
    """
    token = get_auth_token()  # Get Token
    url = f"https://{DNAC_IP}:{DNAC_PORT}/api/v1/network-device"
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    resp = requests.get(url, headers=hdr, verify=False)  # Make the GET Request
    device_list = resp.json()
    get_device_id(device_list, token)  # Call the function to get device IDs, passing the token

def get_device_id(device_json, token):
    """
    Function to print device IDs and call interface info for each device
    """
    for device in device_json['response']: 
        print("Fetching Interfaces for Device Id ----> {}".format(device['id']))
        print('\n')
        get_device_int(device['id'], token)  # Pass the token to get_device_int()
        print('\n')

def get_device_int(device_id, token):
    """
    Function to retrieve device interface info using requests.get
    """
    url = f"https://{DNAC_IP}:{DNAC_PORT}/api/v1/interface"
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}
    querystring = {"macAddress": device_id}  # Using device_id (not MAC address) for querying
    resp = requests.get(url, headers=hdr, params=querystring, verify=False) 
    interface_info_json = resp.json()
    print_interface_info(interface_info_json)

def print_interface_info(interface_info):
    """
    Function to format and print interface information
    """
    print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for intf in interface_info['response']:
        print("{0:42}{1:10}{2:12}{3:18}{4:17}{5:10}{6:15}".
              format(str(intf['portName']),
                     str(intf['vlanId']),
                     str(intf['portMode']),
                     str(intf['portType']),
                     str(intf['duplex']),
                     str(intf['status']),
                     str(intf['lastUpdated'])))

if __name__ == "__main__":
    get_device_list()
