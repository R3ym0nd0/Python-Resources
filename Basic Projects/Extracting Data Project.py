students = [
    ["BSIT",["David", "Alenere"]],
    ["BSCS",["Jaymar", "Emman", "Patrick"]],
    ["BSEDUC",["Gian","Jerome","Eiann"]]
            ]

for student in students:
    print(student[0])
    for x in student[1]:
        print(" -" + x)
    print()