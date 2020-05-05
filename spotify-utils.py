import requests
import base64
from os import environ


def auth(clientID=environ["MOKHA_SPOTIFY_CLIENT_ID"], clientSecret=environ["MOKHA_SPOTIFY_SECRET_ID"]):
    client_ID_Secret = "%s:%s" % (clientID, clientSecret)
    b64 = base64.b64encode(client_ID_Secret.encode()).decode()
    print(b64)
    headers = {"Authorization": "Bearer %s" % (b64)}
    print(headers)


def getCurrentPlayingTrack():
    auth()
    print("Getting the currently playing track's URL.")
