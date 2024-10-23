import ipaddress as IP
import os

def FLSM():

    def ip_input():
        while True:
            try:
                #Asking user to type CIDR Notation
                IP_Address = input("--> Type CIDR Notation (eg..192.168.43.0/24 (Type 'q' to quit): ").strip()
                if IP_Address.lower() == "q":
                    separator()
                    return None #Quitting
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

    def networks(ip):
        def calculating_bits_needed(networks):
            #Calculating bits needs
            bits = 0
            while (1 << bits) < networks: #While 1 << bits is less than networks bits, +1 until...
                bits += 1
            return bits
        
        while True:
            try:
                #Asking user how many subnet it needs to divide
                num_subnet = input(f"--> Please enter the number of subnets 1 TO {ip.num_addresses} (Type 'q' to quit): ").strip().lower()
                #Options
                if num_subnet == 'q':
                    return None #Quitting
                int_num_subnet = int(num_subnet) #Translating into Integer
                if int_num_subnet < 1:
                    print("1 and above only :)")
                    continue
                max_subnets = 2**(32 - ip.prefixlen) # 2^32 - (prefix length of user CIDR notation) 
                if int_num_subnet > max_subnets:
                    print(f"The number of requested subnets exceeds the maximum possible for this network ({max_subnets}). Please try again.")
                    continue
                bits_needed = calculating_bits_needed(int_num_subnet)
                return bits_needed
            except ValueError:
                print(f"Please Type how many networks you want to divide.")

    def calculating(ip,  bits_needed):
        prefix = ip.prefixlen + bits_needed #New prefix length of every CIDR Notation
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
    
    #Binary
    def asking(ip, prefix):     
        while True:
            #Asking user to Translate Network Address, Broadcast Address and Subnet Mask into binary
            user = input("--> Do you want to translate Network Address, Broadcasts Address, and Subnet Mask into binary (Y/N only!): ").strip()
            if user.lower() == "y":
                binary(ip, prefix)
                break #It break after showing the result
            elif user.lower() == "n":
                break #Quitting
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

            #Result of Binary
            print("")
            print(f"---Subnet {number+1}: {result}---")
            print(f"Network Address: {result.network_address} translate into {binary_network_address}")
            print(f"Broadcast Address: {result.broadcast_address} translate into {binary_broadcast_address}")
            print(f"Subnet Mask: {result.netmask} translate into {binary_subnetmask}")
            print(f"Prefix Length: /{result.prefixlen}")
            print(f"Host: {num_address(result)}")
        separator()
    
    #Subnetting a Subnet(FLSM Feature)
    def asking_subnetting_every_subnet(details_list):
        while True:
            #Asking user if he wants to subnet every subnet of the result
            asking_to_subnet_a_subnet = input("\n--> Do you want to subnet every subnet in your result (Y/N): ").strip()
            if asking_to_subnet_a_subnet.lower() == "y":
                ask_to_subnet_a_subnet(details_list)
            elif asking_to_subnet_a_subnet.lower() == "n":
                return None #Quitting
            else:
                print("Y or N Only")

    def choosing_subnet(details_list):    
            while True:
                try:
                    #This will list all of available subnets base on the result
                    print("Available Subnets:")
                    for nums, every_subnet in enumerate(details_list):
                        print(f"Subnet {nums +1}: {every_subnet}")
                    print(f"Host: {every_subnet.num_addresses} Host")
                    #Asking user to chose subnet
                    choosing_user = input(f"\n--> Chose a subnet that you want to divide 1 TO {len(details_list)} (Type 'q'  to quit): ").strip()
                    if choosing_user.lower() == "q":
                        return None #Quitting
                    elif int(choosing_user) < 1 or int(choosing_user) > len(details_list):
                        print(f"Please choose a number between 1 and {len(details_list)}")
                    else:
                        #User chose a subnet
                        for num_subnets, length in enumerate(details_list):
                            if int(choosing_user) == num_subnets +1:
                                if length.prefixlen == 32:
                                    separator()
                                    print(f"Note: The {length} is single IP Address, there no reason to subnet it.\n")
                                    continue
                                separator()
                                #This is user subnet chose
                                print(f"You Chose Subnet {num_subnets +1}: {length}\n")
                                return length
                except ValueError:
                    print(f"Please Type 1 TO {len(details_list)} or Type 'n' to back")
    
    #FLSM printing Available Subnets
    def ask_to_subnet_a_subnet(details_list):
            while True:
                separator()
                length = choosing_subnet(details_list)
                if length is None:
                    break #Quitting
                while True:
                    bits_needed = networks(length)
                    if bits_needed is None:
                        break #Quitting
                    elif not bits_needed:
                        return length #Back to the choosing_subnet(details_list) function
                    prefix = calculating(length, bits_needed)
                    #Asking if user wants to translate the result into binary
                    result(length, prefix)
                    asking(length, prefix) 
                    break

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
            #Design
            terminal_width = os.get_terminal_size().columns
            separator = "=" * terminal_width
            print(separator)

    #All Functions of FLSM
    def FLSM_function():
        while True:
            ip = ip_input()
            if ip is None:
                break #Quitting
            while True:       
                bits_needed = networks(ip)
                if bits_needed is None:
                    break #Quitting
                prefix = calculating(ip, bits_needed)
                details_list = result(ip, prefix)
                asking(ip, prefix)
                if asking_subnetting_every_subnet(details_list) is None:
                    break #Quitting

    def main():
        FLSM_function() #Call the function
    main()

if __name__ == "__main__":
    FLSM()