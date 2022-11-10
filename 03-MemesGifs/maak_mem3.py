from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background2 .jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact.ttf", 20)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "programmeren is leuk"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

# Resultaat showen
achtergrond.show()

# Opslaan onder andere naam
achtergrond.save("Meme_afgemaakt.jpg")