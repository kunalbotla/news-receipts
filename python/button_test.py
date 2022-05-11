import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

open_status = False

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Run commands")
        open_status = True
    if GPIO.input(0) == GPIO.LOW:
        print("Stop commands")
        open_status = False
