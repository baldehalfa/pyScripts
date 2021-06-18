#!/usr/bin/python

from PIL import Image
import os, sys

path = "C:/Users/images/"
dirs = os.listdir( path )


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((32,32), Image.ANTIALIAS)
            imResize.save(f + '_32.png', 'PNG', quality=90)
                  
resize()

input('Press Enter to Continue...')