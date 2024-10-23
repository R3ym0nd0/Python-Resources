#While Loop Examples:

#Example 1:

age = 12

while age < 18:
    print("Still Young" + str(age))
    age = age + 1
else:
    print("Legal Age" + str(age))

#Example 2:

studentid = [11111111, 22222222, 333333, 4444444, 55555, 66666, 777777]

i = 0

while i < len(studentid):
    print(studentid[i])
    i = i +1

#Break Keyword in While Loop:

#Example 1:

while True:
    print("Hello World!")
    break

#Conditions in While Loop

#Example 1:

print("Crush ka ba ng crush mo?")

while True:
    answer = input("Answer: ")
    if answer == "hindi" or answer == "nope":
        print("HAHAAHHA")
        break
    else:
        print("Asa ka??")

#Example 2:

numbers = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(numbers):
    if (numbers[i] % 2 == 0):
        print("Even Number: " + str(numbers[i]))
    else:
        print("Odd Number: " + str(numbers[i]))

    i = i+1

#For Loop Examples:

#Example 1:

numbers = [1,2,3,4,5,6,7,8,9,10]
fruits = ["apple","banana","melon","orange","mango",]

for fruit in fruits:
    print(fruit)

#Else in For Loop:

fruits = ["apple","banana","melon","orange","mango",]

for fruit in fruits:
    print(fruit)
else:
    print("No more Fruit")

#Break Keyword and Conditions in For Loop:

#Example 1:

fruits = ["apple","banana","melon","orange","mango",]

for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

#Example 2:

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print("Even numbers: " + str(number))
    else:
        print("Odd Number: " + str(number))

#range() in For Loop:

#Example 1:

for value in range(10):
    print("Hello World")

#Example 2:

for number in range(11):
    print("Number " + str(number))

#Nested For Loop:

#Example 1:

for x in range(5):
    for y in range(5):
        print("Hello", end="")
    print(" New Line")

#Example 2:

coursestudents = [
    ["BSIT","David"],
    ["BSCS", "Carlo"],
    ["BSIT", "Reymond"]
    ]

for student in coursestudents:
    print(student[1])

#Example 3:

coursestudents = [
    ["BSIT","David"],
    ["BSCS", "Carlo"],
    ["BSIT", "Reymond"]
    ]

for liststudent in coursestudents:
    for i in liststudent:
        print(i)
    print()




