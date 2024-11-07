import ipaddress as IP
import os

def VLSM():

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
                    print(f"Host: {ip.num_addresses}\n") # This will print the number of host of CIDR Notation
                    return ip
            except ValueError:
                separator()
                print("Note: Please type the IPv4 network") # This will print if user didn't type IPV4 Network
                separator()

    def asking_network_host(ip):
        print(f"Note: You can only use {ip.num_addresses - 2} hosts.")
        separator()
        list_host = [] # This will collect all of the number of host that user type
        while True:
            try:
                # Asking user to type list of host
                asking_host = input("--> Type network host (Type 'done' to finish/Type 'q' to quit FLSM/Type 'b' to back): ").strip().lower()
                if asking_host == "done": # This will check if user type 'done'
                    if not list_host: # This will check if list_host variable don't have inside list of host
                        separator()
                        print("Note: Please Type a number of host") # If user type done without typing host, it will see this
                        separator()
                        continue
                    host = sum(list_host) # This will sum the overall list of numbers in list_host variable
                    if host > ip.num_addresses -2: # This will check if the overall result of host variable is greater than ip.num_addresses -2
                        separator()
                        print(f"Note: The number of hosts exceed the maximum number of usable addresses for this network.")
                        separator()
                        list_host = [] # This will reset the list_host or user list of host
                        continue
                    else:        
                        return sorted(list(map(int, list_host)), reverse=True)  # Sort in descending order and translate that list into integer
                elif asking_host.lower() == "b":
                    separator()
                    return None # Back to the previous question
                elif asking_host.lower() == "q":
                    return False # Quitting
                
                int_asking_host = int(asking_host) # It translate the 'asking_host' variable into integer
                if int_asking_host and int_asking_host > 0: # This will check if 'int_asking_host' variable is 1 and above
                    list_host.append(int_asking_host) # This will append into list_host
                else:
                    separator()
                    print("Note: Host size must be a positive number or Host size must be a number.") # This will print if user type negative numbers or words
                    separator()
            except ValueError:
                separator()
                print("Note: Please enter a whole number") # This will print if user type words
                separator()

    def calculating_prefix_length_host(list_host):
        list_of_ip_range = [] # This will collect the new prefix length of every host

        for host in list_host:
            bits_needs = 0
            while (2 ** bits_needs) < host: # While the 2 ^ bits_needs(start from 0) is less than host(for example of host is 62)
                bits_needs += 1 # It will increment until bits_needs is enough. For example: 2 ^ 6(bits_needs) = 64 Host
            new_prefix = 32 - bits_needs # subtracting the bits_needs into 32. For example: 32 - 6 = 26. That means the new prefix length is /26
            list_of_ip_range.append(new_prefix) # This will append in list_of_ip_range variable
        return list_of_ip_range
    
    def VLSM_result(list_of_ip_range, ip):
        terminal_width = os.get_terminal_size().columns
        separator()
        print(f"--> CIDR Notation: {ip} <--".center(terminal_width)) # This will print the original IP Network that user input at the start
        separator()
        network = IP.ip_network(ip, strict=False)
        subnets = sorted(list_of_ip_range)  # This will sort subnets in ascending order
        start_ip = network.network_address # The start of the IP Network. For example: 192.168.43.0/24, the start is 192.168.43.0
        used_networks = [] # This will collect every CIDR Notation
        
        for subnet in list_of_ip_range:
            while True:
                ip_network = IP.ip_network(f"{start_ip}/{subnet}", strict=False) # Translating the combine (start_ip and subnet variable) into IP Network Object
                overlaps = False
                for existing in used_networks:
                    if ip_network.overlaps(existing): # This will check if every CIDR Notation overlaps
                        overlaps = True
                        break
                if not overlaps:
                    break
                # Move to the next start_ip if overlap occurs
                start_ip = IP.ip_address(int(start_ip) + ip_network.num_addresses)
            used_networks.append(ip_network) # This will append in used_networks variable

            # This will print the information of every subnets
            print(f"\n---Network {subnets.index(subnet) + 1}: {ip_network}---")
            print(f"Network Address: {ip_network.network_address}")
            print(f"Broadcast Address: {ip_network.broadcast_address}")
            print(f"Subnet Mask: {ip_network.netmask}")
            print(f"Prefix Length: /{ip_network.prefixlen}")
            print(f"Host: {num_address(ip_network)}")
            print(f"Number of Usable IP: {ip_network.network_address + 1} TO {ip_network.broadcast_address - 1}")
            
            # Move start_ip to the next available address after the current subnet
            start_ip = IP.ip_address(int(ip_network.broadcast_address) +1)
        separator()
        return used_networks

    def ask_to_convert_to_binary(used_networks):     
        while True:
            # Asking user to Translate Network Address, Broadcast Address and Subnet Mask into binary
            user = input("--> Do you want to convert the Network Address, Broadcast Address, and Subnet Mask into binary? (Y/N only) ").strip()
            if user.lower() == "y":
                convert_to_binary(used_networks)
                break # It break after showing the result
            elif user.lower() == "n":
                break # Quitting
            else:
                separator()
                print("Please enter Y or N only") # This will print if user didn't type 'Y' or 'N'
                separator()

    def convert_to_binary(used_networks):
        separator()
        for number, result in enumerate(used_networks):
            # Basically, this will translate the network, broadcast address, and subnet mask into binary
            binary_network_address = '.'.join(f"{int(octet):08b}" for octet in result.network_address.exploded.split('.'))
            binary_broadcast_address =  '.'.join(f"{int(octet):08b}" for octet in result.broadcast_address.exploded.split('.'))
            binary_subnetmask = '.'.join(f"{int(octet):08b}" for octet in result.netmask.exploded.split('.'))

            # This will print the result in binary
            print(f"\n---Subnet {number+1}: {result}---")
            print(f"Network Address: {binary_network_address}")
            print(f"Broadcast Address: {binary_broadcast_address}")
            print(f"Subnet Mask: {binary_subnetmask}")
            print(f"Prefix Length: /{result.prefixlen}")
            print(f"Host: {num_address(result)}")
        separator()
               
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
            # Asking user to type IP Address Range
            ip = ip_input()
            if not ip:
                break
            elif ip is None: # This wil check if ip_input function returns None
                break
            while True:
                # Asking user to type network host
                list_host = asking_network_host(ip)
                if list_host is None: # This wil check if asking_network_host function returns None
                    break
                elif not list_host:
                    return ip
                list_of_ip_range = calculating_prefix_length_host(list_host)
                used_networks = VLSM_result(list_of_ip_range, ip)
                ask_to_convert_to_binary(used_networks)
                break
    main_function()

if __name__ == "__main__":
    VLSM()