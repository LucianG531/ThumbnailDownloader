#!/usr/bin/env python
from apiclient.discovery import build
"""

Python script designed to download thumbnail from last video in a channel
"""
base_url = "https://www.youtube.com/watch?v="

"""

Tutorial on how to get your google API key:
https://developers.google.com/youtube/v3/getting-started
"""

key = input("Enter google API key:" )

channel_name = input("Enter channel name: ")
youtube = build('youtube','v3', developerKey=key)

# Makes a request to the youtube api to find the channel id given a channel name
# NOTE: Channel name is not unique and script may return different images if
#       multiple channels with the same name exist

def getChannelID():
    response = youtube.search().list(type='channel',part='id',q=channel_name,maxResults=1).execute()
    return response['items'][0]['id']['channelId']

channel_id = getChannelID()

# Makes a request to the youtube api to list the details of the wanted channel's content
# We use it mainly to get the id of the "Uploads" playlist so that we can access
# all uploaded videos on the channel

def getPlaylistID():
    response = youtube.channels().list(id = channel_id, part = 'contentDetails').execute()
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

playlist_id = getPlaylistID()

#TODO: Eventually modify both scripts so user can select how many thumbnails they want
#TODO: Add exceptions and see if you can solve the problem when the thumbnail is autogenerated
# Makes a request to the youtube api to return the ytimgs link of a maxres version of the thumbnail
# NOTE: Does not work if the video has no thumbnail set by the user! Script will fail if the video
# has an autogenerated thumbnail by youtube.

def getLastVideoThumb():
    response = youtube.playlistItems().list(playlistId =playlist_id, part = 'snippet',maxResults=1).execute()
    return response['items'][0]['snippet']['thumbnails']['maxres']['url']


