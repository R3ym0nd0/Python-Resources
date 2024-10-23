import ipaddress as IP
import os

def Binary_Translator():
    def menu():
        while True:
            separator()
            print("Choices:")
            print("[1] Decimal Number to Binary")
            print("[2] IP Address to Binary\n")
            user = input("--> Choose a number (Type 'q' to quit): ").strip().lower()
            if user == "q":
                return None #Quitting
            elif user == "1":
                decimal_numbers()
            elif user == "2":
                ip_address()
            else:
                print("Invalid Choice")

    def decimal_numbers():
        separator()
        print("--> You chose Decimal Number to Binary <--\n")
        while True:
            try:
                user = input("--> Type Decimal Numbers (Type 'q' to quit): ").strip()
                if user == "q":
                    break #Quitting
                num = int(user)
                binary = bin(num).split("0b")
                print(f"Result: {binary[1]}")
            except ValueError:
                print("Type a Decimal Number")
    
    def ip_address():
        separator()
        print("--> You chose IP Address to Binary <--\n")
        while True:
            try:
                user = input("--> Type IP Address (Type 'q' to quit): ").strip()
                if user.lower() == 'q':
                    break
                ip = IP.IPv4Address(user)
                int_ip = int(ip)
                binary = format(int_ip, "032b")
                print(f"Result: {binary[0:8]}.{binary[8:16]}.{binary[16:24]}.{binary[24:32]}")
            except Exception:
                print("Type a valid IP Address")

    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)

    def main():
        while True:
            if menu()is None:
                break
    main()
if __name__ == "__main__":
    Binary_Translator()