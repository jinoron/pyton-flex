from PIL import Image,ImageDraw

afbeelding = Image.open("meme_background2.jpg")

breedte = afbeelding.width
hoogte = afbeelding.height

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting =(helft_breedte, helft_hoogte)

print("De afbeelding is" + str(breedte) + "pizels breeden " + str(hoogte) + "pizels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)

lettertype = ImageFont.truetype("impact.ttf", 40)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = "Coding in Python\nNo problemo!"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

afbeelding.show()

afbeelding.save("meme_met_tekst.jpg") 
