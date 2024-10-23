usernames = ["Reymond", "Gian", "Carlo"]
passwords = ["reymond123","gian123","carlo123"]

question1 = input("Username: ")
question2 = input("Password: ")

for name in range(len(usernames)):

    if question1 == usernames[name] and question2 == passwords[name]:
        print(f"Welcome {usernames[name]}")
        break
else:
    print("Account not found")

