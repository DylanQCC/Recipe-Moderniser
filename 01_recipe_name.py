# Asking user for recipe name
# Blank check here

def not_blank(question):
    error = "Your recipe name has  numbers in it."
    has_errors = ""

    valid = False
    while not valid:
        response = input(question)

        # look at each character in string and if it's a number, complain
        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main recipe question
recipe_name = not_blank("Enter recipe name: ")

print("You're making {}".format(recipe_name))
