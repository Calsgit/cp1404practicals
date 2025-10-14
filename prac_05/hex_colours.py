COLOUR_NAME_TO_HEX = {"Electric Purple": "#bf00ff", "Cyan3": "#00cdcd", "Byzantium": "#702963", "Zomp": "#39a78e",
                      "Black": "#000000", "White": "#ffffff", "Gray": "#bebebe", "Gold1": "ffd700",
                      "Malachite": "#0bda51", "Red1": "#ff0000"}

colour = input("Enter Colour Name: ").title()
while colour != "":
    try:
        print(f"{colour} in hex is {COLOUR_NAME_TO_HEX[colour]}")
    except KeyError:
        print(f"{colour} could not be matched to a hex code")
    colour = input("Enter Colour Name: ").title()
