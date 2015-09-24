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
    xd = 3
    yd = 3
    while True:

	for i in range(1,10):
		x = random.randint(0,274)
		y = random.randint(0,176)
		onoff = random.randint(0,1)
    		#draw.text((x,y),'o',fill=BLACK)
    		draw.point((x,y),fill=BLACK)

    	# display image on the panel
    	epd.display(image)
    	epd.partial_update()


# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))
    main(sys.argv[1:])
