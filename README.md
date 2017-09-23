# HAT-A3 web user interface

![Screenshot](/images/screenshot.jpg)

* __index.php__ Home page
* __main.js__ Javascript local functions
* __slides.json__ List of image to display on the RGB led panel
* __upload.php__ Script richiamato in ajax da __main.js__ per fare l'upload delle gif via web
* __play.php__ This script writes on /run/ledplay to talk with python/play.py
* __python/play.py__ Daemon in Python that reads the slides.json contents and launch led-image-viewer
* __slides__ Binary images to show

## Debian package to install 

	sudo apt-get install python-pillow
	sudo apt-get install python-requests
	sudo apt-get install ffmpeg	

## Links
	
* http://www.tanzolab.it/raspberry_ledpanel
* https://github.com/hzeller/rpi-rgb-led-matrix

Sergio Tanzilli &copy; 2017 - [http://www.tanzolab.it/HAT-A3](http://www.tanzolab.it/HAT-A3)
