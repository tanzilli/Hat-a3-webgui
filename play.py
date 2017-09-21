#!/bin/python

import json
import time
import os

images_list="slides.json"


while True:
	with open(images_list) as json_data:
		d = json.load(json_data)
	
		for images_field in d:
			print(images_field["type"])
			print(images_field["file"])
			print("--------------------")
			
			command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % images_field["file"]
			print "  " , command
			print("--------------------")
			os.system(command)

	
	print "Wait..."
	time.sleep(1)
