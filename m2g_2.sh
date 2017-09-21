#!/bin/sh

if [ $# -ne 2 ]
  then
    echo "Sintax error:"
    echo "  ./movie2gif.sh inputfile.m4v outputfile.gif"
    exit 1
fi


palette="palette.png"
filters="fps=30,scale=128:-1:flags=lanczos"
ffmpeg -v warning -i $1 -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $2
