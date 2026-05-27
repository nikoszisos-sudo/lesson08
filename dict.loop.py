heroes_weapons = {
    "Black Panther": "Anti-Metal Claws",
    "Wolverine": "Claws",
    "Ultron": "Plasma-Weapons",
    "Spider-Man": "Web-Shooters",
    "Beast": "Claws",
    "Venom": "Web-Shooters"
}

print ("Key-Value Loop:")
for key, value in heroes_weapons.items():
    print (key + " has " + value)

print ("\nOrdered Key Loop:")
for key in sorted(heroes_weapons.keys()):
    print (key + " has " + heroes_weapons[key])

print ("\nWeapons Gallery:")
for value in set(heroes_weapons.values()):
    print (value + " ", end="")
