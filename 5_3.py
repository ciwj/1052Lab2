# setup
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
pin = GPIO.PWM(25,200)
pin.start(50)

freq = 200

try:
    if freq < 1000:
        freq += 200
    else:
        freq = 200
    pin.ChangeDutyCycle(freq)
    time.sleep(1)

except KeyboardInterrupt:
    pass

pin.stop()
GPIO.cleanup()