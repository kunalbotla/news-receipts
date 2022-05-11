# nytimes

from asyncore import write
import keys
active_NYT_KEY = keys.NYT_KEY

import requests
import json
from random import randrange

# printer

import board
import busio

import adafruit_thermal_printer

# Pick which version thermal printer class to use depending on the version of
# your printer.  Hold the button on the printer as it's powered on and it will
# print a test page that displays the firmware version, like 2.64, 2.68, etc.
# Use this version in the get_printer_class function below.
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

# Define RX and TX pins for the board's serial port connected to the printer.
# Only the TX pin needs to be configued, and note to take care NOT to connect
# the RX pin if your board doesn't support 5V inputs.  If RX is left unconnected
# the only loss in functionality is checking if the printer has paper--all other
# functions of the printer will work.
RX = board.RX
TX = board.TX

# Create a serial connection for the printer.  You must use the same baud rate
# as your printer is configured (print a test page by holding the button
# during power-up and it will show the baud rate).  Most printers use 19200.
# rpi # uart = busio.UART(TX, RX, baudrate=19200)

# For a computer, use the pyserial library for uart access.
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)

# Create the printer instance.
printer = ThermalPrinter(uart, auto_warm_up=False)

# Initialize the printer.  Note this will take a few seconds for the printer
# to warm up and be ready to accept commands (hence calling it explicitly vs.
# automatically in the initializer with the default auto_warm_up=True).
printer.warm_up()

# Check if the printer has paper.  This only works if the RX line is connected
# on your board (but BE CAREFUL as mentioned above this RX line is 5V!)
# if printer.has_paper():
#     print("Printer has paper!")
# else:
#     print("Printer might be out of paper, or RX is disconnected!")

# nytimes

printer.bold = True
    printer.size = adafruit_thermal_printer.SIZE_LARGE
    

    printer.print("The New York Times")
    printer.bold = False
    printer.size = adafruit_thermal_printer.SIZE_SMALL

    printer.print("Copyright (c) 2022 The New York Times Company. All Rights Reserved.")
    

def execute():
#   print(active_NYT_KEY)
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key="+active_NYT_KEY
#   print(requestUrl)
    requestHeaders = {
      "Accept": "application/json"
  }

    nyt_out = requests.get(requestUrl, headers=requestHeaders)
    data = json.loads(nyt_out.text)

    pick_rand_article(data)

def pick_rand_article(data):
    rand_article = data['results'][randrange(len(data['results']))]
    print(rand_article['title'])
    print(rand_article['abstract'])
    print(rand_article['short_url'])
    print(rand_article['published_date'])


    printer.print(rand_article['title'])
    printer.feed(1)

    printer.print(rand_article['abstract'])
    printer.feed(1)

    printer.print(rand_article['short_url'])
    printer.feed(1)

    printer.print(rand_article['published_date'])
    printer.feed(1)

    printer.feed(2)

if __name__ == "__main__":
    execute()