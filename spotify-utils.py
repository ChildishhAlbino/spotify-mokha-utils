import requests
import base64
from os import environ

tokenUrl = "https://accounts.spotify.com/api/token"


def auth(clientID=environ["MOKHA_SPOTIFY_CLIENT_ID"], clientSecret=environ["MOKHA_SPOTIFY_SECRET_ID"]):
    client_ID_Secret = "%s:%s" % (clientID, clientSecret)
    b64 = base64.b64encode(client_ID_Secret.encode()).decode()
    print(b64)
    requestHeaders = {"Authorization": "Basic %s" % (b64)}
    requestBody = {
        "grant_type": "client_credentials"
    }
    r = requests.post(tokenUrl, data=requestBody, headers=requestHeaders)
    print(r.json())


def getCurrentPlayingTrack():
    auth()
    print("Getting the currently playing track's URL.")
