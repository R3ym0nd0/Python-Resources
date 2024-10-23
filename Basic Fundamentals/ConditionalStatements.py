#CONDITIONAL OPERATORS

# == - EQUAL
# != - NOT EQUAL
# > - GREATER THAN
# < - LESS THAN
# >= - GREATER THAN or EQUAL
# <= - LESS THAN or EQUAL

#IF ELIF ELSE STATEMENT

age = int(input("Enter Your Age: "))

if age >= 18:
    print("You're Adult!")
elif age >= 10:
    print("You're Teenager!")
else:
    print("Too Young!")
print("Thank you for using the program :)")

#NESTED CONDITIONAL STATEMENTS

age = int(input("Enter Your Age: "))
height = int(input("Enter Your Height: "))

if age >= 18:
    if height >= 176:
        print("Tall and Legal Age!")
    elif height >= 150:
        print("Average and Legal Age!")
    else:
        print("Short and Legal Age!")
else:
    print("Too Young!")

#NOT KEYWORD and LOGICAL OPERATORS(AND and OR)

#NOT EXAMPLE:

age = int(input("Enter Your Age: "))

if not age >= 18:
    print("Too Young!")
else:
    print("Legal Age")

#AND EXAMPLES:

#EXAMPLE 1:

age = int(input("Enter Your Age: "))
height = int(input("Enter Your Height: "))

if age >= 18 and height >= 176:  
    print("Tall and Legal Age!")
elif age >= 18 and height >= 150:
    print("Average and Legal Age!")      
elif age >= 18:
    print("Short and Legal Age!")
else:
    print("Too Young!")

#EXAMPLE 2:

username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

if username == "Reymond" and password == "joaquin":
    print("Log In Successfully!")
elif username == "Gian" and password == "marcelo":
    print("Log In Successfully!")
else:
    print("Login Failed :(")    

#OR EXAMPLE:

#Teacher wants to get the following:

ballpen = True
notebook =True
pencil = False
bag = False

if ballpen or notebook or pencil or bag or pencil:
    print("Pasok Nak :)")
else:
    print("LABAS!!!!")

#COLLECTION CONDITIONAL STATEMENT

bag = ["gun", "knife", "pencil", "notebook", "phone", "ballpen", "laptop"]

if "gun" or "knife" in bag:
    print("Bawal Pumasok!!!")
else:
    print("Pasok na :)")


