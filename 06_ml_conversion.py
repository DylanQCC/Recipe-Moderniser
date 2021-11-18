
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cups": 250,
    "oz": 30,
    "pint": 473,
    "quart": 496,
    "pound": 453.6
}

loop_one = ""
while loop_one == "":

    amount = eval(input("Enter amount: "))
    amount = float(amount)

    unit = input("Enter units: ")

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    loop_one = input("<enter> or q")
    if loop_one != "":
        break
