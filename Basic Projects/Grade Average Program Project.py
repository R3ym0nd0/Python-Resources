print("Grade Average Program")

firstquarter = float(input("Enter your 1st Grade: "))
secondquarter = float(input("Enter your 2nd Grade: "))
thirdquarter = float(input("Enter your 3rd Grade: "))
fourthquarter = float(input("Enter your 4th Grade: "))

total = firstquarter + secondquarter + thirdquarter + fourthquarter
average = total / 4

if average > 100 or average <= 0:
    print("Invalid Grade")
    print("Average: " + str(average))
elif average >= 98:
    print("With Highest Honor")
    print("Average: " + str(average))
elif average >= 95:
    print("With High Honor")
    print("Average: " + str(average)) 
elif average >= 90:
    print("With Honor")
    print("Average: " + str(average))
elif average >= 75:
    print("Passed")
    print("Average: " + str(average))
else:
    print("Failed")
    print("Average: " + str(average))