"""
Licence
    WDGAF

Authors
    Gabriel Secula
    Michael Belousov

Reference
    https://github.com/Rapptz/discord.py
    http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html        
Installs(for when Gabe inevitably switches machines again)
    pip3 install -U discord.py
    pip3 install Numpy
    pip3 install opencv-contrib-python
    pip3 install urllib3
"""

import discord
import asyncio
from configparser import SafeConfigParser
from discord.ext import commands
from discord.ext.commands import Bot
from urllib.request import urlretrieve
import numpy as np
import cv2
from PIL import Image

bot = Bot(description='Hats and stuff',
        command_prefix='+')
"""bot API wrapper"""
parser = SafeConfigParser()
parser.read('config.ini')
token = parser.get('onlySection','token')
"""discord bot API token"""


@bot.event
async def on_ready():
    print('Logged in as {}, id = {}'.format(
        bot.user.name, 
        bot.user.id))

@bot.event
async def on_message(message):
    if message[:1] == command_prefix:
        print('they did the thing') #do something for real
        if message[1:6] == ('hatme'):
            print('you speak in strange tongues lad')

@bot.command()
async def hat(victim:str, hat:str='', allfaces:str='false'):
    """supply a user with a hat"""
    # define a haar-cascader from a pre-trained data
    facefinder = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # load the victim image, to which we will add a hat 
    victim_img = ''
    victim, _ = urlretrieve(victimimg)
    hat_img = message
    hat, _ = urlretrieve(hat_img)
    img = cv2.imread(victim)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facefinder.detectMultiScale(gray, 1.3, 5)
    if not allfaces:
        faces = [max(faces,key=lambda x,y,w,h: w*h)]
    for x,y,w,h in faces:
        pass
    await bot.say('hello!')

async def close(bot):
    await super().close()
    await bot.session.close()

bot.run(token)


bot.close()


