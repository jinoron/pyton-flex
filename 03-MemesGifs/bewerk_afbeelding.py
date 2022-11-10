from PIL import Image

afbeelding = Image.open("testfoto.png")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("De afbeelding is" + str(breedte) + "pizels breeden " + str(hoogte) + "pizels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)