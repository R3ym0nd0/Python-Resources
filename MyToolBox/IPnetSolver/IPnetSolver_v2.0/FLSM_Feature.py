import ipaddress as IP

from typing import Union
from Helper_Function import ip_input
from Helper_Function import separator
from Helper_Function import num_address
from colorama import Fore, init

# Initialize colorama to automatically reset color after each print
init(autoreset=True)

def FLSM() -> None:

    def calculate_prefix_length(ip: str) -> int:
        def calculating_bits_needed(networks: int):
            # Calculate the number of bits needed to create the requested number of subnets.
            bits: int = 0 # Initialize the bit counter
            while (1 << bits) < networks:  # 1 << bits is equivalent to 2**bits
                bits += 1 # Increment the bits counter to find the minimum required bits
            return bits  # Return the total number of bits needed for the specified number of subnets
        
        while True:
            try:
                # Asking user how many subnet it needs to divide
                num_subnet: int = input(f"{Fore.RED}[*] {Fore.WHITE}Please enter the number of subnets ({Fore.RED}1 to {ip.num_addresses}{Fore.WHITE}). Type {Fore.RED}'q' {Fore.WHITE}to quit: ").strip().lower()
                # Options
                if num_subnet == 'q': # This will check if user type 'q' then it quits
                    return None # Quitting
                
                int_num_subnet: int = int(num_subnet) # Translating into Integer
                if int_num_subnet < 1: # This will check if user type less than 1 for example: 0, -1, -100
                    separator()
                    print(f"{Fore.RED}!! {Fore.YELLOW}Only 1 and above {Fore.RED}!!")
                    separator()
                    continue

                max_subnets: int = 2**(32 - ip.prefixlen) # 'ip.perfixlen' means for example the user type 192.168.43.0/24, ip.prefixlen will only take the prefix length 24
                if int_num_subnet > max_subnets: # This will check if user input is greater than max_subnets, for example: if max_subnets result is 4, then int_num_subnet needs to be 4 and below
                    separator()
                    print(f"{Fore.RED}!! {Fore.YELLOW}The number of requested subnets exceeds the maximum possible for this network ({max_subnets}). Please try again. {Fore.RED}!!")
                    separator()
                    continue
                
                bits_needed = calculating_bits_needed(int_num_subnet) # Calling the 'calculating_bits_needed(int_num_subnet)' function
                return bits_needed 
            except ValueError:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Please type how many networks you want to divide into {Fore.RED}!!") # This will print if user type words
                separator()

    def new_prefix_length(ip: str,  bits_needed: int) -> int:
            prefix: int = ip.prefixlen + bits_needed # The result oft his is the new prefix length of CIDR Notation
            if prefix > 32: # This will check if the result of prefix variable is greater than 32
                raise ValueError(f"{Fore.RED}!! {Fore.YELLOW}The resulting prefix length exceeds /32. Please try again. {Fore.RED}!!")
            return prefix

    def result(ip: str, prefix: int) -> list[IP.ip_network]:
            separator()
            details_list: list[IP.ip_network] = [] # This will collect every subnet info
            #Result of user wants to divide
            print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Result:")
            for i, details in enumerate(ip.subnets(new_prefix=prefix)): # ip.subnets automatically divides the CIDR Notation into subnets, and the 'new_prefix=prefix' means the 'prefix'variable is the new prefix length, so it creates subnet based on the new prefix_length
                # This will print Network, Broadcast Address, Subnet Mask, New Prefix Length, # of Available Host, and IP Range
                get_net_broad: list[IP.ip_address] = list(details.hosts())  # This will get all of the IP address of the IP network
                print(Fore.LIGHTCYAN_EX + f"\nSubnet {i +1}: {Fore.RED + str(details)}\n")
                print(f"   Network Address: {Fore.LIGHTGREEN_EX + str(details.network_address)}")
                print(f"   Broadcast Address: {Fore.LIGHTGREEN_EX + str(details.broadcast_address)}")
                print(f"   Subnet Mask: {Fore.LIGHTGREEN_EX + str(details.netmask)}")
                print(f"   Prefix Length: /{Fore.LIGHTGREEN_EX + str(details.prefixlen)}")
                print(f"   Number of Available Host: {Fore.LIGHTGREEN_EX + str(num_address(details))}")
                print(f"   Usable IP range: {Fore.LIGHTGREEN_EX + str(get_net_broad[0])} TO {str(get_net_broad[-1])}")
                details_list.append(details) # every subnet will be add in details_list = []
            separator()
            return details_list
    
    def asking_to_subnet_each_subnet(details_list: list[IP.ip_network]) -> None: 
        while True:
            # Asking user if he wants to subnet every subnet of the result
            asking_to_subnet_a_subnet: str = input(f"{Fore.RED}[*] {Fore.WHITE}Do you want to subnet each subnet in your result? ({Fore.RED}Y/N{Fore.WHITE}): ").strip().lower()
            if asking_to_subnet_a_subnet == "y":
               separator()
               calling_function(details_list) # This function will call if user type 'y'
            elif asking_to_subnet_a_subnet == "n":
                separator()
                return None # Quitting
            else:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Y or N only, Please try again {Fore.RED}!!") # This will print if user didn't type 'Y' or 'N'
                separator()

    def choose_available_subnet(details_list: list[IP.ip_network]) -> Union[IP.ip_network, None]:
        while True:
            try:
                # This will list all of available subnets base on the result
                print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Available Subnets:\n")
                for nums, every_subnet in enumerate(details_list):
                    print(Fore.LIGHTCYAN_EX + f"Subnet {nums +1}: {Fore.RED + str(every_subnet)}") # This will print all the subnets that details_list variable collects
                print(f"\n{Fore.LIGHTCYAN_EX}Host: {Fore.LIGHTGREEN_EX + str(every_subnet.num_addresses)}") # This will print the number of host available
                separator()

                # Asking user to chose subnet
                choosing_user: int = input(f"{Fore.RED}[*] {Fore.WHITE}Choose a subnet that you want to divide ({Fore.RED}1 to {len(details_list)}{Fore.WHITE}). Type {Fore.RED}'q' {Fore.WHITE}to quit: ").strip()
                if choosing_user.lower() == "q":
                    separator()
                    return None # Quitting
                elif int(choosing_user) < 1 or int(choosing_user) > len(details_list): # This will print if user is less or greater than details_list length, for example if the length of details_list is only 4, it needs to be 1 to 4
                    separator()
                    print(f"{Fore.RED}!! {Fore.YELLOW}Please choose a number between 1 and {len(details_list)} {Fore.RED}!!")
                    separator()
                else:
                    for num_subnets, length in enumerate(details_list):
                        if int(choosing_user) == num_subnets +1:
                            if length.prefixlen == 32: # This will check if the prefix length is /32
                                separator()
                                print(f"{Fore.RED}!! The {length} is a single IP address; there is no reason to subnet it {Fore.RED}!!\n")
                                continue
                            separator()
                            # This is user subnet chose
                            print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}You Chose {Fore.LIGHTCYAN_EX}Subnet {num_subnets +1}: {Fore.RED + str(length)}\n") # This will print the subnet that user chose
                            print(Fore.LIGHTGREEN_EX + f"Network Range: {Fore.WHITE + str(length.network_address)} TO {Fore.WHITE + str(length.broadcast_address)}")
                            print(Fore.LIGHTGREEN_EX + f"Host: {Fore.WHITE + str(length.num_addresses -2)}")
                            separator()
                            return length
            except ValueError:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Please type a number between 1 and {len(details_list)}, or type 'q' to go back. {Fore.RED}!!")
                separator()

    def ask_to_convert_to_binary(ip: str, prefix: int) -> None:     
        while True:
            # Asking user to Translate Network Address, Broadcast Address and Subnet Mask into binary
            user: str = input(f"{Fore.RED}[*] {Fore.WHITE}Do you want to convert the {Fore.LIGHTGREEN_EX}Network Address{Fore.WHITE}, {Fore.LIGHTGREEN_EX}Broadcast Address{Fore.WHITE}, and {Fore.LIGHTGREEN_EX}Subnet Mask {Fore.WHITE}into binary ({Fore.RED}Y/N only{Fore.WHITE}): ").strip().lower()
            if user == "y":
                convert_to_binary(ip, prefix)
                break # It break after showing the result
            elif user == "n":
                separator()
                break # Quitting
            else:
                separator()
                print(f"{Fore.RED}!! {Fore.YELLOW}Please enter Y or N only {Fore.RED}!!") # This will print if user didn't type 'Y' or 'N'
                separator()

    def convert_to_binary(ip: str, prefix: int) -> None:
            separator()
            #Binary Translator
            print(f"{Fore.MAGENTA}[*] {Fore.LIGHTGREEN_EX}Result:")
            for number, result in enumerate(ip.subnets(new_prefix=prefix)):
                # Basically, this will translate the network, broadcast address, and subnet mask into binary
                binary_network_address = '.'.join(f"{int(octet):08b}" for octet in result.network_address.exploded.split('.'))
                binary_broadcast_address =  '.'.join(f"{int(octet):08b}" for octet in result.broadcast_address.exploded.split('.'))
                binary_subnetmask = '.'.join(f"{int(octet):08b}" for octet in result.netmask.exploded.split('.'))

                # This will print the result in binary
                print("")
                print(Fore.LIGHTCYAN_EX + f"Subnet {number+1}: {Fore.RED + str(result)}\n")
                print(f"   Network Address: {Fore.LIGHTGREEN_EX + str(binary_network_address)}")
                print(f"   Broadcast Address: {Fore.LIGHTGREEN_EX + str(binary_broadcast_address)}")
                print(f"   Subnet Mask: {Fore.LIGHTGREEN_EX + str(binary_subnetmask)}")
                print(f"   Prefix Length: /{Fore.LIGHTGREEN_EX + str(result.prefixlen)}")
                print(f"   Host: {Fore.LIGHTGREEN_EX + str(num_address(result))}")
            separator()

    def calling_function(details_list: list[IP.ip_network]) -> Union[None, IP.ip_network]:
            while True:
                length: IP.ip_network = choose_available_subnet(details_list)
                if length is None: # This will check if length returns None
                    break # Quitting
                while True:
                    bits_needed: int = calculate_prefix_length(length)
                    if bits_needed is None:
                        break # Quitting
                    elif not bits_needed:
                        return length # Thsi will back to the choosing_subnet(details_list) function
                    prefix: int = new_prefix_length(length, bits_needed)
                    # Asking if user wants to translate the result into binary
                    result(length, prefix)
                    ask_to_convert_to_binary(length, prefix) 
                    break

    def main_function() -> None:
        separator()
        print(f"{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}Fixed-Length Subnet Masking(FLSM) {Fore.MAGENTA}[*]\n")
        while True:
            ip: str = ip_input()
            if ip is None: # This wil check if ip_input function returns None
                break # Quitting
            while True:       
                bits_needed: int = calculate_prefix_length(ip)
                if bits_needed is None: # This wil check if networks function returns None
                    break # Quitting
                prefix: int = new_prefix_length(ip, bits_needed)
                details_list: list[IP.ip_network] = result(ip, prefix)
                ask_to_convert_to_binary(ip, prefix)
                if asking_to_subnet_each_subnet(details_list) is None: # This wil check if asking_subneting_every_subnet function returns None
                    break # Quitting

    main_function() # Calling the main_function to start the flow

if __name__ == "__main__":
    FLSM()