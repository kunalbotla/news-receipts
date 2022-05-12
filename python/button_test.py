import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 3 to be an input pin and set initial value to be pulled low (off)

# Set default door closed status
old_door_status = GPIO.input(3)
open_status = False
old_open_status = False

while True:

    # Check if door is open
    door_status = GPIO.input(3)

    # Check if the status has changed
    if door_status != old_door_status:
        # Saved the changed state
        old_door_status = door_status


        if door_status == GPIO.HIGH:
            print("Open; placeholder for printing")
            open_status = True
            old_open_status = False
        if door_status == GPIO.LOW:
            print("Closed; placeholder for not printing; print the glass message")
            open_status = False
            old_open_status = True