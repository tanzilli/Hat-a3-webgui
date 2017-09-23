#!/bin/python

import json
import time
import os
import stat

images_list="/var/www/html/slides.json"
my_runfile = "/run/ledplay"
slides_path = "/var/www/html/slides/"

if not os.path.exists(my_runfile):
	os.mknod(my_runfile)	
	os.chmod(my_runfile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

while True:
	if os.path.exists(my_runfile) and os.path.getsize(my_runfile) > 0:

		with open(images_list) as json_data:
			d = json.load(json_data)
	
			for images_field in d:
				print(images_field["type"])
				print(images_field["file"])
				print("--------------------")
			
				command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % (slides_path + images_field["file"])
				print "  " , command
				print("--------------------")
				os.system(command)
				
				if os.path.getsize(my_runfile) == 0:
					break

	
	print "Wait..."
	time.sleep(1)


