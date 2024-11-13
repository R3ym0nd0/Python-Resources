import ipaddress as IP
import os

from Helper_Function import separator

terminal_width: int = os.get_terminal_size().columns

def Binary_Converter() -> None:

    def menu() -> None:
        while True:
            print("Choices:")
            print("[1] Whole Number to Binary")
            print("[2] IP Address to Binary")
            separator()
            user: int = input("--> Choose a number (Type 'q' to quit): ").strip().lower() # Asking user to choose in choices
            if user == "q":
                return None # Quitting
            elif user == "1":
                whole_numbers() # Calling the decimal_number function if user type 1
            elif user == "2":
                ip_address() # Callin the ip_address function if user type 2
            else:
                separator()
                print("Note: Invalid Choice") # This will print if user didn't type valid choices
                separator()

    def whole_numbers() -> None:
        separator()
        print("--> You chose Whole Number to Binary <--".center(terminal_width))
        separator()
        while True:
            try:
                user: str = input("--> Type a whole number (Type 'q' to quit): ").strip() # Asking user to type a whole number
                if user == "q": # This will check if user type 'q'
                    separator()
                    break # Quitting
        
                int_user = int(user) # Translating the user variable into interger

                binary: bin = bin(int_user).split("0b") # This will converts the num variable into binary
                separator()
                print(f"Result: {binary[1]}".center(terminal_width)) # This will print the binary result
                separator()

            except ValueError:
                separator()
                print("Note: Please type a whole number") # This will check if user type whole number
                separator()

    def ip_address() -> None:
        separator()
        print("--> You chose IP Address to Binary <--".center(terminal_width))
        separator()
        while True:
            try:
                user: IP.ip_address = input("--> Type IP Address (Type 'q' to quit): ").strip() # Asking user to type IP Address
                if user.lower() == 'q': # This will check if user type 'q'
                    separator()
                    break # Quitting
                ip: IP.ip_address = IP.IPv4Address(user) # This will convert the user variable into IPV4Address object
                int_ip = int(ip) # This will translate the ip address or ip variable into integer
                binary: bin = format(int_ip, "032b") # This will now translate the int_ip variable into binary
                separator()
                print(f"Result: {binary[0:8]}.{binary[8:16]}.{binary[16:24]}.{binary[24:32]}".center(terminal_width)) # This will now print the result of binary
                separator()
            except Exception:
                separator()
                print("Note: Please type a valid IP Address") # This will print if user didn't type a valid IP Address
                separator()

    def main():
        separator()
        print("--> IP Address/Numbers to Binary Translator <--".center(terminal_width))
        separator()
        while True:
            if menu() is None: # This wil check if menu function returns 
                break
    main() # Calling the main function because if not, you will see blank :)
if __name__ == "__main__":
    Binary_Converter()