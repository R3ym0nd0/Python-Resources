print("Write the correct answer, you have 3 life :).")
print("Question: 1 + 1?")

while True:
  try:

    
    life = 3
    answer = int(input("Answer: "))
    if answer == 2:
        print("You Win!!!")
        asking = input("Do you want to continue? ")
        if asking != "yes":
          break
    else:
     life = life -1
     print(f"{life} left!")
    if life <= 0:
      print("You Lose :(")
      break

  except Exception as error:
     print(f"Something went wrong :( {error}")