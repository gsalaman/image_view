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
icon_size = 10

screen = Image.new("RGBA", (total_columns,total_rows))
screen_draw = ImageDraw.Draw(screen)

print (screen.getbands())

icon_image = Image.open("Hint.png")
icon_image = icon_image.convert("RGBA")
icon_image = icon_image.resize((icon_size,icon_size))

# now that we have our image, we want to make a transparency mask.
# start by looking at each pixel, and if it's black, make the mask
# transparent (also black).  Otherwise, make it fully opaque (white)
mask = Image.new("L", (icon_size,icon_size))
icon_data = icon_image.getdata()
mask_data = []
for item in icon_data:
  if item[0] == 0 and item[1] == 0 and item[2] == 0:
    mask_data.append(0)
    print "transparent"
  else:
    mask_data.append(255)
    print "opaque"
mask.putdata(mask_data)

bg_color = (0,0,100)

screen_draw.rectangle((0,0,total_columns,total_rows), fill = bg_color)

screen.paste(icon_image,(10,10),mask)
#screen.paste(icon_image,(10,10))

screen = screen.convert("RGB")

matrix.SetImage(screen, 0, 0)

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

