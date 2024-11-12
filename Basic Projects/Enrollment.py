import random

def Enrollment():

    class students:

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def get_courses(self, courses):
            self.courses = courses
            self.courses = ["BSIS", "Criminology", "BPE", "Psychology"]
            return random.choice(self.courses)
    
        def get_sections(self, section):
            self.section = section
            self.section = ["1A", "1B", "1C", "1D"]
            return random.choice(self.section)

        def registered(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Course: ")
            print(f"Section: ")
    
    def gathering_info():
        students_info = []

        while True:
            try:
                name = input("Type your Name: ").strip().capitalize()
                age = int(input("Type your Age: "))
                asking = input("Do you want to continue Y/N: ").strip().lower()

                student = students(name, age)
                
                if asking == "y":
                    students_info.append(student)          
                elif asking == "n":
                    students_info.append(student)
                    break
                else:
                    print("Note: Invalid choice, please try again")

            except ValueError:
                print("Please type a Number")
                students_info = []
            except Exception:
                print("Something went wrong, please try again.")
                students_info = []

        for i, stu in enumerate(students_info):
            print(f"\nStudent {i +1}:")
            stu.registered()

    def main():
        gathering_info()
    main()

if __name__ == "__main__":
    Enrollment()
