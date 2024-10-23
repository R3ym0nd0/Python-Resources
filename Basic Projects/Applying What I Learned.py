class Person:

    def __init__(self, name, course, year, section):

        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
         
         print()
         print("Registered")
         print(F"Name: {self.name}")
         print(F"Course {self.course}")
         print(F"Year: {self.year}")
         print(F"Section: {self.section}")


listofpeople = []

while True:

    print("Student Details:")
    names = input("Enter Name: ")
    courses= input("Enter Course: ")
    years = input("Enter Year: ")
    sections = input("Enter Section: ")

    p = Person(names, courses, years, sections)
    listofpeople.append(p)
    question = input("Do you want to continue: ")

    if question != "yes".lower():
        break

for student in listofpeople:
        student.introduce()