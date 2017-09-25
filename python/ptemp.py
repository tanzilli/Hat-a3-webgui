#!/usr/bin/python

# OpenWeatherMap service provides open weather data for more than 200,000
# cities and any geo location that is available on our website and through API.

#https://github.com/akora/openweathermap-python/blob/master/openWeatherMap.py
#https://home.openweathermap.org/api_keys

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
cities = ['Carsoli','Milano','Trento','Bologna','Roma','Napoli','Palermo']
#Panel size
size = 96, 192

def get_temperature(city):
	query = base_url + '?q=%s&units=metric&APPID=%s' % (city, api_key)
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
font = ImageFont.truetype(path + "/" + "Ubuntu-B.ttf", 16)

#im=Image.new("RGB",size,"black")
im=Image.open(path + "/" + "ptemp.png")

#Create a draw object to draw primitives on the new image 
draw = ImageDraw.Draw(im)
draw.fontmode="0" #No antialias

y=0
for city in cities:
	location = get_temperature(city)
	text=location['name'] + ' ' + str(math.ceil(location['main']['temp'])) + ' C '
	draw.text((0,0+y), text, (250,0,250), font=font)
	y=y+16
del draw

#Generate a JPEG image (a format very similar to byte array RGB we need)
im.save("/tmp/ptemp.png", format='PNG')
del im
	

