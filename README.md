# HAT-A3 web user interface

Web front-end to manage an RGB panel with the Raspberry Pi and an [Acme Systems 
HAT-A3 RGB board](http://www.tanzolab.it/HAT-A3).

Based on the  https://github.com/hzeller/rpi-rgb-led-matrix project

## Files description

* __index.php__ Main web page
* __main.js__ Javascript local functions
* __slides.json__ List of images to display on the RGB led panel
* __upload.php__ Script called by __main.js__ to upload images and video from the web interface
* __play.php__ Script used by the web interface to write on /run/ledplay. This file is created bt play.py and is used to play or not images on the rgb led panel
* __python/play.py__ Daemon in Python that reads the slides.json contents and launch led-image-viewer
* __slides__ Binary images or videos to show
* __play.service__ systemd service definition
* __upload.php__ Script for images upload
* __play.php__ This script is used just to write in __/run/ledplay__ the text "running" used by the python daemon __play.py__ to start sending images to the RGB panel
* __slides__ Inside this directory are saved the binary images to show on the RGB panel
* __python__ This directory contains the code that generates the images on the RGB panel
	* __play.py__ Daemon in Python that reads the slides.json contents and launch led-image-viewer
	* __ptemp.py__ Temperature widget
	* __ptime.py__ Time widget

## Installation

### Debian packages required

This is a web application written in PHP so you have to install Apache2 and PHP: 

	sudo update
	sudo apt-get install apache2 php

Install git to clone the source repositories:

	sudo apt-get install git

This package is required by the widget written in python to create dinamically the images using [Pillow](https://python-pillow.org/)

	sudo apt-get install python-pillow

This package is required by the widget python/ptemp.py to get info from [OpenWeatherMap](https://openweathermap.org/)

	sudo apt-get install python-requests

Clone the [rpi-rgb-led-matrix repository](https://github.com/hzeller/rpi-rgb-led-matrix) 
on your Raspberry by typing:

	cd
	git clone https://github.com/hzeller/rpi-rgb-led-matrix 

then compile ed-image-viewer and video-viewer program used to send images and video
to the RGB led panel:

	cd rpi-rgb-led-matrix/utils
	sudo apt-get update
	sudo apt-get install libgraphicsmagick++-dev libwebp-dev -y
	make led-image-viewer
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
	make video-viewer	

Replace the default html directory of Apache 2 with the clone of 
the [Web GUI interface repository](https://github.com/tanzilli/Hat-a3-webgui):

	sudo rm -rf /var/www/html
	sudo git clone https://github.com/tanzilli/Hat-a3-webgui.git /var/www/html

and set the files ownership to www-data user:

	sudo chown -R www-data:www-data /var/www/html

### play.py as Systemd service

Configure __/var/www/html/python/play.py__ as a service under systemd

Save the [play.service](play.service) systemd definition in __/lib/systemd/system__ then
enable the service:

	cd /var/www/html
	sudo cp play.service /lib/systemd/system
	udo systemctl daemon-reload
	sudo systemctl enable play.service	
	sudo systemctl start play.service	

## Links
	
* http://www.tanzolab.it/HAT-A3
* http://www.tanzolab.it/raspberry_ledpanel
* https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/utils

Sergio Tanzilli &copy; 2018
