# aud_listen

# import RPi.GPIO as GPIO

def aud_listen():
    """
    listen if there is any noise
    plan: noise recognition sensor with GPIO-Input
    """
    print("press any key - instead of real noise detection later")
    input()
    return True

if __name__ == '__main__':
    noise = aud_listen()
    print(noise)
    

##GPIO.setmode(GPIO.BCM)
##
##GPIO.setup(23, GPIO.OUT)
##GPIO.setup(25, GPIO.OUT)
##
### GPIO.setup(24, GPIO.IN)
##
##
##for i in range(5):
##    GPIO.output(23, GPIO.HIGH)
##    time.sleep(1.0)
##    GPIO.output(25, GPIO.HIGH)
##    time.sleep(1.0)
##    GPIO.output(23, GPIO.LOW)
##    time.sleep(1.0)
##    GPIO.output(25, GPIO.LOW)
##    time.sleep(1.0)
##
##
### Endlosschleife
### while True:
##    # if GPIO.input(24) == 0:
##        # Ausschalten
##        # PIO.output(23, GPIO.LOW)
##     # else:
##        # Einschalten
##        # GPIO.output(23, GPIO.HIGH)
##
### clean up all channel settings (?? no effect seen)
##GPIO.cleanup()


