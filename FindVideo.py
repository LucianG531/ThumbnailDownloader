#!/usr/bin/env python
from apiclient.discovery import build
"""

Python script designed to download thumbnail from last video in a channel
"""
#TODO: Finish documentation

base_url = "https://www.youtube.com/watch?v="
key = input("Enter google API key:" )
#TODO: Figure out youtube api to pull channel id from channel name
#      to make it easier for the user
cid = input("Enter channel id: ")
youtube = build('youtube','v3', developerKey=key)


def getPlaylistID(channel_id):
    response = youtube.channels().list(id = channel_id, part = 'contentDetails').execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

#TODO: Eventually modify both scripts so user can select how many thumbnails they want
def getLastVideoThumb():
    response = youtube.playlistItems().list(playlistId = getPlaylistID(cid), part = 'snippet',maxResults=1).execute()
    return response['items'][0]['snippet']['thumbnails']['maxres']['url']


