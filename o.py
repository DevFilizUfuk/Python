from PIL import Image
from PIL import ImageOps
from PIL import turtle


image2 = Image.open("n.jpg")

image2 = ImageOps.flip(image2)

largeur_image2,hauteur_image2 = image2.size

for y in range (hauteur_image2):

   for x in range (largeur_image2):

       r,v,b=image2.getpixel((x,y))
       
       image2.putpixel((x,y),(255,145,b))
image2.show()

turtle = turtle.Turtle()
rayon = 20
turtle.circle(rayon)
