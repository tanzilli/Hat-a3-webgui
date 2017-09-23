# HAT-A3 web user interface

* __index.php__ Home page
* __main.js__ Javascript local functions
* __play.sh__ Script da lanciare  in __rc.local__ legge il file __slides.env__ e invia le gif su pannello a led
* __slides.env__ File testo usato da __play_sh__ per la lista delle gif sa visualizzare
* __upload.php__ Script richiamato in ajax da __main.js__ per fare l'upload delle gif via web
* __play.php__ Script richiamato in ajax da __main.js__ per eseguire il play e lo stop delle animazioni su pannello a led

## Debian package to install 

	sudo apt-get install python-pillow
	sudo apt-get install python-requests
	sudo apt-get install ffmpeg	

## Links
	
* http://www.tanzolab.it/raspberry_ledpanel
* https://github.com/hzeller/rpi-rgb-led-matrix

Sergio Tanzilli &copy; 2017 - [http://www.tanzolab.it/HAT-A3](http://www.tanzolab.it/HAT-A3)
