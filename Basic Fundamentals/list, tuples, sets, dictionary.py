#List

courses = ["BSCS", "BSIT", "BSIS", "BSCE", "BSCS"]
name = ["Reymond", "Gian", "Jerome","Carlo"]

food = ["mango", "banana", "apple",["adobo", "menudo",["shampoo","alcohol","palmolive"], "sinigang", "pakbet"]]

x = courses.copy
courses.reverse()
courses.append("BSCRIM")
courses.insert(0, "BSCRIM")
courses[0] = "BSEDUC"
del courses [1]
courses.clear()
courses.remove("BSCS")
courses.pop(0)
name.sort()
name.sort(reverse=True)
print(food[3][2][2])
print(len(courses))
print(courses.count("BSCS"))
print(courses + name)
print(courses)

#Tuples

courses = ("BSCS", "BSIT", "BSIS", "BSCE")
name = ("Reymond", "Gian", "Jerome","Carlo")
courses = list(courses)
print(courses)

#Sets

courses = {"BSCS", "BSIT", "BSIS", "BSCE", "BSCRIM"}
numbers = {1,2,3,4,5,6,7,8,9,10}
courses = list(courses)
setthree = courses.union(numbers)
setthree = courses.difference(numbers)
setthree = courses.intersection(numbers)
setthree = courses.symmetric_difference(numbers)
courses.add("BSeduc")
courses.update(["BSCRIM", "BSEDUC", "CYBERSECURITY", "Technology"])
courses.remove("BSCS")
courses.discard("BSLOL")
courses.pop()
courses.clear()
courses.copy()
print(setthree)
print(courses.isdisjoint(numbers))
print(courses.issubset(numbers))
print(courses.issuperset(numbers))

#Dictionary

student1attributes = {"height":172,
                      "weight":49,
                      "skin":"white"}

student1 = {"name":"Reymond",
           "courses":"BSCS",
           "age":18,
           "physical":student1attributes}

student2 = {"name":"Gian",
           "courses":"BSEDUC",
           "age":18}

students = [student1, student2]



student3 = student1.copy()
student1["name"] = "LOL"
student1.pop("name")
student1.popitem()
student1.clear()
print(student1["age"])
print(student1.get("age"))
print(student1)
print(len(student1))
print(student1.keys())
print(student1.values())
print(student1)