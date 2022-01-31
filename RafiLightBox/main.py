# Simple code for Rafi LightBox
# Wemos 8266
# Neopixel string on D2
# Button on D1

# Bring in our libraries
import neopixel
from machine import Pin
from time import sleep

# Define neopixel pins and amount
pixel_pin=4 #D2
pixel_num=10

# Our toggle button is on pin 5 - D1
button = Pin(5, Pin.IN, Pin.PULL_UP)

# Switch off the internal LED
int_led=Pin(2,Pin.OUT)
int_led(1)

# Define our string
np = neopixel.NeoPixel(machine.Pin(pixel_pin), pixel_num)

# Define colour list
colours=[(0,0,0),(255, 0, 255),(255,255,0),(0,255,0),(0,0,255),(255,0,0)]

# Function to set neopixel string to 1 colour out of colours list defined by rot
def np_on(np,num_pixels,rot,colours):
    for pixel in range(num_pixels):
        np[pixel]=colours[rot]
    np.write()

# Start from colours=0
rgb_rot=0

# And make sure they are all off
np_on(np,pixel_num,rgb_rot,colours)

# Infinite loop, watching for a button press
while True:
    if not button.value():
        # Pressed, now wait until it's let go (debounce)
        while not button.value():
            pass

        # Increment rgb_rot up to 6, then 1
        rgb_rot=rgb_rot+1
        if rgb_rot==len(colours):
            rgb_rot=0

        # Call the np_on function with current value of rgb_rot
        np_on(np,pixel_num,rgb_rot,colours)
