#!/bin/bash

# In loop infinito legge la lista delle gif da mandare
# sul pannello RGB 

# File generato in php per comunicare la nuova lista 
# di immagini da riprodurre a led-image-viewer
# Il file deve contenere una stringa del tipo:
# SLIDE_LIST='img1.gif img2.git img3.gif'

IMAGE_LIST="/dev/shm/slides.env"

# Secondi di ritardo tra una verifica e l'altra
DELAY=5

# Path del programma led-image-viewer
RGB_UTILS_PATH="/home/pi/rpi-rgb-led-matrix/utils/"

while true
do
	export SLIDE_LIST="NULL"
	
	if [ -f $IMAGE_LIST ] ; then
		source $IMAGE_LIST
		if [ "$SLIDE_LIST" == "NULL"  ] ; then
			echo Nessuna immagine. Aspetto $DELAY secondi
			sleep $DELAY
		else
			echo $SLIDE_LIST
			sudo $RGB_UTILS_PATH/led-image-viewer -l1 --led-chain=4 $SLIDE_LIST
		fi
	else
		echo File $IMAGE_LIST non trovato. Aspetto $DELAY secondi
		sleep $DELAY
	fi
done
