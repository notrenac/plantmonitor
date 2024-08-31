import board
import neopixel_spi

pixels = neopixel_spi.NeoPixel_SPI(board.SPI(), 15)
pixels.fill(0x500000)