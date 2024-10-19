import machine
import neopixel
import time

pin = machine.Pin(16)
num_pixels = 25
np = neopixel.NeoPixel(pin, num_pixels)

def set_candy_cane_pattern(offset=0):
    for i in range(num_pixels):
        if (i + offset) % 3 == 0:
            np[i] = (255, 0, 0)
        elif (i + offset) % 3 == 1:
            np[i] = (0, 255, 0)
        else:
            np[i] = (0, 0, 255)
    np.write()


offset = 0
while True:
    set_candy_cane_pattern(offset)
    offset += 1
    time.sleep(0.5)
