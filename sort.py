# Copyright(c) 2019 Yuki KODAMA / @kuy
# This script is distributed under the MIT License.

from PIL import Image

orig = Image.open("image.jpg")
orig.show()

def takeComp(i):
    def take(c):
        return c[i]
    return take

for c in range(3):
    takeFunc = takeComp(c)
    gen = Image.new(orig.mode, orig.size)

    xmax, ymax = orig.size
    for x in range(xmax):
        buf = []
        for y in range(ymax):
            pixel = orig.getpixel((x, y))
            buf.append(pixel)
        
        buf.sort(key=takeFunc, reverse=True)

        for y in range(ymax):
            gen.putpixel((x, y), buf[y])

    gen.show()
