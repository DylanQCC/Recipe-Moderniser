import csv

YELLOW_B = '\033[1;33m'  # Bold Yellow Text
CYAN = '\033[1;36m'  # Cyan Text
DEFAULT = '\033[m'  # Default Text

# Opening the file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data and put into list
csv_groceries = csv.reader(groceries)

# Creating a dictionary for the data
food_dictionary = {}

# Add the data from the list to the dictionary
# First item in the row is key, next is the definition

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)

loop02 = ""
while loop02 == "":
    amount = eval(input("Enter amount: "))
    amount = float(amount)

    # Get ingredients and change to match dictionary
    ingredient = input("ingredient: ")

    if ingredient in food_dictionary:
        multi_by = food_dictionary.get(ingredient)
        amount = amount * float(multi_by) / 250
        print()
        print(YELLOW_B + "Amount in g {}".format(amount) + DEFAULT)
    else:
        print()
        print(CYAN + "{} is unchanged".format(amount) + DEFAULT)
