import ipaddress as IP
import os

def VLSM():
    #Variable-Length Subnet Masking(VLSM)
    def ip_input():
        while True:
            try:
                #Asking user to type CIDR Notation
                IP_Address = input("--> Type CIDR Notation (eg..192.168.43.0/24 (Type 'q' to quit): ").strip()
                if IP_Address.lower() == "q": #Quitting
                    separator()
                    return None
                else:
                    ip = IP.ip_network(IP_Address, strict=False)
                    #Checking if user type CIDR Notation that /32 prefix length 
                    if ip.prefixlen == 32:
                        print(f"Note: The {ip} is single IP Address, there no reason to subnet it.\n")
                        continue
                    separator()
                    print(f"Network Range: {ip.network_address} TO {ip.broadcast_address}")
                    print(f"Host: {ip.num_addresses}\n")
                    return ip
            except ValueError:
                print("Type IPv4 Network. Please try again.")

    def asking_network_host(ip):
        print(f"Note: you can only do {ip.num_addresses -2} Host\n")
        list_host = []
        while True:
            try:
                #Asking user to type list of host
                asking_host = input("--> Type network host (Type 'done' to finish/Type 'q' to quit FLSM/Type 'b' to back): ").strip().lower()
                if asking_host == "done":
                    if not list_host:
                        print("Please Type a number of host") #If user type done without typing host, it will see this
                        continue
                    host = sum(list_host)
                    if host > ip.num_addresses -2:
                        print(f"The number of hosts exceed the maximum number of usable addresses for this network.")
                        list_host = [] #This will reset the list_host or user list of host
                        continue
                    else:        
                        return sorted(list(map(int, list_host)), reverse=True)  # Sort in descending order and translate that list into integer
                elif asking_host.lower() == "b":
                    return None #Back to the previous question
                elif asking_host.lower() == "q":
                    return False #Quitting
                
                int_asking_host = int(asking_host) #Asking host translate into integer
                if int_asking_host and int_asking_host > 0:
                    list_host.append(int_asking_host) #This will append into list_host
                else:
                    print("Host size must be a positive number or Host size must be a number.")
            except ValueError:
                print("Please Type Number :)")
    
    def calculating_prefix_length_host(list_host):
        list_of_ip_range = []
        #Translating a host into CIDR Notation
        for host in list_host:
            bits_needs = 0
            while (2 ** bits_needs) < (host +2):
                bits_needs += 1
            new_prefix = 32 - bits_needs #New prefix Length of every host
            list_of_ip_range.append(new_prefix) #Append it into list
        return list_of_ip_range
    
    def VLSM_result(list_of_ip_range, ip):
        separator()
        print(f"--> CIDR Notation: {ip} <--\n") #The original CIDR Notation of user
        print("--> Result: <--\n")
        network = IP.ip_network(ip, strict=False)
        subnets = sorted(list_of_ip_range)  # Sort subnets in ascending order
        start_ip = network.network_address
        used_networks = [] 
        
        for subnet in list_of_ip_range:
            while True:
                ip_network = IP.ip_network(f"{start_ip}/{subnet}", strict=False)
                if not any(ip_network.overlaps(existing) for existing in used_networks):
                    break
                # Move to the next start_ip if overlap occurs
                start_ip = IP.ip_address(int(start_ip) + ip_network.num_addresses)
            
            used_networks.append(ip_network)
            
            print(f"---Network {subnets.index(subnet) + 1}: {ip_network}---")
            print(f"Network Address: {ip_network.network_address}")
            print(f"Broadcast Address: {ip_network.broadcast_address}")
            print(f"Subnet Mask: {ip_network.netmask}")
            print(f"Prefix Length: /{ip_network.prefixlen}")
            print(f"Host: {ip_network.num_addresses - 2}")
            print(f"Number of Usable IP: {ip_network.network_address + 1} TO {ip_network.broadcast_address - 1}\n")
            
            # Move start_ip to the next available address after the current subnet
            start_ip = IP.ip_address(int(ip_network.broadcast_address) + 1)
        separator()
        return used_networks
    
    def VLSM_to_FLSM(used_networks):
        while True:
            #Asking user if he wants to subnet a CIDR Notation
            FLSM_user = input("--> Do you want to subnet a CIDR Notation (Y/N): ").strip().lower()
            if FLSM_user == "y":
                Subnet_CIDR_Notation(used_networks)
            elif FLSM_user == "n":
                return False #Quitting
            else:
                print("Y or N Only, Please try again.")

    #Subnetting in VLSM
    def networks(ip):
        def calculating_bits_needed(networks):
            #Calculating bits needs
            bits = 0
            while (1 << bits) < networks:
                bits += 1
            return bits
        
        while True:
            try:
                #Asking user how many subnet it needs to divide
                num_subnet = input(f"--> Please enter the number of subnets 1 TO {ip.num_addresses} (Type 'q' to quit): ").strip().lower()
                #Options
                if num_subnet == 'q':
                    print("\nYou back to previous question")
                    return None #Quitting

                int_num_subnet = int(num_subnet) #Translating into Integer
                if int_num_subnet < 1:
                    print("1 and above only :)")
                    continue
                max_subnets = 2**(32 - ip.prefixlen)   
                if int_num_subnet > max_subnets:
                    print(f"The number of requested subnets exceeds the maximum possible for this network ({max_subnets}). Please try again.")
                    continue
                bits_needed = calculating_bits_needed(int_num_subnet)
                return bits_needed
            except ValueError:
                print(f"Please Type how many networks you want to divide.")

    def calculating(ip,  bits_needed):
        prefix = ip.prefixlen + bits_needed
        if prefix > 32:
            raise ValueError("The resulting prefix length exceeds /32. Please try again.")
        return prefix

    def result(ip, prefix):
        separator()
        details_list = []
        #Result of user wants to divide
        for i, details in enumerate(ip.subnets(new_prefix=prefix)):
            #Num Addressses
            print(f"---Subnet {i +1}: {details}---")
            print(f"Network Address: {details.network_address}")
            print(f"Broadcast Address: {details.broadcast_address}")
            print(f"Subnet Mask: {details.netmask}")
            print(f"Prefix Length: /{details.prefixlen}")
            print(f"Number of Available Host: {num_address(details)}")
            print(f"IP Range: {details.network_address} TO {details.broadcast_address}\n")
            details_list.append(details)
        separator()
        return details_list
    
    #Binary Translator
    def asking(ip, prefix):     
        while True:
            #Asking user to Translate Network Address, Broadcast Address and Subnet Mask into binary
            user = input("Do you want to translate Network Address, Broadcasts Address, and Subnet Mask into binary (Y/N only!): ").strip()
            if user.lower() == "y":
                binary(ip, prefix)
                break
            elif user.lower() == "n":
                break
            else:
                print("Y/N only :(")
    
    def binary(ip, prefix):
        print("")
        print("Binary Translate:")
        #Binary Translator
        for number, result in enumerate(ip.subnets(new_prefix=prefix)):
            binary_network_address = '.'.join(f"{int(octet):08b}" for octet in result.network_address.exploded.split('.'))
            binary_broadcast_address =  '.'.join(f"{int(octet):08b}" for octet in result.broadcast_address.exploded.split('.'))
            binary_subnetmask = '.'.join(f"{int(octet):08b}" for octet in result.netmask.exploded.split('.'))

            #Num address
            num_address(result)
        
            #Result
            print("")
            print(f"---Subnet {number+1}: {result}---")
            print(f"Network Address: {result.network_address} translate into {binary_network_address}")
            print(f"Broadcast Address: {result.broadcast_address} translate into {binary_broadcast_address}")
            print(f"Subnet Mask: {result.netmask} translate into {binary_subnetmask}")
            print(f"Prefix Length: /{result.prefixlen}")
            print(f"Host: {num_address(result)}")
        separator()
    
    
    def VLSMs():
        while True:
            #Asking user to type IP Address Range
            ip = ip_input()
            if not ip:
                break
            elif ip is None:
                break
            while True:
                #Asking user to type network host
                list_host = asking_network_host(ip)
                if list_host is None:
                    break
                elif not list_host:
                    return ip
                list_of_ip_range = calculating_prefix_length_host(list_host)
                used_networks = VLSM_result(list_of_ip_range, ip)
                while  True:
                    #Asking user if he wants to subnet a CIDR Notation
                    if not VLSM_to_FLSM(used_networks):
                        break
                    Subnet_CIDR_Notation(used_networks)

    #VLSM Asking what user want to subnet
    def ask_to_pick_cidr_notation(used_networks):
         #Chosing user to pick a CIDR Notation
        while True:
            try:
                separator()
                print("Available CIDR Notation:")
                for index_of_ip_range, ip_range in enumerate(used_networks):
                    print(f"- Network: {index_of_ip_range +1}: {ip_range}")

                user_input = input(f"\n--> Chose a subnet from available list 1 TO {len(used_networks)} type 'b' to back: ").strip().lower()
                if user_input == 'b':
                    return None #Back to the previous
                
                int_user_input = int(user_input) #Translating into Integer

                if int_user_input < 1 or int_user_input > len(used_networks):
                    print(f"Please choose a number between 1 and {len(used_networks)}")
                else:
                    for num_cidr, scd in enumerate(used_networks):
                        if int_user_input == num_cidr +1:
                            single_cidr_notation = IP.ip_network(scd)
                    separator()
                    print(f"You chose CIDR Notation {num_cidr +1}: {single_cidr_notation}")
                    print(f"Host: {single_cidr_notation.num_addresses}\n")
                    return single_cidr_notation
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception:
                print("Something went wrong, please try again.")

    def Subnet_CIDR_Notation(used_networks):
        while True:
            single_cidr_notation = ask_to_pick_cidr_notation(used_networks)
            if single_cidr_notation is None:      
                break
            while True:
                bits_needed = networks(single_cidr_notation)
                if bits_needed is None:
                    break
                prefix = calculating(single_cidr_notation, bits_needed)
                result(single_cidr_notation, prefix)
                asking(single_cidr_notation, prefix)
                return single_cidr_notation
            
    #Num Addresses settings
    def num_address(details):
            #Num Addressses
            if details.num_addresses -2 < 0:
                host = "No Available Host"
            else:
                host = details.num_addresses -2
                if host == 0:
                   host = "No Available Host" 
            return host
            
    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)

    def main():
        VLSMs()
    main()
if __name__ == "__main__":
    VLSM()