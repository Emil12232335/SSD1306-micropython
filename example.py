# Import libs
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Set the width and the hight of the display
WIDTH = 128
HEIGHT = 64

# Set the I2C bus and define it as "oled"
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Manage what is seen on the display
oled.fill(0) # Clear the
oled.text("Hello World", 5, 5) # Print out "Hello World" on x = 5 and y = 5
oled.show() # Show everything on the screen. Always needed at the end
