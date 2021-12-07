YELLOW_B = '\033[1;33m'  # Bold Yellow Text
CYAN = '\033[1;36m'  # Cyan Text
DEFAULT = '\033[m'  # Default Text


# FUNCTIONS

def general_converter(how_much, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        multi_by = dictionary.get(unit)
        how_much = how_much * multi_by * conversion_factor

        return how_much


# Unit checker
def unit_checker():
    current_check = input("Enter units: ")

    # List of abbreviations
    teaspoon = ["t", "tsp", "teaspoon"]
    tablespoon = ["T", "tbs", "tablespoon"]
    cups = ["c", "cups", "cup"]
    ounce = ["oz", "ounce", "ounces", "fluid ounce", "fl oz", "fluid oz"]
    pint = ["pnt", "pint", "pints", "p", "pt", "fl p", "fluid pint"]
    quart = ["quart", "q", "qt", "fluid quart", "fl q"]
    pound = ["pound", "pounds", "lb", "#"]
    litre = ["litre", "litres", "l"]

    if current_check == "":
        print("You chose {}".format(current_check))
        return current_check
    # Tablespoons
    elif current_check == "T" or current_check.lower() in tablespoon:
        return "tbs"
    # Teaspoons
    elif current_check == "t" or current_check.lower() in teaspoon:
        return "tsp"
    # Cups
    elif current_check == "c" or current_check.lower() in cups:
        return "cups"
    # Ounces
    elif current_check == "oz" or current_check.lower() in ounce:
        return "ounce"
    # Pints
    elif current_check == "pnt" or current_check.lower() in pint:
        return "pnt"
    # Quart
    elif current_check == "quart" or current_check.lower() in quart:
        return "quart"
    # Pound
    elif current_check == "pound" or current_check.lower() in pound:
        return "lb"
    # Litre
    elif current_check == "litre" or current_check.lower() in litre:
        return "l"


#                     -     MAIN CODE     -
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 250,
    "ounce": 30,
    "pint": 473,
    "quart": 496,
    "pound": 453.6,
    "litre": 1000
}

loop_one = ""
while loop_one == "":

    amount = eval(input("Enter amount: "))
    amount = float(amount)

    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)

    loop_one = input("<enter> or q")
    print()
    if loop_one != "":
        break
