#!/bin/sh

palette="palette.png"
filters="fps=30,scale=128:-1:flags=lanczos"
ffmpeg -v warning -i $1 -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y ${1%%.*}.gif

#echo $1
#echo ${1%%.*}.gif