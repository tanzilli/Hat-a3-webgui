#!/bin/bash
while :
do
	python ora.py
	sudo rpi-rgb-led-matrix/utils/led-image-viewer --led-chain=6 --led-parallel=3 -R270 -w 5 -l 1 /tmp/ora.png
	sudo rpi-rgb-led-matrix/utils/led-image-viewer --led-chain=6 --led-parallel=3 -R270 -w 5 -l 1 orari.png
done
