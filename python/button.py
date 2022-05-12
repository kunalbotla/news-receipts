from distutils.util import execute
import RPi.GPIO as GPIO
from news_print import print_static_page # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
print(GPIO.getmode(GPIO.BOARD))
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# Set default door closed status
old_door_status = GPIO.input(10)
open_status = False
old_open_status = False

import news_print

while True:

    # Check if door is open
    door_status = GPIO.input(10)

    # Check if the status has changed
    if door_status != old_door_status:
        # Saved the changed state
        old_door_status = door_status


        if door_status == GPIO.HIGH:
            print("Open; placeholder for printing")
            execute(news_print.execute)
            open_status = True
            old_open_status = False
        if door_status == GPIO.LOW:
            print("Closed; placeholder for not printing; print the glass message")
            news_print.print_static_page()
            open_status = False
            old_open_status = True