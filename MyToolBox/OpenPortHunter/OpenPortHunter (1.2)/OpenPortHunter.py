import socket
import ipaddress as IP
import os
import whois as whois_lib

from colorama import Fore, init

# Initialize colorama to automatically reset color after each print
init(autoreset=True)

def Port_Scanner() -> None:
    common_protocols: dict = {
        # Web Protocols
        80: Fore.LIGHTGREEN_EX + "HTTP",
        443: Fore.LIGHTGREEN_EX + "HTTPS",
        8080: Fore.LIGHTGREEN_EX + "HTTP Alternative",

        # Mail Protocols
        25: Fore.RED + "SMTP",
        587: Fore.RED + "SMTP/STARTTLS",
        465: Fore.RED +"SMTPS",
        110: Fore.RED + "POP3",
        995: Fore.RED + "POP3S",
        143: Fore.RED + "IMAP",
        993: Fore.RED + "IMAPS",

        # File Transfer Protocols
        21: Fore.LIGHTRED_EX + "FTP",
        990: Fore.LIGHTRED_EX + "FTPS",
        69: Fore.LIGHTRED_EX + "TFTP",

        # Remote Access Protocols
        22: Fore.BLUE + "SSH",
        23: Fore.BLUE + "Telnet",
        3389: Fore.BLUE + "RDP",
        5900: Fore.BLUE + "VNC",
        5901: Fore.BLUE + "VNC",

        # Network Time Protocol
        123: Fore.LIGHTYELLOW_EX + "NTP",

        # Database Protocols
        3306: Fore.LIGHTYELLOW_EX + "MySQL",
        5432: Fore.LIGHTYELLOW_EX + "PostgreSQL",
        1521: Fore.LIGHTYELLOW_EX + "Oracle Database",

        # Messaging Protocols
        5222: Fore.LIGHTBLUE_EX + "XMPP",
        6697: Fore.LIGHTBLUE_EX + "IRC",

        # VoIP Protocols
        5060: Fore.CYAN + "SIP",
        5061: Fore.CYAN + "SIPS",

        # Game Server Protocols
        27015: Fore.BLUE + "Steam",

        # Others
        161: Fore.MAGENTA + "SNMP Polling Port",
        162: Fore.MAGENTA + "SNMP Trap Port"
        }

    def menu() -> None:  # This function displays the main menu and handles user choices
        separator()
        print(Fore.BLUE + rf"""
   ____                   _____           _   _    _             _            
  / __ \                 |  __ \         | | | |  | |           | |           
 | |  | |_ __   ___ _ __ | |__) |__  _ __| |_| |__| |_   _ _ __ | |_ ___ _ __ 
 | |  | | '_ \ / _ \ '_ \|  ___/ _ \| '__| __|  __  | | | | '_ \| __/ _ \ '__|
 | |__| | |_) |  __/ | | | |  | (_) | |  | |_| |  | | |_| | | | | ||  __/ |   
  \____/| .__/ \___|_| |_|_|   \___/|_|   \__|_|  |_|\__,_|_| |_|\__\___|_|   
        | |                                                                   
        |_|                        {Fore.RED + "- Hunt the ports, uncover the secrets..."}""")

        while True: # Loop until a valid choice is made
            separator()  # Print a separator line
            print(f"{Fore.LIGHTGREEN_EX + "Tool Name"}   {Fore.LIGHTMAGENTA_EX + ":"} {Fore.LIGHTCYAN_EX + "OpenPortHunter"}") # Center and display the tool name
            print(f"{Fore.LIGHTGREEN_EX + "Version"}     {Fore.LIGHTMAGENTA_EX + ":"} {Fore.LIGHTCYAN_EX + "1.2"}") # Center and display the version
            print(f"{Fore.LIGHTGREEN_EX + "Coded by"}    {Fore.LIGHTMAGENTA_EX + ":"} {Fore.LIGHTCYAN_EX + "Reymond Joaquin"}")  # Center and display the author
            print(f"{Fore.LIGHTGREEN_EX + "Description"} {Fore.LIGHTMAGENTA_EX + ":"} {Fore.LIGHTCYAN_EX + "An open port hunter designed to hunt open ports, helping identify potential entry points."}") # Center and display the programming language
            print(f"{Fore.LIGHTGREEN_EX + "Purpose"}     {Fore.LIGHTMAGENTA_EX + ":"} {Fore.LIGHTCYAN_EX + "To assist ethical hackers, penetration testers, and security enthusiasts in their assessments."}")
            print(f"{Fore.LIGHTGREEN_EX + "Disclaimer"}  {Fore.LIGHTMAGENTA_EX + ":"} {Fore.LIGHTCYAN_EX + "This OpenPortHunter is intended for educational purposes and authorized security assessments only."}")
            separator()

            # calling the input_target function
            enter_target()

    def enter_target() -> None:  # This function handles domain name input and resolves it to an IP address
        while True:  # Loop to continuously accept user input until 'q' is entered
            user: str = input(f"{Fore.RED + "[*]"} {Fore.WHITE + f"Enter a Target (e.g, {Fore.YELLOW + "example.com"} {Fore.WHITE + "or"} {Fore.YELLOW + "172.172.123.23"}){Fore.WHITE + f". Type {Fore.RED + "'q'"} {Fore.WHITE + "to quit:"}"}"} ").strip().capitalize() # Prompt user for domain name
            if user.lower() == "q": # If the user chooses to quit
                exit() # This will exit the program
            elif user == "":
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please enter a Domain Name or IP Addresses"} {Fore.RED + "!!"}")
                separator()
                continue
            
            try:
                # Attempt to resolve the domain name to an IP address
                ip: str = socket.gethostbyname(user) # Get the IP address corresponding to the domain name
                scanning_choices(ip, user) # Call the function to scan the resolved IP address
            except socket.gaierror:
                # Handle the case where the domain name cannot be resolved
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + f"Could not resolve the domain name {user}"} {Fore.RED + "!!"}") # Inform the user of the error
                separator()

    def print_info(title: str, info: list[str]) -> None:
        if isinstance(info, list): # This will check if 'info' is a list
            print(f"{Fore.LIGHTGREEN_EX + title}:\n") # Prints the title of 'info' for example domain name, registrar, etc..
            for num, name in enumerate(info):
                print(Fore.LIGHTMAGENTA_EX + f"{num +1}.{name}") # This will print every info in the list
            print("") # Just for spacing
        else:
            print(f"{Fore.LIGHTGREEN_EX + title}:\n") 
            print(Fore.LIGHTMAGENTA_EX + f"1.{info}\n")

    def whois_info(user: str, ip: str) -> None:
        try:
            terminal_width: int = os.get_terminal_size().columns
            data = whois_lib.whois(user) # to access .domain_name, .whois_server, .registrar, .expiration_date, etc.

            # Print some of the retrieved
            separator()
            print(f"{Fore.YELLOW + "!!"} {Fore.LIGHTGREEN_EX + f"Domain Information for {user}"} {Fore.YELLOW + "!!"}".center(terminal_width))
            separator()
            print_info("Domain Name", data.domain_name)
            print(f"{Fore.LIGHTGREEN_EX + "IP Address:"}\n\n{Fore.LIGHTMAGENTA_EX + f"1.{ip}"}\n")
            print_info("Registrar", data.registrar)
            print_info("Whois Server", data.whois_server)
            print_info("Creation Date", data.creation_date)
            print_info("Expiration Date", data.expiration_date)
            print_info("Name Servers", data.name_servers)
            print_info("Status", data.status)

        except ConnectionResetError:
            separator()
            print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Connection was unexpectedly closed by the remote host"} {Fore.RED + "!!"}")
        except TimeoutError:
            separator()
            print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Connection Time Out"} {Fore.RED + "!!"}")

    def scanning_choices(ip: str, user: str) -> None:
        IP.IPv4Address(ip) # Converts the string 'ip' into an IPv4 address object
        whois_info(user, ip) # Calling the whois_info function to print all the information in the target
        while True:
            separator()
            # This will print all the Choices
            print(f"{Fore.LIGHTMAGENTA_EX + "[*]"} {Fore.BLUE + "CHOOSE A PORT SCANNER:"}\n") 
            print(f"{Fore.LIGHTGREEN_EX + "[1]"} Specific Ports (Scan Only Specific Ports)")
            print(f"{Fore.GREEN + "[2]"} Well-Known Ports (1 - 1023)")
            print(f"{Fore.YELLOW + "[3]"} Registered Ports (1024 - 49151)")
            print(f"{Fore.LIGHTRED_EX + "[4]"} Ephemeral Ports (49152 - 65535)")
            print(f"{Fore.RED + "[5]"} Scan All Ports (1 - 65535)")
            separator()
            # Asking user if 'Which in the choice would he like to use'
            port: int = input(f"{Fore.RED + "[*]"} {Fore.WHITE + "Which choice would you like to use (Type"} {Fore.RED + "'q'"} {Fore.WHITE + "to quit):"} ").strip().lower()
            
            # This will call function base on the key, for example, if user pick '1', then they calling the 'specific_port_scan(ip, user)' function 
            choices: dict = {"1": lambda: specific_port_scan(ip, user),
                       "2": lambda: large_port_scan(ip, user, scan_port = [1, 1024]),
                       "3": lambda: large_port_scan(ip, user, scan_port = [1024, 49152]),
                       "4": lambda: large_port_scan(ip, user, scan_port = [49152, 65536]),
                       "5": lambda: large_port_scan(ip, user, scan_port = [1, 65536])
                       }
            
            # This will check if the user's input type is in the choices (1 - 5)
            if port in choices:
                result: dict = choices[port]() 
                if result: # This will check if result is None
                    print(result)
            elif port == "q":
                menu() # Calling the 'menu()' function if user type 'q'
            else:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.RED + "Invalid Choice"} {Fore.RED + "!!"}") # This will print if user is not in the choices (1-5). For example -1, or 6 and so on...

    def specific_port_scan(ip: str, user: str) -> None:
        separator()
        while True:
            # Asking user to Type specific ports (1 - 65535)
            port: int = input(f"{Fore.RED + "[*]"} {Fore.WHITE + "Type Specific Ports"} ({Fore.YELLOW + "1 - 65535"} {Fore.WHITE + "or type"} {Fore.RED + "'q'"} {Fore.WHITE + "to quit):"} ").strip().lower()
            if port == "q": 
                scanning_choices(ip, user) # Calling the 'scanning_choices(ip, user)' function if user type 'q'
            elif port.isdigit(): # This will check if user input is number
                int_port: int = int(port) # This will translate port into integer because it's string at first
                if int_port in range(1, 65536): # This will check if the user number that he type is 1 - 65535 
                    separator() 
                    print(Fore.LIGHTGREEN_EX + f"Scanning Port {int_port} in progress.....\n")
                    result: None = tcp_scanning(ip, int_port)
                    udp_scanning(ip, int_port)
                    separator()
                    if int_port in common_protocols: # This will check if int_port is in common_protocols, if yes, then it will print the value on that port for example: 80/HTTP
                        if result == 0: # This will check if port is successfully listening
                            print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Result:\n"}")
                            print(f"Port {Fore.LIGHTMAGENTA_EX + port} {Fore.WHITE + "|"} {common_protocols[int_port]} {Fore.WHITE + "Protocol is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "in"} {Fore.LIGHTCYAN_EX + ip}") # This will print if the ports is OPEN with her protocol name for example port 80 is HTTP
                            separator()
                        else:
                            print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Result:\n"}")
                            print(f"Port {Fore.LIGHTMAGENTA_EX + port} {Fore.WHITE + "|"} {common_protocols[int_port]} {Fore.WHITE + "Protocol is"} {Fore.RED + "CLOSED"} {Fore.WHITE + "in"} {Fore.LIGHTCYAN_EX + ip}") # This will print if the ports is CLOSED with her protocol name for example port 80 is HTTP
                            separator()
                    else:
                        if result == 0:
                            print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Result:\n"}")
                            print(f"Port {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "in"} {Fore.LIGHTCYAN_EX + ip}") # This will print if the ports is OPEN
                            separator()
                        else:
                            print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Result:\n"}")
                            print(f"Port {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "is"} {Fore.RED + "CLOSED"} {Fore.WHITE + "in"} {Fore.LIGHTCYAN_EX + ip}")  # This will print if the ports is CLOSED
                            separator()
                else:
                    separator()
                    print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please choose a port between 1 - 65535"} {Fore.RED + "!!"}") # This will print if user input the number that its not 1 - 65535
                    separator()
            else:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Invalid Port, please try again"} {Fore.RED + "!!"}") # This will print if user input alphabet
                separator()

    def large_port_scan(ip: str, user: str, scan_port: list[int]) -> None:            
        separator()
        print(Fore.LIGHTGREEN_EX + f"Scanning Port {scan_port[0]} - {scan_port[1] -1} in progress.....\n") # This will print the range of scanning, for example: 1 - 1023
        list_open_ports: list[int] = [] # All of the open ports are go to this list

        def open_ports_result(list_open_ports) -> None:
            if list_open_ports:
                separator()
                print(Fore.RED + f"[*] {Fore.LIGHTGREEN_EX + "Open Ports Result:\n"}")
                for num, port in enumerate(list_open_ports):
                    print(f"{Fore.LIGHTCYAN_EX + f"[{num +1}]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(port)} {Fore.WHITE + "is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}") # This will summarize and print all OPEN PORTS
            else:
                separator()
                print(Fore.LIGHTGREEN_EX + "Open Ports Result:\n")
                print(Fore.RED + f"No open ports found on {Fore.LIGHTCYAN_EX + str(ip)}.") # This will print if no OPEN PORTS found

        for ports in range(scan_port[0], scan_port[1]):
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating socket in TCP
            socket.setdefaulttimeout(1) #1 Second Timeout
            try:
                tcp_result = tcp_socket.connect_ex((str(ip), ports)) # This will attempt to connect to the target IP and port
                if tcp_result == 0: # This will check if the connection was successful (indicating the port is open and listening)
                    print(f"{Fore.GREEN + "[TCP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(ports)} {Fore.WHITE + "is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}") # This will print if ports is OPEN
                    list_open_ports.append(ports) # This will append in list_open_ports = [] variable
                else:
                    print(f"{Fore.GREEN + "[TCP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(ports)} {Fore.WHITE + "is"} {Fore.RED + "CLOSE"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}") # This will print if ports is CLOSED
            except socket.error:
                print(f"{Fore.RED + "[ERROR]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(ports)} {Fore.WHITE + "Connecting to"} {Fore.LIGHTCYAN_EX + ip}") # Prints an error message if the connection to the target fails
            except KeyboardInterrupt:
                open_ports_result(list_open_ports) # Calling the 'open_ports_result(list_open_ports)' if user keyboaradInterrupt, for example he try to ctrl + c
                ip = socket.gethostbyname(user)
                scanning_choices(ip, user) # Calling 'scanning_choices(ip, user)' function
            finally:
                tcp_socket.close() # This will close the TCP socket after use

            # Create UDP socket for UDP scanning
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creating socket in UDP
            udp_socket.settimeout(1) # Set timout for UDP
            try:
                udp_socket.sendto(b'', (ip, ports))  # Send an empty packet
                udp_socket.recvfrom(1024)  # Wait for a response
                print(f"{Fore.YELLOW + "[UDP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(ports)} {Fore.WHITE + "is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}")
                list_open_ports.append(ports) # This will append in list_open_ports = [] variable
            except socket.timeout:
                print(f"{Fore.YELLOW + "[UDP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(ports)} {Fore.WHITE + "is"} {Fore.RED + "CLOSE"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}")  # No response means closed
            except socket.error:
                print(f"{Fore.RED + "[ERROR]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(ports)} {Fore.WHITE + "Connecting to"} {Fore.LIGHTCYAN_EX + ip}")
            finally:
                udp_socket.close()  # Close UDP socket after use

        open_ports_result(list_open_ports) # Calling the summarize 'open_ports_result(list_open_ports)' function after scanning is done

    def tcp_scanning(ip: str, int_port: int) -> int:
        # Create TCP socket for TCP scanning
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating TCP socket
        socket.setdefaulttimeout(1) #1 Second Timeout
        try:
            result = tcp_socket.connect_ex((ip, int_port)) # Attempt to connect to the target IP and port
            if result == 0:
                 print(f"{Fore.GREEN + "[TCP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}")
                 return result # returning the result
            else:
                print(f"{Fore.GREEN + "[TCP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "is"} {Fore.RED + "CLOSE"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}")
        except socket.error:
            print(f"{Fore.RED + "[ERROR]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "Connecting to"} {Fore.LIGHTCYAN_EX + ip}")
        finally:
            tcp_socket.close()

    def udp_scanning(ip: str, int_port: int) -> None:
        # Create UDP socket for UDP scanning
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creating UDP socket
        udp_socket.settimeout(1) # Set timout for UDP
        try:
            udp_socket.sendto(b'', (ip, int_port))  # Send an empty packet
            udp_socket.recvfrom(1024)  # Wait for a response
            print(f"{Fore.YELLOW + "[UDP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "is"} {Fore.LIGHTGREEN_EX + "OPEN"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}")
        except socket.timeout:
            print(f"{Fore.YELLOW + "[UDP]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "is"} {Fore.RED + "CLOSE"} {Fore.WHITE + "on"} {Fore.LIGHTCYAN_EX + ip}")  # No response means closed
        except socket.error:
            print(f"{Fore.RED + "[ERROR]"} {Fore.WHITE + "Port"} {Fore.LIGHTMAGENTA_EX + str(int_port)} {Fore.WHITE + "Connecting to"} {Fore.LIGHTCYAN_EX + ip}")
        finally:
            udp_socket.close() # # Close UDP socket after use

    def separator() -> None:
        # Get the width of the terminal (how many characters fit in one line)
        terminal_width: int = os.get_terminal_size().columns

        # Make a line of '=' characters that is as wide as the terminal
        separator: int = Fore.LIGHTMAGENTA_EX + "=" * terminal_width

        # Print the line of '=' characters
        print(separator)  

    def main() -> None:
        menu() # Calling the 'menu()' function

    while True:
        try:
            main() # Calling the 'main()' function because if not, you will see blank..
        except KeyboardInterrupt:
            print("\nReturning to main menu...") # If user Interrupt with her keyboard for exampl ctrl + C, it will return into 'menu()' function
            continue # Back to the start of the lop[ which is the 'main()' function

if __name__ == "__main__":
    Port_Scanner()
