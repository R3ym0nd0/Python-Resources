import ipaddress as IP
import os

def Supernetting():
    # List of CIDR Notation
    def block_CIDR_notation():
        list_CIDR_notation = [] # This will collect ip networks that user type
        while True:
            try:
                # Asking user to type a list of CIDR Notation
                user = input("--> Type list of CIDR Notation (Type 'done' to finish / Type 'q' to quit): ").strip().lower()
                if user == "q": # This will check if user type 'q'
                    return None  # Quitting
                elif user == "done": # This will check if user type 'done'
                    if not list_CIDR_notation: # This will check if user didn't type any CIDR Notation and then type 'done' immediately
                        separator()
                        print("Note: Please Type a CIDR Notation.")
                        separator()
                        list_CIDR_notation = [] # This will reset the list_CIDR_Notation if it have CIDR Notation inside
                        continue
                    else:
                        separator()
                        return list_CIDR_notation
                else:
                    # Blocks of CIDR Notation
                    cidr = IP.ip_network(user) # Tbis will translate the user input into ip network object, if it detects that user type ip network
                    for i in list_CIDR_notation:
                        if i == cidr: # This will check if i variable is equal to cidr to fix the repeated CIDR Notation
                            separator()
                            print("Note: Repeated CIDR Notation detected, please try again")
                            separator()
                            list_CIDR_notation = []
                            continue
                    else:
                        list_CIDR_notation.append(cidr) # The cidr variable will append in list_CIDR_Notation list
            except ValueError:
                separator()
                print("Note: Please Type the IPv4 network") # This will print if user didn't type ip network
                separator()

    def sorted_result(list_CIDR_notation):
        print("--> Blocks of CIDR Notation <--")
        sorted_cidr = list(sorted(list_CIDR_notation)) # This will sort the list_CIDR_Notation list starting from lowest to highest CIDR Notation
        list_of_num_addresses = [] # This will collect the number of host in every CIDR Notation
        for num, subnet in enumerate(sorted_cidr):
            print(f"- subnet {num + 1}: {subnet}") # This will print every CIDR Notation in sorted starting from lowest to highest CIDR Notation
            overall_num_addresses = subnet.num_addresses # The number of available host in every CIDR Notation
            list_of_num_addresses.append(overall_num_addresses) # This will append the host in list_of_num_addresses
        return sum(list_of_num_addresses), sorted_cidr
    
    # Checking Gaps
    def check_gaps(sorted_cidr):
        print("\n--> Checking for gaps between CIDR blocks... <--")
        for i in range(len(sorted_cidr) - 1):
            current_network = sorted_cidr[i]  # First CIDR block
            next_network = sorted_cidr[i + 1]  # Next CIDR block
            
            # Get the last IP of the current network
            current_last_ip = current_network.broadcast_address
            next_first_ip = next_network.network_address
            
            # Check if there is a gap
            if int(current_last_ip) +1 < int(next_first_ip):
                print(f"Note: Gap detected between {current_last_ip} and {next_first_ip}")
                return None  # Stop if a gap is detected
            
            # Check for overlap
            if current_network.overlaps(next_network):
                print(f"Overlapping detected between {current_network} and {next_network}")
                return None  # Stop if an overlap is detected
        
        # If no gaps or overlaps were found
        print("No gaps or overlaps detected, continuing to supernet result...")
        return True
    
    def prefix_length(list_of_num_addresses, sorted_cidr):
        # Calculate the number of required addresses (including network and broadcast)
        required_addresses = list_of_num_addresses -2
        # Find the smallest power of 2 that is greater than or equal to the required addresses
        power = 0
        while (2 ** power) < required_addresses:  # While the 2 ^ power(start from 0) is less than required_addresses(for example of host is 62)
            power += 1  # It will increment until power variable or bits needed is enough. For example: 2 ^ 6(power) = 64 Host
        
        # Calculate the prefix length
        prefix_length = 32 - power # subtracting the power variable into 32. For example: 32 - 6 = 26. That means the new prefix length is /26
        first_address =  sorted_cidr[0] # This will take the first address in sorted_cidr list
        net_address = first_address.network_address # This will take the network address in first address variable(ip network)
        supernet = f"{net_address}/{prefix_length}" # This will create a new ip network
        print(f"\n--> The supernet is: {supernet} <--") # This will print the result of supernet variable
        return supernet

    def user_asking(list_CIDR_notation):
        while True:
            user = input("--> Do you want to continue Supernetting (Y/N): ").strip().lower() # Asking user if he wants to continue
            if user == "y": # This will check is user type 'Y'
                separator()
                return list_CIDR_notation  # Back to start
            elif user == "n":
                return None  # Quitting
            else:
                separator()
                print("Note: Y or N only, Please try again") # This will print if user didn't type 'Y' or 'N'
                separator()

    def start_program():
        while True:
            list_CIDR_notation = block_CIDR_notation()
            if list_CIDR_notation is None: # This wil check if block_CIDR_notation function returns None
                break
            elif list_CIDR_notation:
                list_of_num_addresses,  sorted_cidr = sorted_result(list_CIDR_notation)
                if check_gaps(sorted_cidr) is None: # This wil check if sorted_result function returns None
                    separator()
                    continue
                else:
                    prefix_length(list_of_num_addresses,  sorted_cidr)
            separator()
            if user_asking(list_CIDR_notation) is None: # This wil check if user_asking function returns None
                break

    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)

    def main():
        start_program() # Calling the start_program function
    main()

if __name__ == "__main__":
    Supernetting()
