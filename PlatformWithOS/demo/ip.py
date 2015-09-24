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


# stuff

output = commands.getoutput('hostname -I');

# text
draw.text((30, 30), output, fill=BLACK)
epd.display(image)
epd.update()

