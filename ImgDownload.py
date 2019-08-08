#!/usr/bin/env python
import FindVideo as fv
import urllib.request

"""

Script to download and save the thumbnail of a video using the link provided
by the FindVideo script
"""


url = fv.getLastVideoThumb()
file_name = input("Save as: ")
output_path = input("Type path to directory where you wish to save the image: ")

"""

Method that retrieves the image found at a given url and saves it to the specified path

Parameters:
-----------
url : str 
    The url to the picture that is to be downloaded
    Provided by the getLastVideoThumb() method in FindVideo
path : str
    Location on the computer where the user wishes to save
    the image
name : str
    The name that the user wants to give to the saved image
"""

def downloadImg(url, path, name):
   # Build the name of the path and location to where
   # the image will be saved
   save_path = path + name + '.jpg'
   
   # Download image at url to location save_path
   urllib.request.urlretrieve(url, save_path)

downloadImg(url, output_path, file_name)
