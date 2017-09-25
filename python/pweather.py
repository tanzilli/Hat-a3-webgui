#!/usr/bin/python
# -*- coding: utf-8 -*-

# OpenWeatherMap service provides open weather data for more than 200,000
# cities and any geo location that is available on our website and through API.

#https://github.com/akora/openweathermap-python/blob/master/openWeatherMap.py
#https://home.openweathermap.org/api_keys
#http://api.openweathermap.org/data/2.5/weather?APPID=5a3e61a21bf10f79e69a4a6a9af17a57&q=roma&lang=it&units=metric

import sys
import os
from PIL import Image, ImageDraw, ImageFont
import StringIO
import time
import math
import requests
from datetime import datetime

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

base_url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = '5a3e61a21bf10f79e69a4a6a9af17a57'  
city = "roma"

#Panel size
size = 96, 192

def get_weather(city):
	query = base_url + '?q=%s&units=metric&lang=it&APPID=%s' % (city, api_key)
	try:
		response = requests.get(query)
		# print("[%s] %s" % (response.status_code, response.url))
		if response.status_code != 200:
	  		response = 'N/A'
	  		return response
		else:
	  		weather_data = response.json()
	  		return weather_data
	except requests.exceptions.RequestException as error:
		print error
		return 'N/A'

#Load a TTF font
font = ImageFont.truetype(path + "/" + "Ubuntu-B.ttf", 13)

#im=Image.new("RGB",size,"black")
im=Image.open(path + "/" + "pweather.png")

#Create a draw object to draw primitives on the new image 
draw = ImageDraw.Draw(im)
draw.fontmode="0" #No antialias

wdata = get_weather(city)

# City
y=4
draw.text((0,4), city.upper(), (0,250,250), font=font)

#Weather descrition
y=100
wdescription=wdata['weather'][0]['description'].upper()
draw.text((0,y), wdescription, (0,0,250), font=font)

y=y+15
wtemp="Temp: " + ("%.1f" % wdata['main']['temp']) + u'°C '
print wdata['main']['temp']
draw.text((0,y), wtemp, (0,0,250), font=font)

y=y+15
whumidity="Um %: " + str(math.ceil(wdata['main']['humidity']))
draw.text((0,y), whumidity, (0,0,250), font=font)

y=y+15
wwind_speed="Vento: " + str(math.ceil(wdata['wind']['speed']))
draw.text((0,y), wwind_speed, (0,0,250), font=font)

del draw

y=10
#Get the weather icon
wicon_name=wdata['weather'][0]['icon'] + ".png"
im_wicon=Image.open(path + "/wicons/" + wicon_name)
im_wicon_zoom=im_wicon.resize((96,96), Image.ANTIALIAS)
im.paste(im_wicon_zoom,(0,y),im_wicon_zoom)
im.save("/tmp/pweather.png", format='PNG')
del im
	
#Direct test	
command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 10 %s" % ("/tmp/pweather.png")
os.system(command)
