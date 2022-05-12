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
    rand_article = {'section': 'opinion', 'subsection': '', 'title': 'The Power of Lies in an Age of Political Fiction', 'abstract': 'To the fabulist go the spoils?', 'url': 'https://www.nytimes.com/2022/05/12/opinion/marcos-philippines-putin-trump.html', 'uri': 'nyt://article/cb5d3d1a-19e8-5f89-9efa-a5979b8e67d2', 'byline': 'By Frank Bruni', 'item_type': 'Article', 'updated_date': '2022-05-12T12:00:04-04:00', 'created_date': '2022-05-12T12:00:04-04:00', 'published_date': '2022-05-12T12:00:04-04:00', 'material_type_facet': '', 'kicker': '', 'des_facet': ['internal-sub-only-nl'], 'org_facet': [], 'per_facet': ['Marcos, Imelda R', 'Marcos, Ferdinand Jr', 'Marcos, Ferdinand E', 'Putin, Vladimir V', 'Trump, Donald J', 'Herbster, Charles W', 'Pillen, Jim'], 'geo_facet': ['Philippines'], 'multimedia': [{'url': 'https://static01.nyt.com/images/2022/05/12/opinion/12bruni-image/12bruni-image-superJumbo.jpg', 'format': 'Super Jumbo', 'height': 2048, 'width': 2048, 'type': 'image', 'subtype': 'photo', 'caption': '', 'copyright': 'Ben Wiseman'}, {'url': 'https://static01.nyt.com/images/2022/05/12/opinion/12bruni-image/12bruni-image-threeByTwoSmallAt2X.jpg', 'format': 'threeByTwoSmallAt2X', 'height': 400, 'width': 600, 'type': 'image', 'subtype': 'photo', 'caption': '', 'copyright': 'Ben Wiseman'}, {'url': 'https://static01.nyt.com/images/2022/05/12/opinion/12bruni-image/12bruni-image-thumbLarge.jpg', 'format': 'Large Thumbnail', 'height': 150, 'width': 150, 'type': 'image', 'subtype': 'photo', 'caption': '', 'copyright': 'Ben Wiseman'}], 'short_url': 'https://nyti.ms/3wgzd7C'}

    print("The New York Times.")
    print("Copyright (c) 2022 The New York Times Company. All Rights Reserved.")

    print(rand_article['title'])
    print(rand_article['byline'])
    print(rand_article['abstract'])
    print(rand_article['short_url'])
    print(rand_article['published_date'])

    print("Data provided by The New York Times.")

    # Print the page header with logo:

    # import img.nytimes_185 as nytimes_185
    # printer.printBitmap(nytimes_185.width, nytimes_185.height, nytimes_185.data)
    
    # alternate image format, png
    # from PIL import Image
    # printer.printImage(Image.open('img/nytimes_185.png'), True)
    
    # replace with text if it doesn't work
    printer.bold = True
    printer.print("The New York Times")
    printer.bold = False
    printer.feed(1)

    # Print the article:

    printer.print(rand_article['title'])
    printer.print(rand_article['byline'])
    printer.feed(1)

    printer.print(rand_article['abstract'])
    printer.feed(1)

    printer.print(rand_article['short_url'])
    printer.feed(1)

    printer.print(rand_article['published_date'])
    printer.feed(1)

    # Print the page footer with data credits:

    # import img.nytimes_data_150 as nytimes_data_150
    # printer.printBitmap(nytimes_data_150.width, nytimes_data_150.height, nytimes_data_150.data)
    
    # alternate image format, png
    # from PIL import Image
    # printer.printImage(Image.open('img/nytimes_data_150.png'), True)
    
    # replace with text if it doesn't work
    printer.print("Data provided by")
    printer.print("The New York Times.")

    printer.feed(1)

    printer.feed(2)

def print_static_page():

    printer.upside_down = True
    printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER

    
    printer.print("Open to recive news. Data sourced from")

    # Print the page header with logo:

    # import img.nytimes_185 as nytimes_185
    # printer.printBitmap(nytimes_185.width, nytimes_185.height, nytimes_185.data)
    
    # alternate image format, png
    # from PIL import Image
    # printer.printImage(Image.open('img/nytimes_185.png'), True)
    
    # replace with text if it doesn't work
    printer.bold = True
    printer.print("The New York Times")
    printer.bold = False

    printer.print("News Receipts; by Kunal Botla and Will Fosnot.")
    printer.print("Social Robots for the Ages; at NuVu Cambridge, May 2022.")


    printer.upside_down = False
    printer.justify = adafruit_thermal_printer.JUSTIFY_RIGHT

if __name__ == "__main__":
    execute()