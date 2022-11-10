from PIL import Image, ImageFont

afbeelding = Image.open("meme_background.jpg")

lettertype = ImageFont.truetype("impact.ttf", 40)

breedte = afbeelding.width
hoogte = afbeelding.height


maak_meme.py

print("De afbeelding is" + str(breedte) + "pizels breeden " + str(hoogte) + "pizels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)

tekengebied = ImageDraw.Draw.Draw(achtergrond)
tekst = "codeing in python\nNo problemo!"

tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

afbeelding.show()

