import ipaddress as IP

from Helper_Function import separator
from Helper_Function import clear_screen
from colorama import Fore, init

# Initialize colorama to automatically reset color after each print
init(autoreset=True)

def Binary_Converter() -> None:

    def menu() -> None:
        while True:
            print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Choices:"}\n")
            print(f"{Fore.LIGHTCYAN_EX + "[1]"} {Fore.WHITE + "Whole Number to Binary"}")
            print(f"{Fore.LIGHTCYAN_EX + "{2]"} {Fore.WHITE + "IP Address to Binary"}")
            separator()
            user: int = input(f"{Fore.RED + "[*]"} {Fore.WHITE + "Choose a number (Type"} {Fore.RED + "'q'"} {Fore.WHITE + "to quit):"} ").strip().lower() # Asking user to choose in choices
            if user == "q":
                clear_screen()
                return None # Quitting
            elif user == "1":
                whole_numbers() # Calling the decimal_number function if user type 1
            elif user == "2":
                ip_address() # Callin the ip_address function if user type 2
            else:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Invalid Choice"} {Fore.RED + "!!"}") # This will print if user didn't type valid choices
                separator()

    def whole_numbers() -> None:
        separator()
        print(f"{Fore.MAGENTA + "[*]"} {Fore.LIGHTCYAN_EX + "Whole Number to Binary"} {Fore.MAGENTA + "[*]"}\n")
        while True:
            try:
                user: str = input(f"{Fore.RED + "[*]"} {Fore.WHITE + "Type a whole number (Type"} {Fore.RED + "'q'"} {Fore.WHITE + "to quit): "}").strip() # Asking user to type a whole number
                if user == "q": # This will check if user type 'q'
                    separator()
                    break # Quitting
        
                int_user = int(user) # Translating the user variable into interger

                binary: bin = bin(int_user).split("0b") # This will converts the num variable into binary
                print(f"\n{Fore.MAGENTA + "[*]"} {Fore.LIGHTCYAN_EX + f"Result: {Fore.LIGHTGREEN_EX + f"{binary[1]}"}"}") # This will print the binary result
                separator()

            except ValueError:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please type a whole number"} {Fore.RED + "!!"}") # This will check if user type whole number
                separator()

    def ip_address() -> None:
        separator()
        print(f"{Fore.MAGENTA + "[*]"} {Fore.LIGHTCYAN_EX + "IP Address to Binary"} {Fore.MAGENTA + "[*]"}\n")
        while True:
            try:
                user: IP.ip_address = input(f"{Fore.RED + "[*]"} {Fore.WHITE + "Type IP Address (Type"} {Fore.RED + "'q'"} {Fore.WHITE + "to quit): "}").strip() # Asking user to type IP Address
                if user.lower() == 'q': # This will check if user type 'q'
                    separator()
                    break # Quitting
                ip: IP.ip_address = IP.IPv4Address(user) # This will convert the user variable into IPV4Address object
                int_ip = int(ip) # This will translate the ip address or ip variable into integer
                binary: bin = format(int_ip, "032b") # This will now translate the int_ip variable into binary
                print(f"\n{Fore.MAGENTA + "[*]"} {Fore.LIGHTCYAN_EX + "Result: "} {Fore.LIGHTGREEN_EX + binary[0:8]}.{binary[8:16]}.{binary[16:24]}.{binary[24:32]}") # This will now print the result of binary
                separator()
            except Exception:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please type a valid IP Address"} {Fore.RED + "!!"}") # This will print if user didn't type a valid IP Address
                separator()

    def main():
        separator()
        print(f"{Fore.MAGENTA + "[*]"} {Fore.LIGHTCYAN_EX + "IP Address/Numbers to Binary Converter"} {Fore.MAGENTA + "[*]"}\n")
        while True:
            if menu() is None: # This wil check if menu function returns 
                break
    main() # Calling the main function because if not, you will see blank :)
if __name__ == "__main__":
    Binary_Converter()