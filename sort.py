# Copyright(c) 2019 Yuki KODAMA / @kuy
# This script is distributed under the MIT License.

from PIL import Image

orig = Image.open("image.jpg")
origdata = list(orig.getdata())
orig.show()

def takeComp(i):
    def take(c):
        return c[i]
    return take

for c in range(3):
    takeFunc = takeComp(c)
    
    buf = []
    xmax, ymax = orig.size
    for row in range(ymax):
        base = row * xmax
        line = origdata[base:base+xmax]
        line.sort(key=takeFunc, reverse=True)
        buf += line

    gen = Image.new(orig.mode, orig.size)
    gen.putdata(buf)
    gen.show()
