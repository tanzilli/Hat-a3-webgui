#!/usr/bin/python

import sys
import os
from PIL import Image, ImageDraw, ImageFont
import StringIO
import time

from datetime import datetime

mesi=["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]

#Panel size
size = 96, 192

#Load a TTF font
font1 = ImageFont.truetype("Ubuntu-B.ttf", 18)
font2 = ImageFont.truetype("Ubuntu-B.ttf", 34)
font3 = ImageFont.truetype("Ubuntu-B.ttf", 16)

#im=Image.new("RGB",size,"black")
im=Image.open("ptime.png")

#Create a draw object to draw primitives on the new image 
draw = ImageDraw.Draw(im)
draw.fontmode="0" #No antialias

time_string=datetime.now().strftime('%H:%M')
date_string=datetime.now().strftime('%d/%m/%Y')

#Draw counter text on the panel 
y=50
draw.text((0,0+y), "Sono le ore", (250,0,250), font=font1)
draw.text((6,16+y), time_string, (0,255,0), font=font2)
draw.text((34,50+y), "del", (255,0,255), font=font1)
draw.text((0,70+y), date_string, (255,255,0), font=font1)
del draw

#Generate a JPEG image (a format very similar to byte array RGB we need)
output = StringIO.StringIO()
im.save("/tmp/ptime.png", format='PNG')
del im
	
