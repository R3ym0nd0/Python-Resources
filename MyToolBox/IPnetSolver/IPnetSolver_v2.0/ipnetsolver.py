from Helper_Function import separator   
from Helper_Function import clear_screen

from FLSM_Feature import FLSM
from VLSM_Feature import VLSM
from Supernetting_Feature import Supernetting
from Binary_Converter import Binary_Converter
from Guide_Feature import calculation_guide
from colorama import Fore, init

# Initialize colorama to automatically reset color after each print
init(autoreset=True)

def Subnetting():           

    def intro_function() -> None:
        separator()
        print(Fore.LIGHTCYAN_EX + rf"""
  _____ _____            _    _____       _                
 |_   _|  __ \          | |  / ____|     | |               
   | | | |__) | __   ___| |_| (___   ___ | |_   _____ _ __ 
   | | |  ___/ '_ \ / _ \ __|\___ \ / _ \| \ \ / / _ \ '__|
  _| |_| |   | | | |  __/ |_ ____) | (_) | |\ V /  __/ |   
 |_____|_|   |_| |_|\___|\__|_____/ \___/|_| \_/ \___|_|
                                                                   
        {Fore.LIGHTMAGENTA_EX}- IP Calculations Made Easy, and Can Be Your Buddy!""")
        separator()
        print(f"{Fore.RED}Tool Name   {Fore.WHITE}: {Fore.LIGHTGREEN_EX}IPnetSolver")
        print(f"{Fore.RED}Version     {Fore.WHITE}: {Fore.LIGHTGREEN_EX}2.0")
        print(f"{Fore.RED}Coded by    {Fore.WHITE}: {Fore.LIGHTGREEN_EX}Reymond Joaquin")
        print(f"{Fore.RED}Description {Fore.WHITE}: {Fore.LIGHTGREEN_EX}It simplifies subnetting with FLSM, VLSM, Supernetting, and IP-to-binary conversion")
        print(f"{Fore.RED}Purpose     {Fore.WHITE}: {Fore.LIGHTGREEN_EX}This tool helps network engineers and students learn and assist with networking calculations")
        print(f"{Fore.RED}Disclaimer  {Fore.WHITE}: {Fore.LIGHTGREEN_EX}For educational and professional use only. Misuse is prohibited")
        separator()

    # Info Function
    def guide() -> None: 
        while True:
            separator()
            print(f"{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}Welcome to IPnetSolver v2.0 Calculation Guide {Fore.MAGENTA}[*]\n")
            print(f"""{Fore.YELLOW}[*] {Fore.RED}NOTE {Fore.YELLOW}[*]
                    
    {Fore.WHITE}Before using this guide, make sure you understand {Fore.LIGHTGREEN_EX}IP addresses{Fore.WHITE},
    {Fore.LIGHTGREEN_EX}network {Fore.WHITE}and {Fore.LIGHTGREEN_EX}broadcast addresses{Fore.WHITE}, {Fore.LIGHTGREEN_EX}subnet masks{Fore.WHITE}, {Fore.LIGHTGREEN_EX}prefix length{Fore.WHITE},
    {Fore.WHITE}and {Fore.LIGHTGREEN_EX}binary conversion{Fore.WHITE}. This will help you follow along more easily.\n""")    
            print(f"{Fore.LIGHTCYAN_EX}[1] {Fore.WHITE}FLSM Calculation Guide")
            print(f"{Fore.LIGHTCYAN_EX}[2] {Fore.WHITE}VLSM Calculation Guide")
            print(f"{Fore.LIGHTCYAN_EX}[3] {Fore.WHITE}Supernetting Calculation Guide")
            print(f"{Fore.LIGHTCYAN_EX}[4] {Fore.WHITE}Binary Conversion Guide (Whole Number and IP Address)")
            separator()
            user: str = input(f"{Fore.RED}[*] {Fore.WHITE}Pick an option ({Fore.RED}1 - 4 {Fore.WHITE}/ Type {Fore.RED}'q' {Fore.WHITE}to quit): ").strip() # Asking user to type 'q' to quit
            if user.lower() == "q": # This will check if user type 'q'
                clear_screen()
                break # Quitting
            elif user in ["1", "2", "3", "4"]:
                calculation_guide(user)
                while True:
                    quit = input(f"{Fore.RED}[*] {Fore.WHITE}Type {Fore.RED}'q' {Fore.WHITE}to quit: ").lower().strip()
                    if quit == "q":
                        break
                    else:
                        print(f"{Fore.RED}\n!! {Fore.YELLOW}Type 'q' to quit {Fore.RED}!!")
                        separator()
                    
            else:
                print(f"\n{Fore.RED}!! {Fore.YELLOW}1 - 4 or Q only, please try again. {Fore.RED}!!") # This will print if user didn't type 'q'
    
    # Main Menu Function 
    def main_menu() -> None:
        while True:
            intro_function()
            # User asking to pick choices 1 to 5
            print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Choices:\n")
            print(f"{Fore.LIGHTCYAN_EX}[1] {Fore.LIGHTWHITE_EX}Fixed-Length Subnet Masking (FLSM)")
            print(f"{Fore.LIGHTCYAN_EX}[2] {Fore.LIGHTWHITE_EX}Variable-Length Subnet Masking (VLSM)")
            print(f"{Fore.LIGHTCYAN_EX}[3] {Fore.LIGHTWHITE_EX}Supernetting")
            print(f"{Fore.LIGHTCYAN_EX}[4] {Fore.LIGHTWHITE_EX}IP Addresses/Whole Numbers to Binary Converter")
            print(f"{Fore.LIGHTCYAN_EX}[5] {Fore.LIGHTWHITE_EX}Exit")
            separator()
            user: str = input(f"{Fore.RED}[*] {Fore.WHITE}Pick an option ({Fore.LIGHTCYAN_EX}1 - 5 {Fore.WHITE}/ {Fore.GREEN}'guide' {Fore.WHITE}for network calculation guide): ").strip().lower() # Asking user to choose in choices
            choices: dict = {"1": lambda: FLSM(),
                             "2": lambda: VLSM(),
                             "3": lambda: Supernetting(),
                             "4": lambda: Binary_Converter(),
                             "5": lambda: exit(),
                             "guide": lambda: guide()
                             }

            if user in choices:
                pick_choice: dict = choices[user]() # This will call the function base of user type in choices
                if pick_choice:
                    print(pick_choice)
            else:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}1 - 5 or 'guide' only {Fore.RED}!!") # This will print if user type invalid choices
    while True:

        try:
            main_menu() # Calling the main_menu() function to start the program
        except KeyboardInterrupt:
            print("returning to the start")
if __name__ == "__main__":
    Subnetting()