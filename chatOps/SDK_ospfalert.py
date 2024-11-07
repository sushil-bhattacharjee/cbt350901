import requests
import json
import os
from rich import print
from nornir import InitNornir
#from nornir.core import InitNornir
#from nornir_salt.plugins.tasks import netmiko_send_commands
#from nornir.plugins.tasks.networking import netmiko_send_command
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins. functions import print_result
from webexteamssdk import WebexTeamsAPI

access_token = (
    "Yzk0ZmQzZWItNDYyMy00NTI0LTgwYWUtODA5ZDcxYjE2ZmRhY2ZkYTFiYmMtYTc4_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
)

api = WebexTeamsAPI(access_token=access_token)

nr = InitNornir()
clear_command = "clear"
os.system(clear_command)


def ospftest(task):
    dev_name = task.host
    my_list = []
    result = task.run(
        netmiko_send_command, command_string="show ip ospf neigh", use_genie=True
    )
    task.host["facts"] = result.result
    interfaces = task.host["facts"]["interfaces"]
    for interface in interfaces:
        neighbor = interfaces[interface]["neighbors"]
        for adjacency in neighbor:
            my_list.append(adjacency)
    num_neighbors = len(my_list)
    if num_neighbors == 2:
        print(f"{dev_name}: [green]PASSED[/green]")
    else:
        print(f"{dev_name}: [red]FAILED[/red]")
        fail_report(dev_name)

def fail_report(dev_name):
    rooms = api.rooms.list( )
    for room in rooms :
        if room.title == "ALERTS":
            target_room = room.id
    api.messages.create(target_room, text=f"ALERT: {dev_name} OSPF NEIGHBOR FAILURE")

results = nr.run(task=ospftest)

#If you want to use environment variable for Token, then delete line 13, access_token
#Store your Token in environment varible file like, myToken.sh
#Before running this python file following -
#step-1: in the bash type [source myToken.sh]
#Step-2: in the bash type [python3.SDK_ospfalert.py]