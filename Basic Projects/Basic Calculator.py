def Run_Calculator():
 
 while True:
  
  try:
    
    valid_operators = ["+", "-", "*", "//"]
    operator = input("Type (+, //, *, -): ")

    while operator not in valid_operators:
        print(f"Invalid Operator: {operator}")
        operator = input("Type (+, //, *, -): ")

    def calculator(a, b):

        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "-":
            return a - b
        elif operator == "//":
            return a % b

    QuestionOne = int(input("Type 1st Number: "))
    QuestionTwo = int(input("Type 2nd Number: "))

    answer = calculator(QuestionOne, QuestionTwo)
    print(f"Answer: {answer}")

    while True:
      
      QuestionThree = input("Do you want to continue (Yes/No): ")
      if QuestionThree == "yes".lower():
         break
      elif QuestionThree == "no".lower():
         print("Bye!")
         return
      else:
          print("Yes or No Only!")

  except Exception as error:
    print(f"Something went wrong :(: {error}")

if __name__ == "__main__":
    Run_Calculator()



