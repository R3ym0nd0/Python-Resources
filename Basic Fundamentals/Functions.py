#Def:

#Example 1:

def sayhello():
    print("Hello")
    print("World")
sayhello()

#Arguments and Parameters:

#Example 1:

def sayhello(firstname):

    print("Hello, " + firstname)

name = input("Type Your name: ")
sayhello(name)

#Example 2:

def sayhello(firstname, secondname):

    print("Hello, " + firstname + " " + secondname)

person1 = input("Type Your 1st Name: ")
person2 = input("Type Your Last Name: ")

sayhello(person1, person2)

#Return Values:

# Example 1:

def add(numberone, numbertwo):
    return numberone + numbertwo
sum = add(5,3)
print(sum)

#Example 2:

def legalage(age):

    if age >= 18:
        return True
    else:
        return False
    
person = int(input("Type Your Age: "))

print(legalage(person))

#Arbitraty Arguments:

#Example 1:

def sayhello(*names):
     
     for name in names:
       print("Hello, " + name)

sayhello("reymond","Gian","Carlo","Jerome")

#Keyword Arguments:

#Example 1:

def sayhello(firstname, lastname):

    print("Hello, " + firstname + " " + lastname)

sayhello(lastname = "Joaquin", firstname = "Reymond")

#Example 2:

def printfamily(*firstname, lastname):

    for name in firstname:
     print("Hello, " + name + " " + lastname)

printfamily("Reymond", "Gian", "Carlo", "Jerome", lastname = "Joaquin")

#Arbitrary Keyword Arguments:

#Example 1:

def family(**student):

    print(student["name"])
    print(student["age"])
    print(student["course"])
    print(student["average"])  

family(name = "Reymond", age = 18, course = "BSIT", average = 92)





