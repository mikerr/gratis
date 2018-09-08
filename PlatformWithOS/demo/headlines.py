
import sys
from PIL import Image
from PIL import ImageDraw
from EPD import EPD

import feedparser

WHITE = 1
BLACK = 0

def main(argv):
    """print the latest headlines from an RSS feed"""

    epd = EPD()
    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version, g=epd.cog, f=epd.film))
    epd.clear()

    demo(epd)

def demo(epd):


    # initially set all white background
    image = Image.new('1', epd.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)


    d = feedparser.parse('http://feeds.skynews.com/feeds/rss/home.xml')

    title = d['feed']['title']
    title = (title[:15])
    updated = d['feed']['updated']
    draw.text((0, 0), title + "   " + updated,fill=BLACK)
    y = 15
    for post in d.entries:
        try:
            draw.text((0, y), post.title, fill=BLACK)
            y = y + 10
            draw.text((10, y), post.description, fill=BLACK)
            y = y + 15
        except:
            print "error: " + post.title
        if y > epd.height:
                break

    # display image on the panel
    epd.display(image)
    epd.update()

# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))
    main(sys.argv[1:])
~
