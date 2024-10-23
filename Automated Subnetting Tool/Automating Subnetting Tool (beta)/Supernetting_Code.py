import ipaddress as IP
import os

def Supernetting():
    # List of CIDR Notation
    def block_CIDR_notation():
        list_CIDR_notation = []
        while True:
            try:
                user = input("--> Type list of CIDR Notation (Type 'done' to finish / Type 'q' to quit): ").strip().lower()
                if user == "q":
                    separator()
                    return None  # Quitting
                elif user == "done":
                    if not list_CIDR_notation:
                        print("Note: Please Type a CIDR Notation.")
                        list_CIDR_notation = []
                        continue
                    else:
                        separator()
                        return list_CIDR_notation
                else:
                    # Blocks of CIDR Notation
                    cidr = IP.ip_network(user)
                    for i in list_CIDR_notation:
                        if i == cidr:
                            print("Note: Repeated CIDR Notation detected, please try again")
                            list_CIDR_notation = []
                            continue
                    else:
                        list_CIDR_notation.append(cidr)
            except ValueError:
                print("Note: Please Type a valid IPv4 network")

    def sorted_result(list_CIDR_notation):
        print("--> Blocks of CIDR Notation <--")
        sorted_cidr = list(sorted(list_CIDR_notation))
        list_of_num_addresses = []
        for num, subnet in enumerate(sorted_cidr):
            print(f"- subnet {num + 1}: {subnet}")
            overall_num_addresses = subnet.num_addresses
            list_of_num_addresses.append(overall_num_addresses)
        return sum(list_of_num_addresses), sorted_cidr
    
    #Checking Gaps
    def check_gaps(sorted_cidr):
        print("\n--> Checking for gaps between CIDR blocks... <--")
        for i in range(len(sorted_cidr) - 1):
            current_network = sorted_cidr[i]  # First CIDR block
            next_network = sorted_cidr[i + 1]  # Next CIDR block
            
            # Get the last IP of the current network
            current_last_ip = current_network.broadcast_address
            next_first_ip = next_network.network_address
            
            # Check if there is a gap
            if current_last_ip +1 != next_first_ip:
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
        while (2 ** power) < required_addresses:
            power += 1   
        # Calculate the prefix length
        subnet_bits = power
        prefix_length = 32 - subnet_bits
        first_address =  sorted_cidr[0]
        net_address = first_address.network_address
        supernet = f"{net_address}/{prefix_length}"
        print(f"\n--> The supernet is: {supernet} <--")
        return supernet

    def user_asking(list_CIDR_notation):
        while True:
            user = input("--> Do you want to continue Supernetting (Y/N): ").strip().lower()
            if user == "y":
                separator()
                return list_CIDR_notation  # Back to start
            elif user == "n":
                return None  # Quitting
            else:
                print("Y or N only")

    def first_feature():
        while True:
            list_CIDR_notation = block_CIDR_notation()
            if list_CIDR_notation is None:
                break
            elif list_CIDR_notation:
                list_of_num_addresses,  sorted_cidr = sorted_result(list_CIDR_notation)
                if check_gaps(sorted_cidr) is None:
                    separator()
                    continue
                else:
                    prefix_length(list_of_num_addresses,  sorted_cidr)
            separator()
            if user_asking(list_CIDR_notation) is None:
                break

    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)

    def main():
        first_feature()
    main()

if __name__ == "__main__":
    Supernetting()
