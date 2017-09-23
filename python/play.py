#!/usr/bin/python

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
				if os.path.getsize(my_runfile) == 0:
					break

				print(images_field["file"])

				if images_field["type"]=="ptime":
					command="/var/www/html/python/ptime.py"
					os.system(command)
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % ("/tmp/ptime.png")
					os.system(command)
					continue

				if images_field["type"]=="ptemp":
					command="/var/www/html/python/ptemp.py"
					os.system(command)
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % ("/tmp/ptemp.png")
					os.system(command)
					continue

				if images_field["type"]=="image":
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % (slides_path + images_field["file"])
					os.system(command)
				

	
	print "Wait..."
	time.sleep(1)


