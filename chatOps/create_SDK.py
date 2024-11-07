from webexteamssdk import WebexTeamsAPI
from rich import print


#This is personal access Token
access_token = "Yzk0ZmQzZWItNDYyMy00NTI0LTgwYWUtODA5ZDcxYjE2ZmRhY2ZkYTFiYmMtYTc4_P0A1_024cf1cc-0fff-4459-9d22-2bf3b7018d17"
api = WebexTeamsAPI(access_token=access_token)
demo_room = api.rooms.create("SDK room")
api.messages.create(demo_room.id, text="Welcome to SDK room")