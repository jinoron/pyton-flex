# Hier importeer je de os module
import os

# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)

# Op het scherm printen
print("De huidige map is: " + werkmap)

# Een nieuwe map maken met os.mkdir()
os.mkdir("Map")

# De gebruiker vragen welke naam hij de map wilt geven
mapnaam = input("Hoe wil je dat de map heet? ")

# Als de naam van de map groter is dan 0 dan maakt hij er een
lengte_map = len(mapnaam)
if lengte_map > 0:
    os.mkdir(mapnaam)
    print("De map: " + mapnaam + " is gemaakt!")
else:
    print("Vul een geldige naam in voor jou map! ")