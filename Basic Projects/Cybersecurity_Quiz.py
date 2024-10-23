networkingquestions = [{"question":"1.What does DHCP stand for?\n",
                        "option": ["A.Dynamic Host Configuration Protocol",
                                   "B.Domain Host Configuration Protocol",
                                   "C.Data Handling Configuration Protocol",
                                   "D.Dynamic Host Control Protocol"],
                        "correct answer": "a"},

                {"question":"2.Which device connects multiple computers within a single local area network(LAN)?\n", 
                "option": ["A.Router",
                           "B.Modem",
                           "C.Switch",
                           "D.Firewall"], 
                "correct answer": "c"},

                {"question":"3.What does NAT stand for in networking?\n",  
                "option": ["A.Network Acess Table",
                           "B.Network Address Translation",
                           "C.Network Access Terminal",
                           "D.Network Address Table"],
                "correct answer": "b"},

                {"question":"4.What is the primary function of DNS in networking?\n",  
                "option": ["A.To encrypt data transmissions",
                           "B.To provide IP addresses for domain names",
                           "C.To secure network traffic",
                           "D.To filter web content"],
                "correct answer": "b"},

                {"question":"5.Which protocol is used to assign IP addresses automatically within a network?\n",  
                "option": ["A.FTP",
                           "B.SNMP",
                           "C.DHCP",
                           "D.HTTP"],
                "correct answer": "c"}]

pythonquestions = [{"question":"1.Sino ang pambansang bayani ng Pilipinas?",
                    "correct answer": "a",
                    "option": ["A.Jose Rizal", "B.Apolinario Mabini", "C.Juan Luna", "D.Andres Bonifacio"]},

                    {"question":"2.Sino....: ", 
                     "option": ["A.","B.","C.","D."],
                     "correct answer": "a"},

                    {"question":"3.3 + 3: ", 
                     "option": ["A.","B.","C.","D."], 
                     "correct answer": "a"},

                    {"question":"4.4 + 4", 
                     "option": ["A.","B.","C.","D."],
                     "correct answer": "a"},

                    {"question":"5.5 + 5", 
                     "option": ["A.","B.","C.","D."], 
                     "correct answer": "a"}]

def networking():
    print("---Networking Quiz: Answer the following---")  
    while True:

        try:
            for question_obj in networkingquestions:
                print(question_obj['question'])
                for option in question_obj["option"]:
                    print(option)
                        
                answer = input("Answer: ")
                if answer == question_obj["correct answer"]:
                    print("Correct!")
                else:
                    print("Wrong!")
            
            print("Congrats You completed the Quiz!")
            break

        except Exception as error:
            print(f"{error}")
def python():
    print("---Python Quiz: Answer the following---\n") 
    while True:

        try:

            for question in pythonquestions:
                print(question["question"])
                for option in question["option"]:
                    print(option)

                asking = input("Type your answer here: ")
                if asking == question["correct answer"]:
                    print("Correct")
                else:
                    print("Wrong")
            print("Congrats You completed the Quiz!")
            break

        except Exception as error:
            print({error})
def linux():
    print("---Linux Quiz---\n") 
def  bash():
    print("---Bash Script Quiz---\n") 

def main():
    
    while True: 

        print("")
        print("---Test Your Knowledge---\n")
        print("1.Networking")
        print("2.Python Programming")
        print("3.Linux Operating System")
        print("4.Bash Script")

        try:
            asking = int(input("Pick a Subject (1 - 4 Only): "))
            if asking <= 0 or asking >= 5:
                print("Invalid Choice")
            else:

                if asking == 1:
                    networking()
                elif asking == 2:
                    python()
                elif asking == 3:
                    linux()
                elif asking == 4:
                    bash()
                else:
                    print("1 TO 4 Only")
                
                while True:

                    user = input("Do you want to continue (y/n): ")
                    if user == "Y".lower():
                        break
                    elif user == "N".lower():
                        print("Thanks for using this program :)")
                        exit()
                    else:
                        print("Y or N only!")

        except ValueError as error:
            print("Number Only!")
        except Exception as error:
            print({error})

main()


