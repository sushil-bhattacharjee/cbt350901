from webexteamssdk import WebexTeamsAPI
from rich import print

#When using environemnt for token, following were disabled
#This is personal access Token
access_token = "Yzk0ZmQzZWItNDYyMy00NTI0LTgwYWUtODA5ZDcxYjE2ZmRhY2ZkYTFiYmMtYTc4_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
api = WebexTeamsAPI(access_token=access_token)

#api = WebexTeamsAPI()
rooms = api.rooms.list()

#Send a Text to a particular roomId
# for room in rooms:
#     #print(room)
#     if room.title == "Marketing":
#         roomId = room.id 
# api.messages.create(roomId, text="Hello Marketing room from SDK")

#Send a message to a roomId that serve a particular condition
for room in rooms:
    #print(room)
    if room.title == "Support":
        roomId = room.id 
if 2 == 2:
    api.messages.create(roomId, text="Alert alert room from SDK")