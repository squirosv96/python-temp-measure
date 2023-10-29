import board
import adafruit_mlx90614

from ideaboard import IdeaBoard
import time

import socketpool
import ssl
import wifi
import adafruit_requests as requests

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

print("Connecting...")
wifi.radio.connect("BaradDur", "L4#r3d#d3#4b4j0")
print("Connected to Wifi!")

ib = IdeaBoard()

i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)
boton = ib.DigitalIn(board.IO27)

AZUL = (0,0,255)
NEGRO = (0,0,0)

while True:
    if(boton.value == False):
        ib.pixel = AZUL
        print("Ambent Temp: ", mlx.ambient_temperature)
        print("Object Temp: ", mlx.object_temperature)
        response = https.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
        if response.status_code == 200:
            print('Request was successful!')
            print(response.text)  
        else:
            print('Request failed with status code:', response.status_code)
        ib.pixel = NEGRO

