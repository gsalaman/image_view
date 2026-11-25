# Used in main loop
from time import sleep

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 64 
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

###################################
# Main loop 
###################################

# ORIG
image = Image.open("aofc_just_symbol_small.jpg").convert('RGB')
image = image.resize((64,64))
matrix.SetImage(image, 0, 0)

# NEW
#image = Image.open("aoc.png")
#image.thumbnail((matrix.width, matrix.height), Image.Resampling.LANCZOS)
#matrix.SetImage(image.convert('RGB'))

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

