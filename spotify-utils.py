import requests
import base64
from os import environ, path
import datetime
import json
import spotipy
import spotipy.util as util
import pyperclip

scope = 'user-library-read user-read-currently-playing user-read-playback-state'

sp = None


def auth(username=None):
    global sp
    username = environ["SPOTIFY-USERNAME"] if username == None else username
    scope = environ["SPOTIFY-TOKEN-SCOPE"]
    token = util.prompt_for_user_token(
        username=username,
        scope=scope
    )
    sp = spotipy.Spotify(auth=token)


def getCurrentPlayingTrack(username=None):
    auth(username=username)
    if(sp):
        currentTrack = sp.current_playback()
        if (currentTrack):
            print(currentTrack["item"])
            url = currentTrack["item"]["external_urls"]["spotify"]
            pyperclip.copy(url)
        else:
            print("No track currently playing.")
