# setup
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
pin = GPIO.PWM(25,50)
pin.start(0)

# reset
pin.ChangeDutyCycle(0)
cycle = 0

# cycle between dutycycles

i = 1

try:
    while i == 1:
        pin.ChangeDutyCycle(cycle)
        if cycle < 100:
            cycle += 20
        else:
            cycle = 0
        time.sleep(1)

# exit
except KeyboardInterrupt:
    pass

pin.stop()
GPIO.cleanup()
