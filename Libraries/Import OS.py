import os

#Example 1: Read a file

location = "C:\\Users\\Reymond Joaquin\\Documents\\Example Files\\hello.txt"

if os.path.exists(location):
    print("That location exist!")
    if os.path.isfile(location):
     print("That is a File!")
    elif os.path.isdir(location):
     print("That is a Directory")
else:
    print("That location doesn't exist!")

#Exampel 2: Move a File

source = "text.txt"
destination = "C:\\Users\\Reymond Joaquin\\Documents\\Python Files\\lol\\text.txt"

try:
    if os.path.exists(destination):
        print("There's already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} was moved!")
except FileNotFoundError:
    print(f"{source} was not moved!")

#Example 3: Delete a file

try:
  
  path = "lame.txt"

  os.remove(path)

except FileNotFoundError:
  print("File Not found!")
except PermissionError:
  print("You do not have permission to delete that!")









