import deskled
import time



while True:
        deskled.pwm()
        time.sleep(2)
        deskled.flasher(5,3) #how many, pause in seconds

