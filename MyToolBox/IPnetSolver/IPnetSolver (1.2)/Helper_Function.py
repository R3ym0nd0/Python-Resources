import ipaddress as IP
import os

def ip_input() -> IP.ip_network:
        while True:
            try:
                # Asking user to type CIDR Notation
                IP_Address: str = input("--> Type CIDR notation (e.g., 192.168.43.0/24). Type 'q' to quit: ").strip()
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

def num_address(details: int) -> int:
            #Num Addressses
            if details.num_addresses -2 < 0: # This will check if details.num_addresses or basically the number of host -2, is less than 0
                host = "No Available Host"
            else:
                host = details.num_addresses -2 # subtracting 2 the number of host for the network and broadcast addresses
                if host == 0: # Thi will check if number of host -2 is 0
                   host = "No Available Host" 
            return host

# This function is for design purposes
def separator() -> None:
    terminal_width: int = os.get_terminal_size().columns
    separator: int = "=" * terminal_width
    print(separator)