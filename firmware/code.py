import time
import board
import busio
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from terminalio import FONT

# Release any existing display
displayio.release_displays()

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Wait until I2C is ready
while not i2c.try_lock():
    pass
i2c.unlock()

# OLED setup
WIDTH = 128
HEIGHT = 32
RESET_PIN = None  # Change if your display reset pin is connected

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C, reset=RESET_PIN)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Create a display group
group = displayio.Group()

# Background
bg = displayio.TileGrid(
    displayio.Bitmap(WIDTH, HEIGHT, 1),
    pixel_shader=displayio.Palette(1)
)
bg.pixel_shader[0] = 0x000000
group.append(bg)

# Text
text = label.Label(
    FONT,
    text="SSD1306 OK",
    color=0xFFFFFF,
    x=20,
    y=10
)
group.append(text)

text2 = label.Label(
    FONT,
    text="XIAO RP2040",
    color=0xFFFFFF,
    x=18,
    y=24
)
group.append(text2)

display.show(group)

# Simple test loop: toggle a small status line
on = True
while True:
    text.text = "SSD1306 OK" if on else "SSD1306 TEST"
    text2.text = "XIAO RP2040"
    on = not on
    time.sleep(1)