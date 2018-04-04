#!/usr/bin/python

import json
import time
import os
import stat

path, filename = os.path.split(os.path.realpath(__file__))

images_list= "../slides.json"
slides_dir = "../slides"
my_runfile = "/run/ledplay"

#Numero di pannelli in linea 
led_chain=2
led_parallel=1
rotate=270

if not os.path.exists(my_runfile):
	os.mknod(my_runfile)	
	os.chmod(my_runfile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

f = open(my_runfile,"w")
f.write("play")
f.close()

command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=%d --led-parallel=%d --led-pixel-mapper='Rotate:%d' -w 5 %s" % (led_chain, led_parallel, rotate, path + "/" + slides_dir + "/" + "logo.png")
os.system(command)


def checkPlayFile():
	if not os.path.exists(my_runfile):
		return False

	f=open(my_runfile,"r")
	content=f.read();
	print content
	if "play" in content:
		return True
	return False

while True:
	if checkPlayFile():
		with open(path + "/" + images_list) as json_data:
			d = json.load(json_data)
	
			for images_field in d:
				print(images_field["file"])

				if images_field["type"]=="ptime":
					command=path + "/" + "ptime.py"
					os.system(command)
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=%d --led-parallel=%d --led-pixel-mapper='Rotate:%d' -w 5 %s" % (led_chain, led_parallel, rotate, "/tmp/ptime.png")
					os.system(command)
					continue

				if images_field["type"]=="pweather":
					command=path + "/" + "pweather.py"
					os.system(command)
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=%d --led-parallel=%d --led-pixel-mapper='Rotate:%d' -w 5 %s" % (led_chain, led_parallel, rotate, "/tmp/pweather.png")
					os.system(command)
					continue

				if images_field["type"]=="image":
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=%d --led-parallel=%d --led-pixel-mapper='Rotate:%d' -w 5 %s" % (led_chain, led_parallel, rotate, path + "/" + slides_dir + "/" + images_field["file"])
					os.system(command)
				
	print "Wait..."
	time.sleep(1)


