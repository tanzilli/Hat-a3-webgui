#!/usr/bin/python

import json
import time
import os
import stat

path, filename = os.path.split(os.path.realpath(__file__))

images_list= "../slides.json"
slides_dir = "../slides"
my_runfile = "/run/ledplay"

if not os.path.exists(my_runfile):
	os.mknod(my_runfile)	
	os.chmod(my_runfile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

f = open(my_runfile,"w")
f.write("go")
f.close()

command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % (path + "/" + slides_dir + "/" + "logo.png")
os.system(command)

while True:
	if os.path.exists(my_runfile) and os.path.getsize(my_runfile) > 0:

		with open(path + "/" + images_list) as json_data:
			d = json.load(json_data)
	
			for images_field in d:
				if os.path.getsize(my_runfile) == 0:
					break

				print(images_field["file"])

				if images_field["type"]=="ptime":
					command=path + "/" + "ptime.py"
					os.system(command)
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % ("/tmp/ptime.png")
					os.system(command)
					continue

				if images_field["type"]=="pweather":
					command=path + "/" + "pweather.py"
					os.system(command)
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % ("/tmp/pweather.png")
					os.system(command)
					continue

				if images_field["type"]=="image":
					command="/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer -l1 --led-chain=6 --led-parallel=3 -R270 -w 5 %s" % (path + "/" + slides_dir + "/" + images_field["file"])
					os.system(command)
				
	print "Wait..."
	time.sleep(1)


