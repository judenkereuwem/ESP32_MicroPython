from machine import SoftI2C, Pin
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("  Welcome  to", 0, 16)
oled.text("  Placidlearn", 0, 30)
oled.show()