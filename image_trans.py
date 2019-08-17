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
#options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular' 

#options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

###################################
# Main loop 
###################################
screen = Image.new("RGBA", (total_columns,total_rows))
screen_draw = ImageDraw.Draw(screen)

print (screen.getbands())

mask = Image.new("L", (10,10),64)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rectangle((0,0,10,10),0)
mask_draw.rectangle((2,2,7,7),255)

icon_image = Image.new("RGBA", (10,10))
icon_draw = ImageDraw.Draw(icon_image)
icon_draw.rectangle((2,2,7,7),(255,0,0))

bg_color = (0,0,100)

screen_draw.rectangle((0,0,total_columns,total_rows), fill = bg_color)

screen.paste(icon_image,(10,10),mask)

screen = screen.convert("RGB")

matrix.SetImage(screen, 0, 0)

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

