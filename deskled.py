#!/usr/bin/env python

import time
import os
import feedparser

STEP = 2
DELAY = 0.001
pin = 6
url = "https://www.reddit.com/r/battlestations/.rss"

feed = feedparser.parse( url )


def lightpower(p):
    cmd = "echo " + str(pin) + "=" + str(p) + " > /dev/servoblaster"
    os.system(cmd)


def pwm():
    for j in range(1, 249, STEP):
        cmd = "echo " + str(pin) + "=" + str(j) + " > /dev/servoblaster"
        os.system(cmd)
        time.sleep(DELAY)
    for j in range(249, 1, (STEP*-1)):
        cmd = "echo " + str(pin) + "=" + str(j) + " > /dev/servoblaster"
        os.system(cmd)
        time.sleep(DELAY)

def flasher(flashes, seconds):
        for j in range(1,flashes,1):
            lightpower(250)
            time.sleep(seconds)
            lightpower(0)
            time.sleep(seconds)
