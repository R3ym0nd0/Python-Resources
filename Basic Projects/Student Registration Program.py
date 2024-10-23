class Register:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section
    
    def introduce(self):
        print("Student")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")
        print(f"Section: {self.section}")
        print()  # Print an empty line for better readability

# List to store registered students
list_of_register = []

while True:
    print("Enter student details:")
    name = input("Name: ")
    course = input("Course: ")
    year = input("Year: ")
    section = input("Section: ")

    # Create a Register object with the provided details
    student = Register(name, course, year, section)

    # Add the student object to the list
    list_of_register.append(student)

    print("Student registered successfully!")
    
    # Ask if the user wants to continue registering
    choice = input("Do you want to register another student? (yes/no): ").lower()
    if choice != 'yes':
        break

print("\nRegistered Students:")
for student in list_of_register:
    student.introduce()

