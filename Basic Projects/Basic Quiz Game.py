print("QUIZ GAME!")
print("Choose The Correct Answer.\nYou only have 3 life.")
print()

life = 3

# Define the questions and answers
questions = [
    {
        "question": "1. Sino ang Pambansang Bayani ng Pilipinas?",
        "options": ["A. Jose Rizal", "B. Apolinario Mabini", "C. Juan Luna", "D. Reymond Joaquin"],
        "correct_answer": "A"
    },
    {
        "question": "2. Masaya ba mabuhay sa Pilipinas?",
        "options": ["True", "False"],
        "correct_answer": "True"
    }
]

# Function to ask a question and handle user input
def ask_question(question_obj):
    
    print(question_obj["question"])
    for option in question_obj["options"]:
        print(option)
    
    while True:
        answer = input("Answer: ").strip().lower()
        
        if answer == question_obj["correct_answer"].lower():
            print("Correct!")
            return True
        elif answer == "":
            print("Please Answer The Question")
        else:
            global life
            life -= 1
            print(f"Wrong! {life} life left")
            if life <= 0:
                print("You Lose!")
                return False

# Loop through each question
for question in questions:
    if not ask_question(question):
        break  # Exit the loop if user loses
    
    # Ask if user wants to continue
    while True:
        answer = input("Do you want to continue? (yes/no): ").strip().lower()
        if answer == "yes":
            break
        elif answer == "no":
            print("Bye!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    # Reset life for the next question
    life = 3

print("Congratulations! You completed the quiz!")
