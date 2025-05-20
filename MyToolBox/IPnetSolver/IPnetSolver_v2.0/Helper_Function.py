import ipaddress as IP
import os
from colorama import Fore, init

# Initialize colorama to automatically reset color after each print
init(autoreset=True)

def ip_input() -> IP.ip_network:
        while True:
            try:
                # Asking user to type CIDR Notation
                IP_Address: str = input(f"{Fore.RED}[*] {Fore.WHITE}Type CIDR notation (e.g., {Fore.YELLOW}192.168.43.0/24{Fore.WHITE}). Type {Fore.RED}'q' {Fore.WHITE}to quit: ").strip()
                if IP_Address.lower() == "q": # This will check if user type 'q' then it quits
                    clear_screen()
                    return None # Quitting
                else:
                    ip = IP.ip_network(IP_Address, strict=False) # Translating the IP_Address variable into ip_network object. strict=False means that the ip_network is not limited to juts network address; it can also include broadcast addresses, host addresses, etc. For example, '192.168.43.123/24' is a valid host address within the '192.168.43.0/24' network.
                    # Checking if user type CIDR Notation that /32 prefix length 
                    if ip.prefixlen == 32:
                        separator()
                        print(f"{Fore.RED}!! {Fore.YELLOW}The {ip} is a single IP address; there is no reason to subnet it {Fore.RED}!!") # This will print if user type CIDR Notation that prefix length is /32
                        separator()
                        continue # This will go back to the start of the loop
                    separator()
                    # Printing the Network Range in Host
                    print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}CIDR Information:\n")
                    print(f"{Fore.LIGHTGREEN_EX}Network Range: {Fore.WHITE}{str(ip.network_address)} TO {Fore.WHITE}{str(ip.broadcast_address)}") # This will print the range of CIDR Notation that user type
                    print(f"{Fore.LIGHTGREEN_EX}Host: {Fore.WHITE}{str(ip.num_addresses -2)}") # This will print the number of host of CIDR Notation
                    separator()
                    return ip
            except ValueError:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Please type the IPv4 network {Fore.RED}!!") # This will print if user didn't type IPV4 Network
                separator()

def num_address(details: int) -> int:
            #Num Addressses
            if details.num_addresses -2 < 0: # This will check if details.num_addresses or basically the number of host -2, is less than 0
                host = "No Available Host"
            else:
                host = details.num_addresses -2 # subtracting 2 the number of host for the network and broadcast addresses
                if host == 0: # Thi will check if number of host -2 is 0
                   host = "No Available Host" 
            return host
 
def clear_screen() -> None:
    # Check if the operating system is Windows or Unix-based
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Unix/MacOS

# This function is for design purposes
def separator() -> None:
    terminal_width: int = os.get_terminal_size().columns
    separator: int = Fore.BLUE + "=" * terminal_width
    print(separator)