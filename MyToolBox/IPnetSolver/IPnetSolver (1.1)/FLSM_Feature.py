import ipaddress as IP
import os

def FLSM():

    def ip_input():
        while True:
            try:
                # Asking user to type CIDR Notation
                IP_Address = input("--> Type CIDR notation (e.g., 192.168.43.0/24). Type 'q' to quit: ").strip()
                if IP_Address.lower() == "q": # This will check if user type 'q' then it quits
                    return None # Quitting
                else:
                    ip = IP.ip_network(IP_Address, strict=False) # Translating the IP_Address variable into ip_network object. strict=False means that the ip_network is not limited to juts network address; it can also include broadcast addresses, host addresses, etc. For example, '192.168.43.123/24' is a valid host address within the '192.168.43.0/24' network.
                    # Checking if user type CIDR Notation that /32 prefix length 
                    if ip.prefixlen == 32:
                        print(f"Note: The {ip} is a single IP address; there is no reason to subnet it\n") # This will print if user type CIDR Notation that prefix length is /32
                        continue # This will go back to the start of the loop
                    separator()
                    # Printing the Network Range in Host
                    print(f"Network Range: {ip.network_address} TO {ip.broadcast_address}") # This will print the range of CIDR Notation that user type
                    print(f"Host: {ip.num_addresses}") # This will print the number of host of CIDR Notation
                    separator()
                    return ip
            except ValueError:
                separator()
                print("Note: Please type the IPv4 network") # This will print if user didn't type IPV4 Network
                separator()

    def calculate_prefix_length(ip):
        def calculating_bits_needed(networks):
            # Calculate the number of bits needed to create the requested number of subnets.
            bits = 0 # Initialize the bit counter
            while (1 << bits) < networks:  # 1 << bits is equivalent to 2**bits
                bits += 1 # Increment the bits counter to find the minimum required bits
            return bits  # Return the total number of bits needed for the specified number of subnets
        
        while True:
            try:
                # Asking user how many subnet it needs to divide
                num_subnet = input(f"--> Please enter the number of subnets (1 to {ip.num_addresses}). Type 'q' to quit: ").strip().lower()
                # Options
                if num_subnet == 'q': # This will check if user type 'q' then it quits
                    return None # Quitting
                
                int_num_subnet = int(num_subnet) # Translating into Integer
                if int_num_subnet < 1: # This will check if user type less than 1 for example: 0, -1, -100
                    separator()
                    print("Note: Only 1 and above")
                    separator()
                    continue

                max_subnets = 2**(32 - ip.prefixlen) # 'ip.perfixlen' means for example the user type 192.168.43.0/24, ip.prefixlen will only take the prefix length 24
                if int_num_subnet > max_subnets: # This will check if user input is greater than max_subnets, for example: if max_subnets result is 4, then int_num_subnet needs to be 4 and below
                    separator()
                    print(f"Note: The number of requested subnets exceeds the maximum possible for this network ({max_subnets}). Please try again.")
                    separator()
                    continue
                
                bits_needed = calculating_bits_needed(int_num_subnet) # Calling the 'calculating_bits_needed(int_num_subnet)' function
                return bits_needed 
            except ValueError:
                separator()
                print(f"Note: Please type how many networks you want to divide into") # This will print if user type words
                separator()

    def new_prefix_length(ip,  bits_needed):
        prefix = ip.prefixlen + bits_needed # The result oft his is the new prefix length of CIDR Notation
        if prefix > 32: # This will check if the result of prefix variable is greater than 32
            raise ValueError("The resulting prefix length exceeds /32. Please try again.")
        return prefix

    def result(ip, prefix):
        separator()
        details_list = [] # This will collect every subnet info
        #Result of user wants to divide
        for i, details in enumerate(ip.subnets(new_prefix=prefix)): # ip.subnets automatically divides the CIDR Notation into subnets, and the 'new_prefix=prefix' means the 'prefix'variable is the new prefix length, so it creates subnet based on the new prefix_length
            # This will print Network, Broadcast Address, Subnet Mask, New Prefix Length, # of Available Host, and IP Range
            print(f"\n---Subnet {i +1}: {details}---")
            print(f"Network Address: {details.network_address}")
            print(f"Broadcast Address: {details.broadcast_address}")
            print(f"Subnet Mask: {details.netmask}")
            print(f"Prefix Length: /{details.prefixlen}")
            print(f"Number of Available Host: {num_address(details)}")
            print(f"IP Range: {details.network_address} TO {details.broadcast_address}")
            details_list.append(details) # every subnet will be add in details_list = []
        separator()
        return details_list
    
    def ask_to_convert_to_binary(ip, prefix):     
        while True:
            # Asking user to Translate Network Address, Broadcast Address and Subnet Mask into binary
            user = input("--> Do you want to convert the Network Address, Broadcast Address, and Subnet Mask into binary? (Y/N only) ").strip()
            if user.lower() == "y":
                convert_to_binary(ip, prefix)
                break # It break after showing the result
            elif user.lower() == "n":
                separator()
                break # Quitting
            else:
                separator()
                print("Please enter Y or N only") # This will print if user didn't type 'Y' or 'N'
                separator()

    def convert_to_binary(ip, prefix):
        separator()
        #Binary Translator
        for number, result in enumerate(ip.subnets(new_prefix=prefix)):
            # Basically, this will translate the network, broadcast address, and subnet mask into binary
            binary_network_address = '.'.join(f"{int(octet):08b}" for octet in result.network_address.exploded.split('.'))
            binary_broadcast_address =  '.'.join(f"{int(octet):08b}" for octet in result.broadcast_address.exploded.split('.'))
            binary_subnetmask = '.'.join(f"{int(octet):08b}" for octet in result.netmask.exploded.split('.'))

            # This will print the result in binary
            print("")
            print(f"---Subnet {number+1}: {result}---")
            print(f"Network Address: {result.network_address} translate into {binary_network_address}")
            print(f"Broadcast Address: {result.broadcast_address} translate into {binary_broadcast_address}")
            print(f"Subnet Mask: {result.netmask} translate into {binary_subnetmask}")
            print(f"Prefix Length: /{result.prefixlen}")
            print(f"Host: {num_address(result)}")
        separator()
    
    def asking_to_subnet_each_subnet(details_list): 
        while True:
            # Asking user if he wants to subnet every subnet of the result
            asking_to_subnet_a_subnet = input("\n--> Do you want to subnet each subnet in your result? (Y/N): ").strip().lower()
            if asking_to_subnet_a_subnet == "y":
               calling_function(details_list) # This function will call if user type 'y'
            elif asking_to_subnet_a_subnet == "n":
                separator()
                return None # Quitting
            else:
                separator()
                print("Note: Y or N only, Please try again") # This will print if user didn't type 'Y' or 'N'
                separator()

    def choose_available_subnet(details_list):
            terminal_width = os.get_terminal_size().columns  
            while True:
                try:
                    # This will list all of available subnets base on the result
                    print("Available Subnets:\n")
                    for nums, every_subnet in enumerate(details_list):
                        print(f"Subnet {nums +1}: {every_subnet}") # This will print all the subnets that details_list variable collects
                    print(f"\nHost: {every_subnet.num_addresses} Host") # This will print the number of host available
                    separator()

                    # Asking user to chose subnet
                    choosing_user = input(f"\n--> Choose a subnet that you want to divide (1 to {len(details_list)}). Type 'q' to quit: ").strip()
                    if choosing_user.lower() == "q":
                        separator()
                        return None # Quitting
                    elif int(choosing_user) < 1 or int(choosing_user) > len(details_list): # This will print if user is less or greater than details_list length, for example if the length of details_list is only 4, it needs to be 1 to 4
                        separator()
                        print(f"Note: Please choose a number between 1 and {len(details_list)}")
                        separator()
                    else:
                        for num_subnets, length in enumerate(details_list):
                            if int(choosing_user) == num_subnets +1:
                                if length.prefixlen == 32: # This will check if the prefix length is /32
                                    separator()
                                    print(f"Note: The {length} is a single IP address; there is no reason to subnet it\n")
                                    continue
                                separator()
                                # This is user subnet chose
                                print(f"--> You Chose Subnet {num_subnets +1}: {length} <--".center(terminal_width)) # This will print the subnet that user chose
                                separator()
                                return length
                except ValueError:
                    separator()
                    print(f"Note: Please type a number between 1 and {len(details_list)}, or type 'q' to go back.")
                    separator()

    def calling_function(details_list):
            while True:
                separator()
                length = choose_available_subnet(details_list)
                if length is None: # This will check if length returns None
                    break # Quitting
                while True:
                    bits_needed = calculate_prefix_length(length)
                    if bits_needed is None:
                        break # Quitting
                    elif not bits_needed:
                        return length # Thsi will back to the choosing_subnet(details_list) function
                    prefix = new_prefix_length(length, bits_needed)
                    # Asking if user wants to translate the result into binary
                    result(length, prefix)
                    ask_to_convert_to_binary(length, prefix) 
                    break
                
    def num_address(details):
            #Num Addressses
            if details.num_addresses -2 < 0: # This will check if details.num_addresses or basically the number of host -2, is less than 0
                host = "No Available Host"
            else:
                host = details.num_addresses -2 # subtracting 2 the number of host for the network and broadcast addresses
                if host == 0: # Thi will check if number of host -2 is 0
                   host = "No Available Host" 
            return host

    def separator():
            terminal_width = os.get_terminal_size().columns
            separator = "=" * terminal_width
            print(separator)

    def main_function():
        while True:
            ip = ip_input()
            if ip is None: # This wil check if ip_input function returns None
                break # Quitting
            while True:       
                bits_needed = calculate_prefix_length(ip)
                if bits_needed is None: # This wil check if networks function returns None
                    break # Quitting
                prefix = new_prefix_length(ip, bits_needed)
                details_list = result(ip, prefix)
                ask_to_convert_to_binary(ip, prefix)
                if asking_to_subnet_each_subnet(details_list) is None: # This wil check if asking_subneting_every_subnet function returns None
                    break # Quitting

    main_function()

if __name__ == "__main__":
    FLSM()