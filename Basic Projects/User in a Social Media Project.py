class User:

    def __init__(self, firstname, lastname, likescount, friendsname):

        self.firstname = firstname
        self.lastname = lastname
        self.likescount= likescount
        self.friendsname = friendsname

    def introduceself(self):

        print(f"My Name is {self.firstname} {self.lastname}")

    def fullprofile(self):

        print(f"Full Name: {self.firstname} {self.lastname}")
        print(f"Likes: {str(self.likescount)}")
        print("Friends")

        for friend in self.friendsname:
            print("  -" + friend)
    

userone = User("Reymond", "Joaquin", 20, ["Gian", "Carlo", "Jerome", "Eiann", "Parcia"])
usertwo = User("Gian", "marcelo", 110, ["Reymond", "Carlo", "Jerome", "Eiann", "Parcia"])

usertwo.fullprofile()