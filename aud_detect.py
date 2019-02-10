#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                # sound detected, later: grab some seconds
                # send email with sound snippet
                # what do with ongoing sound ? wait here?
                print("Sound Detected!")
        else:
                print("Sound Detected! (else-branch)")
                # send email without sound snippet
                # also here: what do with ongoing noise?
# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

# assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)


# infinite loop
while True:
        time.sleep(1)
