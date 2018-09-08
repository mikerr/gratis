
import sys,time
from PIL import Image
from PIL import ImageDraw
from EPD import EPD

import feedparser

WHITE = 1
BLACK = 0

# headlines.py <rss-url>
# Show headlines (RSS) on e-paper display
#
# http://feeds.bbci.co.uk/news/rss.xml

# default rss
rss = 'http://feeds.skynews.com/feeds/rss/home.xml'

def main(argv):
    """print the latest headlines from an RSS feed"""
    epd = EPD()
    demo(epd)

def demo(epd):
    
    # initially set all white background
    image = Image.new('1', epd.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)

    d = feedparser.parse('http://feeds.skynews.com/feeds/rss/home.xml')

    title = d['feed']['title']
    draw.text((0, 0), title[:25],fill=BLACK)
    draw.text((170, 0), time.ctime(),fill=BLACK)
    
    y = 15
    for post in d.entries:
        try:
            draw.text((0, y), post.title, fill=BLACK)
            y = y + 8
        except:
            print "error: " + post.title
        if y > epd.height:
                break

    # display image on the panel
    epd.display(image)
    epd.update()

# main
if "__main__" == __name__:
    if len(sys.argv) > 1:
        rss = sys.argv[1]
    main(sys.argv[1:])
~
