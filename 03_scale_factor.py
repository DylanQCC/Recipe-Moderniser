# Functions/Variables
# ___________________
# Numb Check Function

def num_check(question):

    error = "Please enter an integer than is greater than 0"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)


# Main Routine/Code
# _________________
serving_size = num_check("How many servings is this recipe? ")
print()
user_serving = num_check("How many servings do you want? ")

scale_fact = user_serving / serving_size

print("Scale Factor: {}".format(scale_fact))
