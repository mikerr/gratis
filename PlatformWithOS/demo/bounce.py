import sys
from PIL import Image
from PIL import ImageDraw
from EPD import EPD
import random

WHITE = 1
BLACK = 0

def main(argv):
    """main program - draw and display a test image"""

    epd = EPD()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version, g=epd.cog, f=epd.film))

    epd.clear()

    demo(epd)


def demo(epd):
    """simple drawing demo - black drawing on white background"""

    # initially set all white background
    image = Image.new('1', epd.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)

    # bouncing ball 

    x = 0
    y = 0
    xd = 1
    yd = 1
    while True:

	x = x + xd
	y = y + yd
    	#draw.point((x,y),fill=BLACK)
    	draw.text((x,y),'o',fill=BLACK)
    	# display image on the panel
    	if ( x % 5 == 0):
		epd.display(image)
    		epd.partial_update()
    	draw.text((x,y),'o',fill=WHITE)
    	#epd.display(image)
    	#epd.partial_update()

	if ((x <0 ) or (x > 274)):
		 xd = -xd
	if ((y <0 ) or (y > 176)):
		 yd = -yd

    # text
    # draw.text((30, 30), 'hello world', fill=BLACK)



# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))
    main(sys.argv[1:])
