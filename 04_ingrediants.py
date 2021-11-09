# Not blank function
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main chunk/area
# Empty ingredient list
ingredients = []

# Loop for user to input ingredients names
stop = ""
while stop != "xxx":
    # Ask user for ingredient, using the not_blank
    get_ingredient = not_blank(" Please enter and ingredient name: ",
                               "This can't be blank",
                               "yes")

    # Stop looping when exit code typed and there are more
    # than two ingredient names
    if get_ingredient.lower() == "xxx" and len(ingredients) > 1:
        break

    # If the exit code is not inputted then add the ingredient to list
    else:
        ingredients.append(get_ingredient)

# Printing the ingredients list
print(ingredients)
