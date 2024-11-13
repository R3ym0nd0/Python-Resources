import os

from Helper_Function import separator
from FLSM_Feature import FLSM
from VLSM_Feature import VLSM
from Supernetting_Feature import Supernetting
from Binary_Converter import Binary_Converter

terminal_width: int = os.get_terminal_size().columns

def Subnetting():           

    def intro_function() -> None:
        separator()
        print("Tool Name: IPnetSolver".center(terminal_width))
        print("Version: 1.2".center(terminal_width))
        print("Coded by: Reymond Joaquin".center(terminal_width))
        print("Written in: Python".center(terminal_width))
        separator()
        print("Description:\n".center(terminal_width))
        print("-- Welcome to IPnetSolver 1.2 --\n".center(terminal_width))
        print("-- This is an updated version of 1.0, designed to help you manage and calculate IP subnets with ease --".center(terminal_width))
        print("-- This tool helps automate complex subnetting tasks, including FLSM, VLSM, Supernetting, and more --".center(terminal_width))
        print("-- Use the menu below to navigate through the various options for managing and calculating IP subnets --".center(terminal_width))
        separator()
        
    # Info Function
    def info_function() -> None: 
        separator()
        print("Welcome to IPnetSolver (Version 1.2)".center(terminal_width))
        separator()
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
            user: str = input("\n--> Type 'q' to quit: ").strip() # Asking user to type 'q' to quit
            if user.lower() == "q": # This will check if user type 'q'
                break # Quitting
            else:
                print("Q only, please try again.") # This will print if user didn't type 'q'

    # Main Menu Function 
    def main_menu() -> None:
        while True:
            intro_function()
            # User asking to pick choices 1 to 5
            print("Type 'info' for more information.\n")
            print("Choices:")
            print("[1] Fixed-Length Subnet Masking(FLSM)")
            print("[2] Variable-Length Subnet Masking(VLSM)")
            print("[3] Supernetting")
            print("[4] IP Addresses/Whole Numbers to Binary Converter")
            print("[5] Leave\n")
            user: str = input("--> Pick what you want to use (1 - 5): ").strip().lower() # Asking user to choose in choices
            choices: dict = {"1": lambda: FLSM(),
                             "2": lambda: VLSM(),
                             "3": lambda: Supernetting(),
                             "4": lambda: Binary_Converter(),
                             "5": lambda: exit(),
                             "info": lambda: info_function()
                             }

            if user in choices:
                pick_choice: dict = choices[user]() # This will call the function base of user type in choices
                if pick_choice:
                    print(pick_choice)
            else:
                separator()
                print("Note: 1 - 5 or info only") # This will print if user type invalid choices
    while True:
        try:
            main_menu() # Calling the main_menu() function to start the program
        except KeyboardInterrupt:
            print(f"returning to the start")
if __name__ == "__main__":
    Subnetting()