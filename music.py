####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# music
# this plays the music for "Lights Out"
# playing music on Python learned from: https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
####################################

####################################
# imports
# necessary to run program
#################################### 

from pygame import *

####################################
# functions
#################################### 

# loops music
def timerFired():
    if not mixer.music.get_busy():
        mixer.music.rewind()
        mixer.music.play()

# plays the music
def runMusic():
    mixer.init()
    mixer.music.load("assets/LightsOutMusic.mp3")
    mixer.music.play()
    timerFired()

runMusic()