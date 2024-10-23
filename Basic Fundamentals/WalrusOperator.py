#:= Operator

#Before:

foods = list()

while True:
    user = input("What food you like? ")

    if user == "quit":
        break
    foods.append(user)

#After:

foods = []

while food := input("What food do you like? ") != "quit":
    foods.append(food)