
try:
  with open('text.txt') as file:
      print(file.read())
  print(file.closed)
except FileNotFoundError:
   print("File was not found :(")

