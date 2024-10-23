import os

def Subnetting():           
    #Tool Design
    def print_intro():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width

        print(separator)
        print("Tool Name: Automated Subnetting Tool".center(terminal_width))
        print("Version: Beta".center(terminal_width))
        print("Coded by: Reymond Joaquin".center(terminal_width))
        print("Written in: Python".center(terminal_width))
        print(separator)
        print("Description:".center(terminal_width))
        print("-- Welcome to my Automated Subnetting Tool! --".center(terminal_width))
        print("-- This is the first tool I've created in my programming journey! --".center(terminal_width))
        print("-- This tool helps you automatically calculate and manage IP subnets --".center(terminal_width))
        print("-- Use the menu below to navigate through the options --".center(terminal_width))
        print(separator)
    
    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)
        
    #info Function
    def help_function():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width

        print(separator)
        print("Welcome to Automated Subnetting Tool (Version Beta)\n".center(terminal_width))
        print("--> DESCRIPTION <--\n".center(terminal_width))
        print("- This tool provides functionalities for subnetting, including Fixed-Length Subnet Masking (FLSM), Variable-Length Subnet Masking (VLSM), Supernetting, and IP Address/Numbers to Binary Translator.\n".center(terminal_width))
        print(separator)
        print("--> FLSM (Fixed-Length Subnet Masking) <--\n".center(terminal_width))
        print("- All subnets are of equal size, meaning each subnet has the same number of hosts. This method is simple and easy to manage but may lead to IP address wastage.\n")
        print(separator)
        print("--> VLSM (Variable-Length Subnet Masking) <--\n".center(terminal_width))
        print("- Subnets can vary in size, allowing for more efficient IP address allocation based on specific needs. This method is more complex but reduces IP address wastage.\n")
        print(separator)
        print("--> Supernetting <--\n".center(terminal_width))
        print("- A technique used to combine multiple subnets into a single larger network, often to reduce routing complexity.\n")
        print(separator)
        print("--> IP Address to Binary <--\n".center(terminal_width))
        print("- Converts an IP address into its binary equivalent, helping in understanding the underlying network structure.\n\n")
        print(separator)
        print("THANK YOU FOR USING MY AUTOMATED SUBNETTING TOOL!".center(terminal_width))
        print(separator)
        while True:
            user = input("\nType 'q' to quit: ").strip()
            if user.lower() == "q":
                break
            else:
                print("Q only, please try again.")

    #Main Menu Function 
    def main_menu():
        while True:
            print_intro()
            #User asking to pick choices 1 to 5
            print("Type 'info' for more information.\n")
            print("Choices:")
            print("[1] Fixed-Length Subnet Masking(FLSM)")
            print("[2] Variable-Length Subnet Masking(VLSM)")
            print("[3] Supernetting")
            print("[4] IP Address/Numbers to Binary Translator")
            print("[5] Leave\n")
            user = input("--> Pick what you want to use (1 - 5 Only):  ")
            if user == "1":
                separator()
                print("--> Fixed-Length Subnet Masking(FLSM) <--\n")   
                from FLSM_Code import FLSM
                FLSM()
            elif user == "2":
                separator()
                print("--> Variable-Length Subnet Masking(VLSM) <--\n")
                from VLSM_Code import VLSM
                VLSM()
            elif user == "3":
                separator()
                print("--> Supernetting <--\n")
                from Supernetting_Code import Supernetting
                Supernetting()
            elif user == "4":
                separator()
                print("--> IP Address/Numbers to Binary Translator <--\n")
                from Binary import Binary_Translator
                Binary_Translator()
            elif user == "5":
                break
            elif user.lower() == "info":
                help_function()
            else:
                print("1 - 5 or info only")
    main_menu() 
    
if __name__ == "__main__":
    Subnetting()
