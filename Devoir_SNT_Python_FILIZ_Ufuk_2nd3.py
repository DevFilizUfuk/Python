from PIL import Image
from PIL import ImageOps

image = Image.open("pomme.jpg")

largeur_image,hauteur_image = image.size

for y in range (hauteur_image):

   for x in range (largeur_image):

       r,v,b=image.getpixel((x,y))  

       image.putpixel((x,y),(255-r,255-v,255-b))

image.show()
####################################################
image2 = Image.open("n.jpg")

image2 = ImageOps.flip(image2)

largeur_image2,hauteur_image2 = image2.size

for y in range (hauteur_image2):

   for x in range (largeur_image2):

       r,v,b=image2.getpixel((x,y)) 
       image2.putpixel((x,y),(255,145,b))
image2.show()
