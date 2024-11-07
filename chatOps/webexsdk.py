from webexteamssdk import WebexTeamsAPI

#Disableing folloing hardcoded token, since token is sourcing from the environment file
#access_token = "NjNmM2M5NzEtZTY2OS00NzU1LTgxYjItM2I0OWY5MDc5ZmI0YTI4NGExNmMtZGJm_PF84_865b27d1-f263-4044-9f1c-32c40e62ece8"
#api = WebexTeamsAPI(access_token=access_token)

api = WebexTeamsAPI()
demo_room = api.rooms.create("SDK_ALERTS")
api.messages.create(demo_room.id, text="Warning Warning Warning Warning")