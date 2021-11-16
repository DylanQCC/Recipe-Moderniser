RED_B = '\033[0;1;31m'  # Bold Red Text
DEFAULT = '\033[m'  # Default Text


# Numb Check Function:
def num_check(question):
    # Error message for ingredient amount:
    error = RED_B + "           ~      ERROR      ~" "\nPlease enter an integer that is greater than 0\n" + DEFAULT

    valid = False
    while not valid:
        response = input(question)

        if response.lower() == "exit":
            return "exit"

        else:
            try:
                if float(response) <= 0:
                    print(error)
                else:
                    return response

            except ValueError:
                print(error)


# Not blank function:
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # Look at each character in string and if it's a number, complain
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


# Main chunk/area --------------------------
scale_factor = float(input("Scale Factor: "))

# Empty ingredient list
ingredients = []

# Loop for user to input ingredients names
stop = ""
while stop != "exit":

    amount = num_check("What amount of this ingredient? ")

    if amount.lower() == "exit" and len(ingredients) > 1:
        break

    elif amount.lower() == "exit" and len(ingredients) < 2:
        print(RED_B + "You must have 2 or more ingredients\n"
              " Please add more ", DEFAULT)

    # Add ingredient to list if theres no "exit" code
    else:
        get_ingredient = not_blank(" Please enter an ingredient name: ",
                                   "This can't be blank",
                                   "yes")
        amount = float(amount) * scale_factor

        ingredients.append("{} units {}".format(amount, get_ingredient))

print(ingredients)
