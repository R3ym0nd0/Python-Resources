#Class

#Example 1:

class character:
    name = "Reymond"
    hp = 100
    mp =50
    atk = 12
    lvl = 1

character1 = character()
character2 = character()

character2.name = "Gian"
character2.hp = 200
character2.atk = 100
character2.mp = 15
character2.lvl = 10

print(character2.hp)

# #Constructors

# #Example 1:

class Character:

    def __init__(self):
        print("Character Created")

characterone = Character()
charactertwo = Character()
characterthree = Character()

#Object with Constructor:

#Example 1:

class Character:

    def __init__(self, name, hp, level, attack, mp,):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack= attack
        self.mp = mp
        print("Created " + self.name)

characterone = Character(name = "Reymond", hp = 200, level = 10, attack = 50, mp = 100)
charactertwo = Character(name = "Gian", hp = 300, level = 20, attack = 60, mp = 200)

#Object Functions:

#Example 1:

class Animal:

    def __init__(self, type, voice, introduce):
        self.type = type
        self.voice = voice
        self.introduce = introduce

    def speak(self):
        print(self.voice)

    def types(self):
        print(self.type) 

    def introduceself(self):
        print(self.introduce)

animalone = Animal("Dog","Arf","I am Dog!")
animaltwo = Animal("Cat", "Meow","I am Cat!")
 
animaltwo.introduceself()

#Inheritance

#Example 1:

class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def introduce(self):
        print(f"Hi, I am {self.firstname} {self.lastname}")

class Student(Person):
    pass

PersonOne = Person("Connie", "Joaquin")

studentone = Student("Reymond", "Joaquin")

#Overriding Constructor

#Example 1: 

class Parent:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def introduce(self):
        print(f"Hi, I am {self.firstname} {self.lastname}")

class Child(Parent):

    def __init__(self,firstname,lastname, sectionyear):
        super().__init__(firstname, lastname)

        self.sectionyear = sectionyear

childone = Child("Reymond", "Joaquin", "12 - Agoncillo")

#Overriding Functions

#Example 1:

class Parent:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def introduce(self):
        print(f"Hi, I am {self.firstname} {self.lastname}")

class Child(Parent):

    def __init__(self,firstname,lastname, sectionyear):
        super().__init__(firstname, lastname)

        self.sectionyear = sectionyear

    def introduce(self):
        print(f"Hi, I am {self.firstname} {self.lastname} and my section is {self.sectionyear}")

parentone = Parent("Connie", "Joaquin")
childone = Child("Reymond", "Joaquin", "12 - Agoncillo")

parentone.introduce()
childone.introduce()

#Example 2:

class Parent:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def introduce(self):
        print(f"Hi, I am {self.firstname} {self.lastname}")

class Child(Parent):

    def __init__(self,firstname,lastname, sectionyear):
        super().__init__(firstname, lastname)

        self.sectionyear = sectionyear

    def introduce(self):
        super().introduce()
        print(f"From {self.sectionyear}")

class Employee(Parent):

    def __init__(self,firstname, lastname, salary):
        super().__init__(firstname, lastname)

        self.salary = salary
    
    def introduce(self):
        super().introduce()
        print(f"My salary is {str(self.salary)}")


parentone = Parent("Connie", "Joaquin")
childone = Child("Reymond", "Joaquin", "12 - Agoncillo")
employeeone = Employee("Gian", "Marcelo", 5000)

parentone.introduce()
childone.introduce()
employeeone.introduce()

#Adding Function:

#Example 1:

class Parent:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def introduce(self):
        print(f"Hi, I am {self.firstname} {self.lastname}")

    def introducelastname(self):
        print(f"My Username is {self.lastname}")


class Child(Parent):

    def __init__(self,firstname,lastname, sectionyear):
        super().__init__(firstname, lastname)

        self.sectionyear = sectionyear

    def introduce(self):
        super().introduce()
        print(f"From {self.sectionyear}")

    def saysection(self):
        print(f"I am from {self.sectionyear}")

parentone = Parent("Connie", "Joaquin")
childone = Child("Reymond", "Joaquin", "12 - Agoncillo")

#Creating Object with User Input:

#Example 1:

class Person:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} Created")

names = input("Enter Name: ")

pone = Person(names)

# Store Objects in Collection

# Example 1:

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

pone = Person("Reymond")
ptwo = Person("David")
pthree = Person("Gian")

listofpeople = [pone, ptwo, pthree]

listofpeople[2].introduce()

# Using Loop To Read Collections:

class Person:

    def __init__(self, name):
        self.name = name

p1 = Person("Reymond")
p2 = Person("Gian")
p3 = Person("Luis")

listofpeople  = [p1,p2,p3]

for people in listofpeople:
    print(people.name)

#Using Loop To Write in Collections:

#Example 1:

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

listofpeople = []

for i in range(5):

    name = input("Name: ")
    p = Person(name)
    listofpeople.append(p)

for person in listofpeople:
    person.introduce()









