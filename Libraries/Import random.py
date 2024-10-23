import random

# a = random.randint(1,6)
# b = random.random()
# c = random.choice(list)
# d = rando.shuffle()

#Example 1 in random.choice()

list = ["rock","paper","scissors"]

z = random.choice(list)
print(z)

#Example 2 in random.randint(1,6)

x = random.randint(1,6)
print(x)

#Example 3 in random.shuffle()

cards = [1,2,3,4,5,6,7,8,9,"j","k","a","q"]

random.shuffle(cards)
print(cards)

#Example 4 in random.random()

b = random.random()

print(b)