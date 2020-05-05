import requests
import base64
from os import environ, path
import datetime
import json
tokenUrl = "https://accounts.spotify.com/api/token"


def generateNewToken(clientID=None, clientSecret=None):
    clientID = environ["MOKHA_SPOTIFY_CLIENT_ID"] if clientID == None else clientID
    clientSecret = environ["MOKHA_SPOTIFY_SECRET_ID"] if clientSecret == None else clientSecret
    client_ID_Secret = "%s:%s" % (clientID, clientSecret)
    b64 = base64.b64encode(client_ID_Secret.encode()).decode()
    requestHeaders = {"Authorization": "Basic %s" % (b64)}
    requestBody = {
        "grant_type": "client_credentials"
    }
    r = requests.post(tokenUrl, data=requestBody, headers=requestHeaders)
    responseJSON = r.json()
    if (r.status_code == 200):
        now = datetime.datetime.now()
        tokenExpiresIn = responseJSON["expires_in"]
        print(tokenExpiresIn)
        token = responseJSON["access_token"]
        tokenExpiryDateTime = now + datetime.timedelta(seconds=tokenExpiresIn)
        print(tokenExpiryDateTime)
        cache = {"token": token, "expiry": str(tokenExpiryDateTime)}
        with open("cache.json", "w") as f:
            json.dump(cache, f)
        return (True, token)
    else:
        print("There was en error authorizing your credentials.")
        return (False, None)


def auth(clientID=None, clientSecret=None):
    token = None
    if (path.exists("cache.json")):
        with open("cache.json") as f:
            cache = json.load(f)
        tokenExpiry = cache["expiry"]
        tokenExpiryDateTime = datetime.datetime.strptime(
            tokenExpiry, "%Y-%m-%d %H:%M:%S.%f")
        tokenExpired = tokenExpiryDateTime < datetime.datetime.now()
        if (not tokenExpired):
            print("Token was cached and is not expired.")
            return (True, cache["token"])
    print("Cached Token either didn't exist or was expired, generating a new one.")
    return generateNewToken(clientID=clientID, clientSecret=clientSecret)


def getCurrentPlayingTrack():
    (authorized, token) = auth()
    print(authorized)
    print(token)
    print("Getting the currently playing track's URL.")


getCurrentPlayingTrack()
