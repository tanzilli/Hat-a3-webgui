#!/bin/bash


# In loop infinito legge la lista delle gif da mandare
# sul pannello RGB 

# Lista immagini su singola riga separate da spazi
# "SLIDE_LIST='pippo.gif sabato_aperti.git'"
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
			#sudo $RGB_UTILS_PATH/led-image-viewer -l1 --led-chain=4 $SLIDE_LIST
		fi
	else
		echo File $IMAGE_LIST non trovato. Aspetto $DELAY secondi
		sleep $DELAY
	fi
done
