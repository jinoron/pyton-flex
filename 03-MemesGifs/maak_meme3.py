from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("C:/Users/jinau/OneDrive/Bureaublad/ma/bewijzenmap/periode 1.1/flex-les phyton/03-MemesGifs/meme_background2.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact.ttf", 20)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Hoelaat begin ik morgen\n9 uur..."
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(255,255,255))

# Resultaat showen
achtergrond.show()

# Opslaan onder andere naam
achtergrond.save("Meme_afgemaakt.jpg")
