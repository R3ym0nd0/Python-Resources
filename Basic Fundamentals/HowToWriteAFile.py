#Example 1: how to write some tex

text = "yo bro!\n"

with open("text.txt", "w") as file:
    file.write(text)


#Example 2: how to add some text

text = "nice to see ya!"

with open("text.txt", "a") as file:
    file.write(text)



