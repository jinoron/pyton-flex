from PIL import Image

afbeelding = Image.open("testfoto.png")



breedte = afbeelding.width
hoogte = afbeelding.height

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting =(helft_breedte, helft_hoogte)

kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

kleinere_afbeelding.save('testfoto.png')

afbeelding.show()

print("De afbeelding is" + str(breedte) + "pizels breeden " + str(hoogte) + "pizels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)