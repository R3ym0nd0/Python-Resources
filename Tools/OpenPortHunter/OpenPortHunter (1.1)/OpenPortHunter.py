import socket
import ipaddress as IP
import os
import whois

def Port_Scanner():
    common_protocols = {
        # Web Protocols
        80:"HTTP",
        443:"HTTPS",
        8080:"HTTP Alternative",

        # Mail Protocols
        25:"SMTP",
        587:"SMTP/STARTTLS",
        465:"SMTPS",
        110:"POP3",
        995:"POP3S",
        143:"IMAP",
        993:"IMAPS",

        # File Transfer Protocols
        21:"FTP",
        990:"FTPS",
        69:"TFTP",

        # Remote Access Protocols
        22:"SSH",
        23:"Telnet",
        3389:"RDP",
        5900:"VNC",
        5901:"VNC",

        # Network Time Protocol
        123:"NTP",

        # Database Protocols
        3306:"MySQL",
        5432:"PostgreSQL",
        1521:"Oracle Database",

        # Messaging Protocols
        5222:"XMPP",
        6697:"IRC",

        # VoIP Protocols
        5060:"SIP",
        5061:"SIPS",

        # Game Server Protocols
        27015:"Steam",

        # Others
        161:"SNMP Polling Port",
        162:"SNMP Trap Port"
        }

    def menu():  # This function displays the main menu and handles user choices
        terminal_width = os.get_terminal_size().columns # Get the terminal width for centering text
        while True: # Loop until a valid choice is made
            separator()  # Print a separator line
            print("Tool Name: OpenPortHunter".center(terminal_width)) # Center and display the tool name
            print("Version: 1.0".center(terminal_width)) # Center and display the version
            print("Coded by: Reymond Joaquin".center(terminal_width))  # Center and display the author
            print("Written in: Python".center(terminal_width)) # Center and display the programming language

            separator()
            print("!! Important Notice !!\n".center(terminal_width)) # Center and display importance notice
            print("This OpenPortHunter is intended for educational purposes and authorized security assessments only.".center(terminal_width)) # Inform the user of the tool's purpose
            print("Unauthorized use of this tool may violate local laws and regulations.".center(terminal_width))
            separator()

            # calling the input_target function
            enter_target()

    def enter_target():  # This function handles domain name input and resolves it to an IP address
        while True:  # Loop to continuously accept user input until 'q' is entered
            user = input("--> Enter a Target (e.g, example.com or 172.172.123.23). Type 'q' to quit: ").strip().capitalize() # Prompt user for domain name
            if user.lower() == "q": # If the user chooses to quit
                exit() # This will exit the program
            elif user == "":
                separator()
                print("Note: Please enter a Domain Name or IP Addresses")
                separator()
                continue
            
            try:
                # Attempt to resolve the domain name to an IP address
                ip = socket.gethostbyname(user) # Get the IP address corresponding to the domain name
                scanning_choices(ip, user) # Call the function to scan the resolved IP address
            except socket.gaierror:
                # Handle the case where the domain name cannot be resolved
                separator()
                print(f"Note: Could not resolve the domain name {user}") # Inform the user of the error
                separator()

    def print_info(title, info):
        if isinstance(info, list): # This will check if 'info' is a list
            print(f"{title}:") # Prints the title of 'info' for example domain name, registrar, etc..
            for num, name in enumerate(info):
                print(f"{num +1}.{name}") # This will print every info in the list
            print("") # Just for spacing
        else:
            print(f"{title}:") 
            print(f"1.{info}\n")

    def whois_info(user, ip):
        terminal_width = os.get_terminal_size().columns
        domain_info = whois.whois(user) # to access .domain_name, .whois_server, .registrar, .expiration_date, etc.

        # Print some of the retrieved
        separator()
        print(f"--> Domain Information for {user} <--   ".center(terminal_width))
        separator()
        print_info("Domain Name", domain_info.domain_name)
        print(f"IP Address:\n1.{ip}\n")
        print_info("Registrar", domain_info.registrar)
        print_info("Whois Server", domain_info.whois_server)
        print_info("Creation Date", domain_info.creation_date)
        print_info("Expiration Date", domain_info.expiration_date)
        print_info("Name Servers", domain_info.name_servers)
        print_info("Status", domain_info.status)

    def scanning_choices(ip, user):
        IP.IPv4Address(ip) # Converts the string 'ip' into an IPv4 address object
        whois_info(user, ip) # Calling the whois_info function to print all the information in the target
        while True:
            separator()
            # This will print all the Choices
            print("Choices:") 
            print("[1] Specific Ports (Scan Only Specific Ports)")
            print("[2] Well-Known Ports (1 - 1023)")
            print("[3] Registered Ports (1024 - 49151)")
            print("[4] Ephemeral Ports (49152 - 65535)")
            print("[5] Scan All Ports (1 - 65535)")
            separator()
            # Asking user if 'Which in the choice would he like to use'
            port = input("--> Which choice would you like to use (Type 'q' to quit): ").strip().lower()
            
            # This will call function base on the key, for example, if user pick '1', then they calling the 'specific_port_scan(ip, user)' function 
            choices = {"1": lambda: specific_port_scan(ip, user),
                       "2": lambda: large_port_scan(ip, user, scan_port = [1, 1024]),
                       "3": lambda: large_port_scan(ip, user, scan_port = [1024, 49152]),
                       "4": lambda: large_port_scan(ip, user, scan_port = [49152, 65536]),
                       "5": lambda: large_port_scan(ip, user, scan_port = [1, 65536])
                       }
            
            # This will check if the user's input type is in the choices (1 - 5)
            if port in choices:
                result = choices[port]() 
                if result: # This will check if result is None
                    print(result)
            elif port == "q":
                menu() # Calling the 'menu()' function if user type 'q'
            else:
                separator()
                print("Note: Invalid Choice") # This will print if user is not in the choices (1-5). For example -1, or 6 and so on...

    def specific_port_scan(ip, user):
        separator()
        while True:
            # Asking user to Type specific ports (1 - 65535)
            port = input("--> Type Specific Ports (1 - 65535 / Type 'q' to quit): ").strip().lower()
            if port == "q": 
                scanning_choices(ip, user) # Calling the 'scanning_choices(ip, user)' function if user type 'q'
            elif port.isdigit(): # This will check if user input is number
                int_port = int(port) # This will translate port into integer because it's string at first
                if int_port in range(1, 65536): # This will check if the user number that he type is 1 - 65535 
                    separator() 
                    print(f"Scanning Port {int_port} in progress.....\n")
                    result = tcp_scanning(ip, int_port)
                    udp_scanning(ip, int_port)
                    separator()
                    if int_port in common_protocols: # This will check if int_port is in common_protocols, if yes, then it will print the value on that port for example: 80/HTTP
                        if result == 0: # This will check if port is successfully listening
                            print("Result:\n")
                            print(f"--> Port {port} | {common_protocols[int_port]} Protocol is OPEN in {ip} <--") # This will print if the ports is OPEN with her protocol name for example port 80 is HTTP
                            separator()
                        else:
                            print("Result:\n")
                            print(f"--> Port {port} | {common_protocols[int_port]} Protocol is CLOSED in {ip} <--") # This will print if the ports is CLOSED with her protocol name for example port 80 is HTTP
                            separator()
                    else:
                        if result == 0:
                            print("Result:\n")
                            print(f"--> Port {int_port} is OPEN in {ip} <--") # This will print if the ports is OPEN
                            separator()
                        else:
                            print("Result:\n")
                            print(f"--> Port {int_port} is CLOSED in {ip} <--") # This will print if the ports is CLOSED
                            separator()
                else:
                    separator()
                    print("Note: Please choose a port between 1 - 65535") # This will print if user input the number that its not 1 - 65535
                    separator()
            else:
                separator()
                print("Note: Invalid Port, please try again") # This will print if user input alphabet
                separator()

    def large_port_scan(ip, user, scan_port):            
        separator()
        print(f"---> Scanning Port {scan_port[0]} - {scan_port[1] -1} in progress..... <--\n") # This will print the range of scanning, for example: 1 - 1023
        list_open_ports = [] # All of the open ports are go to this list

        def open_ports_result(list_open_ports):
            if list_open_ports:
                for num, port in enumerate(list_open_ports):
                    separator()
                    print("Open Ports Result:\n")
                    print(f"{num +1}. Port {port} is OPEN on {str(ip)}") # This will summarize and print all OPEN PORTS
            else:
                separator()
                print("Open Ports Result:\n")
                print(f"No open ports found on {str(ip)}.") # This will print if no OPEN PORTS found

        for ports in range(scan_port[0], scan_port[1]):
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating socket in TCP
            socket.setdefaulttimeout(1) #1 Second Timeout
            try:
                tcp_result = tcp_socket.connect_ex((str(ip), ports)) # This will attempt to connect to the target IP and port
                if tcp_result == 0: # This will check if the connection was successful (indicating the port is open and listening)
                    print(f"- TCP Port {ports} is OPEN on {ip}") # This will print if ports is OPEN
                    list_open_ports.append(ports) # This will append in list_open_ports = [] variable
                else:
                    print(f"- TCP Port {ports} is CLOSED on {ip}") # This will print if ports is CLOSED
            except socket.error as error:
                print(f"- Error connecting to {ip}:{ports} - {error}") # Prints an error message if the connection to the target fails
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
                print(f"- UDP Port {ports} is OPEN on {ip}")
                list_open_ports.append(ports) # This will append in list_open_ports = [] variable
            except socket.timeout:
                print(f"- UDP Port {ports} is CLOSED on {ip}")  # No response means closed
            except socket.error as error:
                print(f"- Error connecting to {ip}:{ports} - {error}")
            finally:
                udp_socket.close()  # Close UDP socket after use

        open_ports_result(list_open_ports) # Calling the summarize 'open_ports_result(list_open_ports)' function after scanning is done

    def tcp_scanning(ip, int_port):
        # Create TCP socket for TCP scanning
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating TCP socket
        socket.setdefaulttimeout(1) #1 Second Timeout
        try:
            result = tcp_socket.connect_ex((ip, int_port)) # Attempt to connect to the target IP and port
            if result == 0:
                 print(f"- TCP Port {int_port} is OPEN on {ip}")
                 return result # returning the result
            else:
                print(f"- TCP Port {int_port} is CLOSED on {ip}")
        except socket.error as error:
            print(f"Error connecting to {ip}:{int_port} - {error}")
        finally:
            tcp_socket.close()

    def udp_scanning(ip, int_port):
        # Create UDP socket for UDP scanning
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creating UDP socket
        udp_socket.settimeout(1) # Set timout for UDP
        try:
            udp_socket.sendto(b'', (ip, int_port))  # Send an empty packet
            udp_socket.recvfrom(1024)  # Wait for a response
            print(f"- UDP Port {int_port} is OPEN on {ip}")
        except socket.timeout:
            print(f"- UDP Port {int_port} is CLOSED on {ip}")  # No response means closed
        except socket.error:
            print(f"- Error connecting to {ip}:{int_port}")
        finally:
            udp_socket.close() # # Close UDP socket after use

    def separator():
        # Get the width of the terminal (how many characters fit in one line)
        terminal_width = os.get_terminal_size().columns

        # Make a line of '=' characters that is as wide as the terminal
        separator = "=" * terminal_width

        # Print the line of '=' characters
        print(separator)  

    def main():
        menu() # Calling the 'menu()' function

    while True:
        try:
            main() # Calling the 'main()' function because if not, you will see blank..
        except KeyboardInterrupt:
            print("\nReturning to main menu...") # If user Interrupt with her keyboard for exampl ctrl + C, it will return into 'menu()' function
            continue # Back to the start of the lop[ which is the 'main()' function

if __name__ == "__main__":
    Port_Scanner()