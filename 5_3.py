# setup
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
pin = GPIO.PWM(25,200)
pin.start(50)

freq = 200

i = 1
try:
    while i == 1:
        if freq < 1000:
            freq += 200
        else:
            freq = 200
        pin.ChangeFrequency(freq)
        time.sleep(1)

except KeyboardInterrupt:
    pass

pin.stop()
GPIO.cleanup()
