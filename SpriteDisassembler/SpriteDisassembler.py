from PIL import Image
from SpriteArray import patterns, modname, format, size

ImPatch = modname.replace(" ", "_")
im = Image.open("./" + ImPatch + "CSS.png")
itemformat = format / size
for pattern in patterns:
    itemname, position = pattern
    xsprite = (int(position) - 1) % itemformat
    ysprite = (int(position) - 1) // itemformat
    x = xsprite * size
    y = ysprite * size
    box = (x, y, x + size, y + size)
    region = im.crop(box)
    imout = Image.new("RGBA", (size, size), (255, 0, 0, 0))
    imout.paste(region)
    imgname = "Grid " + itemname + " (" + modname + ").png"
    imout.save(imgname)
    imout = Image.open(imgname)
