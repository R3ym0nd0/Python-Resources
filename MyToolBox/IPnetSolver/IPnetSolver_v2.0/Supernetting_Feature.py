import ipaddress as IP

from typing import Union
from Helper_Function import separator
from Helper_Function import num_address
from Helper_Function import clear_screen
from colorama import Fore, init

# Initialize colorama to automatically reset color after each print
init(autoreset=True)


def Supernetting() -> None:
    # List of CIDR Notation
    def block_CIDR_notation() -> Union[list[IP.ip_network], None]:
        list_CIDR_notation: list[IP.ip_network] = [] # This will collect ip networks that user type
        while True:
            try:
                # Asking user to type a list of CIDR Notation
                user: str = input(f"{Fore.RED}[*] {Fore.WHITE}Type list of CIDR Notation (Type {Fore.RED}'done' {Fore.WHITE}to finish / Type {Fore.RED}'q' {Fore.WHITE}to quit): ").strip().lower()
                if user == "q": # This will check if user type 'q'
                    clear_screen()
                    return None  # Quitting
                elif user == "done": # This will check if user type 'done'
                    if not list_CIDR_notation: # This will check if user didn't type any CIDR Notation and then type 'done' immediately
                        separator()
                        print(f"{Fore.RED}!! {Fore.YELLOW}Please Type a CIDR Notation. {Fore.RED}!!")
                        separator()
                        list_CIDR_notation = [] # This will reset the list_CIDR_Notation if it have CIDR Notation inside       
                    elif len(list_CIDR_notation) <= 1: # This will check if the length of list_CIDR_notation variable is less than equal 1
                        separator()
                        print(f"{Fore.RED}!! {Fore.YELLOW}Please enter more than one CIDR notation. {Fore.RED}!!")
                        separator()
                        list_CIDR_notation = []
                    else:
                        separator()
                        return list_CIDR_notation
                else:
                    # Blocks of CIDR Notation
                    cidr = IP.ip_network(user) # This will translate the user input into ip network object, if it detects that user type ip network
                    for i in list_CIDR_notation:
                        if i == cidr: # This will check if i variable is equal to cidr to fix the repeated CIDR Notation
                            separator()
                            print(f"{Fore.RED}!! {Fore.YELLOW}Repeated CIDR Notation detected, please try again {Fore.RED}!!")
                            separator()
                            list_CIDR_notation = []
                            continue
                    else:
                        list_CIDR_notation.append(cidr) # The cidr variable will append in list_CIDR_Notation list
            except ValueError:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Please Type the IPv4 network {Fore.RED}!!") # This will print if user didn't type ip network
                separator()

    def sorted_result(list_CIDR_notation: list[IP.ip_network]) -> Union[list[IP.ip_network], int]:
        print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Blocks of CIDR Notation\n")
        sorted_cidr = list(sorted(list_CIDR_notation)) # This will sort the list_CIDR_Notation list starting from lowest to highest CIDR Notation
        list_of_num_addresses: list[int] = [] # This will collect the number of host in every CIDR Notation
        
        for num, subnet in enumerate(sorted_cidr):
            print(Fore.LIGHTCYAN_EX + f"Subnet {num + 1}: {Fore.RED + str(subnet)}") # This will print every CIDR Notation in sorted starting from lowest to highest CIDR Notation
            overall_num_addresses: int = subnet.num_addresses # The number of available host in every CIDR Notation
            list_of_num_addresses.append(overall_num_addresses) # This will append the host in list_of_num_addresses
        separator()
        return sum(list_of_num_addresses), sorted_cidr

    def check_list_subnets(subnets) -> Union[True, False]:

        if len(subnets) > 0 and len(subnets) & (len(subnets) -1) == 0:
            return True
        else:
            return False

    def check_rules(sorted_cidr: list[IP.ip_network]) -> Union[None, True]:
        print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Checking for errors...\n")

        for i in range(len(sorted_cidr) - 1):
            current_network: str = sorted_cidr[i]  # First CIDR block
            next_network: str = sorted_cidr[i + 1]  # Next CIDR block
            
            # Get the last IP of the current network
            current_last_ip: str = current_network.broadcast_address
            next_first_ip: str = next_network.network_address
            
            # Check if there is a gap
            if int(current_last_ip) +1 < int(next_first_ip):
                print(f"{Fore.LIGHTCYAN_EX}Note: {Fore.WHITE}Gap detected between {current_last_ip} and {next_first_ip}")
                return False  # Stop if a gap is detected
            
            # Check for overlap
            if current_network.overlaps(next_network):
                print(f"{Fore.LIGHTCYAN_EX}Note: {Fore.WHITE}Overlapping detected between {current_network} and {next_network}")
                return False  # Stop if an overlap is detected

        # If no gaps or overlaps were found
        print(f"{Fore.LIGHTCYAN_EX}Note: {Fore.WHITE}No gaps or overlaps detected")
        return True

    def prefix_length(list_of_num_addresses: list[int], sorted_cidr: list[IP.ip_network]) -> IP.ip_network:
        # Calculate the number of required addresses (including network and broadcast)
        required_addresses: int = list_of_num_addresses -2
        # Find the smallest power of 2 that is greater than or equal to the required addresses
        power: int = 0
        while (2 ** power) < required_addresses:  # While the 2 ^ power(start from 0) is less than required_addresses(for example of host is 62)
            power += 1  # It will increment until power variable or bits needed is enough. For example: 2 ^ 6(power) = 64 Host
        
        # Calculate the prefix length
        new_prefix: int = 32 - power # subtracting the power variable into 32. For example: 32 - 6 = 26. That means the new prefix length is /26
        first_address: IP.ip_network =  sorted_cidr[0] # This will take the first address in sorted_cidr list
        net_address = first_address.network_address # This will take the network address in first address variable(ip network)
        supernet: str = f"{net_address}/{new_prefix}" # This will create a new ip network
        return IP.ip_network(supernet, strict=False), new_prefix    
    
    def canSupernet(sorted_cidr, supernet) -> None:

        cidr_netAddress = IP.ip_network(sorted_cidr[0])
        return supernet.network_address == cidr_netAddress.network_address

    def supernet_info(supernet: IP.ip_network) -> None:
        print(f"\n{Fore.LIGHTCYAN_EX}The Supernet is: {Fore.LIGHTGREEN_EX + str(supernet)}") # This will print the supernet result
        separator()

        while True:
            user = input(f"{Fore.RED}[*] {Fore.WHITE}Do you want to see detailed information about the result ({Fore.RED}Y/N{Fore.WHITE}): ").strip().lower() # Asking user if he wants to see the supernet info
            if user == "y":
                separator()
                get_net_broad: list[IP.ip_address] = list(supernet.hosts()) # This will get all of the IP address of the IP network
                print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Result:\n")
                print(Fore.LIGHTCYAN_EX + f"Network: {Fore.RED + str(supernet)}\n")
                print(f"   Network Address: {Fore.LIGHTGREEN_EX + str(supernet.network_address)}")
                print(f"   Broadcast Address: {Fore.LIGHTGREEN_EX + str(supernet.broadcast_address)}")
                print(f"   Subnet Mask: {Fore.LIGHTGREEN_EX + str(supernet.netmask)}")
                print(f"   Prefix Length: /{Fore.LIGHTGREEN_EX + str(supernet.prefixlen)}")
                print(f"   Host: {Fore.LIGHTGREEN_EX + str(num_address(supernet))}")
                print(f"   Usable IP range: {Fore.LIGHTGREEN_EX + str(get_net_broad[0])} TO {str(get_net_broad[-1])}")
                separator()
                return None # This will go back from the start
            elif user == "n":
                separator()
                return None # This will go back from the start
            else:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Invalid Choice, please try again {Fore.RED}!!") # This will print if user didn't type valid choices
                separator()

    def start_program() -> None:
        separator()
        print(f"{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}Supernetting {Fore.MAGENTA}[*]\n")
        while True:
            list_CIDR_notation: list[IP.ip_network] = block_CIDR_notation()
            if list_CIDR_notation is None: # This wil check if block_CIDR_notation function returns None
                break
            elif list_CIDR_notation:
                list_of_num_addresses,  sorted_cidr = sorted_result(list_CIDR_notation)
                # Error Checking
                if check_list_subnets(sorted_cidr) is False:
                    print(f"{Fore.LIGHTCYAN_EX}Note: {Fore.WHITE}Invalid List of Subnets: {Fore.YELLOW + str(len(sorted_cidr))}")
                    separator()
                    continue
                elif check_list_subnets(sorted_cidr) is True:
                    if check_rules(sorted_cidr) is False:
                        separator()
                        continue
                    else:
                        supernet, new_prefix = prefix_length(list_of_num_addresses,  sorted_cidr)
                        if canSupernet(sorted_cidr, supernet) is False:
                            print(f"{Fore.LIGHTCYAN_EX}Note: {Fore.WHITE}Invalid subnet block detected")
                            separator()
                            continue

                        if supernet_info(supernet) is None:
                            continue

    def main() -> None:
        start_program() # Calling the start_program function
    main()

if __name__ == "__main__":
    Supernetting()
