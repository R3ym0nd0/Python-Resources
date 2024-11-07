import os

def Subnetting():           

    def print_intro():
        terminal_width = os.get_terminal_size().columns
        
        separator()
        print("Tool Name: IPnetSolver".center(terminal_width))
        print("Version: 1.1".center(terminal_width))
        print("Coded by: Reymond Joaquin".center(terminal_width))
        print("Written in: Python".center(terminal_width))
        separator()
        print("Description:\n".center(terminal_width))
        print("-- Welcome to IPnetSolver 1.1 --\n".center(terminal_width))
        print("-- This is an updated version of 1.0, designed to help you manage and calculate IP subnets with ease --".center(terminal_width))
        print("-- This tool helps automate complex subnetting tasks, including FLSM, VLSM, Supernetting, and more --".center(terminal_width))
        print("-- Use the menu below to navigate through the various options for managing and calculating IP subnets --".center(terminal_width))
        separator()
    
    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)
        
    # Info Function
    def help_function():
        terminal_width = os.get_terminal_size().columns

        separator()
        print("Welcome to IPnetSolver (Version 1.1)\n".center(terminal_width))
        print("--> DESCRIPTION <--\n".center(terminal_width))
        print("- This tool provides functionalities for subnetting, including Fixed-Length Subnet Masking (FLSM), Variable-Length Subnet Masking (VLSM), Supernetting, and IP Address/Numbers to Binary Translator.\n".center(terminal_width))
        separator()
        print("--> FLSM (Fixed-Length Subnet Masking) <--\n".center(terminal_width))
        print("- All subnets are of equal size, meaning each subnet has the same number of hosts. This method is simple and easy to manage but may lead to IP address wastage.\n")
        separator()
        print("--> VLSM (Variable-Length Subnet Masking) <--\n".center(terminal_width))
        print("- Subnets can vary in size, allowing for more efficient IP address allocation based on specific needs. This method is more complex but reduces IP address wastage.\n")
        separator()
        print("--> Supernetting <--\n".center(terminal_width))
        print("- A technique used to combine multiple subnets into a single larger network, often to reduce routing complexity.\n")
        separator()
        print("--> IP Address to Binary <--\n".center(terminal_width))
        print("- Converts an IP address into its binary equivalent, helping in understanding the underlying network structure.\n\n")
        separator()
        print("Thank you for using my IPnetSolver Tool!".center(terminal_width))
        separator()

        while True:
            user = input("\nType 'q' to quit: ").strip() # Asking user to type 'q' to quit
            if user.lower() == "q": # This will check if user type 'q'
                break # Quitting
            else:
                print("Q only, please try again.") # This will print if user didn't type 'q'

    # Main Menu Function 
    def main_menu():
        terminal_width = os.get_terminal_size().columns
        while True:
            print_intro()
            # User asking to pick choices 1 to 5
            print("Type 'info' for more information.\n")
            print("Choices:")
            print("[1] Fixed-Length Subnet Masking(FLSM)")
            print("[2] Variable-Length Subnet Masking(VLSM)")
            print("[3] Supernetting")
            print("[4] IP Address/Numbers to Binary Translator")
            print("[5] Leave\n")
            user = input("--> Pick what you want to use (1 - 5): ").strip() # Asking user to choose in choices
            if user == "1": # This will checl if user type '1'
                separator()
                print("--> Fixed-Length Subnet Masking(FLSM) <--".center(terminal_width))
                separator()
                from FLSM_Feature import FLSM # FLSM Module
                FLSM() # Calling the FLSM function in FLSM_Code file
            elif user == "2": # This will checl if user type '2'
                separator()
                print("--> Variable-Length Subnet Masking(VLSM) <--".center(terminal_width))
                separator()
                from VLSM_Feature import VLSM # Calling the VLSM function in VLSM_Code file
                VLSM()
            elif user == "3": # This will checl if user type '3'
                separator()
                print("--> Supernetting <--".center(terminal_width))
                separator()
                from Supernetting_Feature import Supernetting # Supernetting Module
                Supernetting() # Calling the Supernetting function in Supernetting_Code file
            elif user == "4": # This will checl if user type '4'
                separator()
                print("--> IP Address/Numbers to Binary Translator <--".center(terminal_width))
                separator()
                from Binary_Converter import Binary_Converter # Binary_Translator Module
                Binary_Converter() # Calling the Binary_Translaor function in Binary_Translator file
            elif user == "5": # This will checl if user type '5'
                break
            elif user.lower() == "info": # This will check if user type 'info'
                help_function() # Calling the help_function
            else:
                print("1 - 5 or info only") # This will print if user type invalid choices
    main_menu() # Calling the main_menu() function to start the program
    
if __name__ == "__main__":
    Subnetting()