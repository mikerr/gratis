import sys
from PIL import Image
from PIL import ImageDraw
from EPD import EPD
import commands

WHITE = 1
BLACK = 0

epd = EPD()
epd.clear()

# initially set all white background
image = Image.new('1', epd.size, WHITE)

# prepare for drawing
draw = ImageDraw.Draw(image)

# show current hostname & ip address 

output = commands.getoutput('hostname -I');
draw.text((40, 0), output, fill=BLACK)
output = commands.getoutput('hostname');
draw.text((120, 0), output, fill=BLACK)

# more info

output = "mike redrobe ; thank you fro your recent order";
draw.text((0, 40), output, fill=BLACK)

# date & time at bottom of screen

output = commands.getoutput('date');
draw.text((40, 160), output, fill=BLACK)

epd.display(image)
epd.update()

