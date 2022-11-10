import os

bestand = open("C:/Users/ywalt/OneDrive/Bureaublad/MA/Jaar 1/Periode1/FLEX/Python/02-FilesFolders/klasgenoten.txt","r")

tekst_regel = bestand.readline()

while tekst_regel:
    tekst_regel = tekst_regel.strip()
    print(tekst_regel)
    os.mkdir(tekst_regel)
    tekst_regel = bestand.readline()