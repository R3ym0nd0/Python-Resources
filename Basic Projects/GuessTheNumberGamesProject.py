import random

numbers = random.randint(1,5)

while True:
 
 try:
        
   player = int(input("Guess The Number ('Type 1 - 5): "))
 
   if player == numbers:
        print(f"{player} your correct!, it's {numbers}")
        break

 except ValueError:
       print("Number Only!")
 except Exception:
       print("Something went wrong :(")