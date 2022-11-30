# -*- coding: utf-8 -*-
from PIL import Image
p1 = Image.open('n.jpg')
p2 = Image.open('pomme.jpg')
p3 = Image.blend(p1, p2, .8)
p3.save('ss.jpg')
