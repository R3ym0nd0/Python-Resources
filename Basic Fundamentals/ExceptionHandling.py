while True:
  
  try:
      
      numerator = int(input("Enter a number to divide: "))
      denominator = int(input("Enter a number to divide by: "))
      result = numerator / denominator

  except ZeroDivisionError as e:
    print(f"{e}: You can't divide 0")
  except ValueError as e:
      print(f"{e}: Number Only!")
  except Exception as e:
     print(f"{e}: Something went wrong :(")
  else:
     print(result)
  finally:
     print("This will always execute :)")