# HAT-A3 web user interface

Web front-end to manage an RGB panel with the Raspberry Pi and an [Acme Systems 
HAT-A3 RGB board](http://www.tanzolab.it/HAT-A3).

Based on the  https://github.com/hzeller/rpi-rgb-led-matrix project

![Screenshot](/images/screenshot.jpg)

## Files description

* __index.php__ Main web page
* __main.js__ Javascript local functions
* __slides.json__ List of image to display on the RGB led panel
<<<<<<< HEAD
* __upload.php__ Script richiamato in ajax da __main.js__ per fare l'upload delle gif via web
* __play.php__ This script writes on /run/ledplay to talk with python/play.py
* __python/play.py__ Daemon in Python that reads the slides.json contents and launch led-image-viewer
* __slides__ Binary images to show
* __play.service__ systemd servi definition
=======
* __upload.php__ Script for images upload
* __play.php__ This script is used just to write in __/run/ledplay__ the text "running" used by the python daemon __play.py__ to start sending images to the RGB panel
* __slides__ Inside this directory are saved the binary images to show on the RGB panel
* __python__ This directory contains the code that generates the images on the RGB panel
	* __play.py__ Daemon in Python that reads the slides.json contents and launch led-image-viewer
	* __ptemp.py__ Temperature widget
	* __ptime.py__ Time widget
* __video__ Some scripts to convert video file to gif images using ffmpeg
>>>>>>> 87868917bfd46ffa3cb5ce2bbb33bba3936c638c

## Installation

Install __rpi-rgb-led-matrix__ software on your Raspberry Pi following this web site:

* https://github.com/hzeller/rpi-rgb-led-matrix

Clone the repository then config Apache2 to use it as DocumentRoot

	git clone https://github.com/tanzilli/Hat-a3-webgui.git

Configure __python/play.py__ as a service under systemd

### Debian packages required

This is a web application written in PHP so you have to install Apache2 and PHP: 

	sudo apt-get install apache2 php

This package is required by the widget written in python to create dinamically the images using [Pillow](https://python-pillow.org/)

	sudo apt-get install python-pillow

This package is required by the widget python/ptemp.py to get info from [OpenWeatherMap](https://openweathermap.org/)

	sudo apt-get install python-requests
	
This package is required just if you want to generate gif image from video using this script [video/m2g_2.sh](Hat-a3-webgui/video/m2g_2.sh)

	sudo apt-get install ffmpeg	
	
## Systemd service

Save the [play.service](play.service) systemd definition in __/lib/systemd/system__ then
enable the service:

	sudo systemctl enable play.service	

## Links
	
* http://www.tanzolab.it/HAT-A3
* http://www.tanzolab.it/raspberry_ledpanel

Sergio Tanzilli &copy; 2017
