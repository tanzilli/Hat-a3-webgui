# HAT-A3 web user interface

Web front-end to manage an RGB panel with the Raspberry Pi and an [Acme Systems 
HAT-A3 RGB board](http://www.tanzolab.it/HAT-A3).

Based on the  https://github.com/hzeller/rpi-rgb-led-matrix project

![Screenshot](/images/screenshot.jpg)

## Files description

* __index.php__ Home page
* __main.js__ Javascript local functions
* __slides.json__ List of image to display on the RGB led panel
* __upload.php__ Script richiamato in ajax da __main.js__ per fare l'upload delle gif via web
* __play.php__ This script writes on /run/ledplay to talk with python/play.py
* __python/play.py__ Daemon in Python that reads the slides.json contents and launch led-image-viewer
* __slides__ Binary images to show

Installation

	git clone https://github.com/tanzilli/Hat-a3-webgui.git

How to install the rpi-rgb-led-matrix software on your Raspberry Pi

* https://github.com/hzeller/rpi-rgb-led-matrix

Debian packages required 

	sudo apt-get install python-pillow
	sudo apt-get install python-requests
	sudo apt-get install ffmpeg	

## Links
	
* http://www.tanzolab.it/raspberry_ledpanel

Sergio Tanzilli &copy; 2017 - [http://www.tanzolab.it/HAT-A3](http://www.tanzolab.it/HAT-A3)
