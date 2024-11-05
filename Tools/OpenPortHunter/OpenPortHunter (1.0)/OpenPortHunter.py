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
        if isinstance(info, list):
            print(f"{title}:")
            for num, name in enumerate(info):
                print(f"{num +1}.{name}")
            print("")
        else:
            print(f"{title}:")
            print(f"1.{info}\n")

    def whois_info(user, ip):
        terminal_width = os.get_terminal_size().columns
        domain_info = whois.whois(user)

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
        IP.IPv4Address(ip)
        whois_info(user, ip)
        while True:
            separator()
            print("Choices:")
            print("[1] Specific Ports (Scan Only Specific Ports)")
            print("[2] Well-Known Ports (1 - 1023)")
            print("[3] Registered Ports (1024 - 49151)")
            print("[4] Ephemeral Ports (49152 - 65535)")
            print("[5] Scan All Ports (1 - 65535)")
            separator()
            port = input("--> Which choice would you like to use (Type 'q' to quit): ").strip().lower()
            choices = {"1": lambda: specific_port_scan(ip, user),
                       "2": lambda: large_port_scan(ip, user, scan_port = [1, 1024]),
                       "3": lambda: large_port_scan(ip, user, scan_port = [1024, 49152]),
                       "4": lambda: large_port_scan(ip, user, scan_port = [49152, 65536]),
                       "5": lambda: large_port_scan(ip, user, scan_port = [1, 65536])
                       }
            if port in choices:
                result = choices[port]()
                if result:
                    print(result)
            elif port == "q":
                menu()
            else:
                separator()
                print("Note: Invalid Choice")

    def specific_port_scan(ip, user):
        separator()
        while True:
            port = input("--> Type Specific Ports (1 - 65535 / Type 'q' to quit): ").strip().lower()
            if port == "q":
                scanning_choices(ip, user)
            elif port.isdigit():
                int_port = int(port)
                if int_port in range(1, 65536):
                    separator() 
                    print(f"Scanning Port {int_port} in progress.....\n")
                    result = tcp_scanning(ip, int_port)
                    udp_scanning(ip, int_port)
                    separator()
                    if int_port in common_protocols:
                        if result == 0:
                            print("Result:\n")
                            print(f"--> Port {port} | {common_protocols[int_port]} Protocol is OPEN in {ip} <--")
                            separator()
                        else:
                            print("Result:\n")
                            print(f"--> Port {port} | {common_protocols[int_port]} Protocol is CLOSED in {ip} <--")
                            separator()
                    else:
                        if result == 0:
                            print("Result:\n")
                            print(f"--> Port {int_port} is OPEN in {ip} <--")
                            separator()
                        else:
                            print("Result:\n")
                            print(f"--> Port {int_port} is CLOSED in {ip} <--")
                            separator()
                else:
                    separator()
                    print("Note: Please choose a port between 1 - 65535")
                    separator()
            else:
                separator()
                print("Note: Invalid Ports, please try again")
                separator()

    def large_port_scan(ip, user, scan_port):            
        separator()
        print(f"---> Scanning Port {scan_port[0]} - {scan_port[1] -1} in progress..... <--\n")
        list_open_ports = []

        def open_ports_result(list_open_ports):
            if list_open_ports:
                for num, port in enumerate(list_open_ports):
                    separator()
                    print("Open Ports Result:\n")
                    print(f"{num +1}. Port {port} is OPEN on {str(ip)}")
            else:
                separator()
                print("Open Ports Result:\n")
                print(f"No open ports found on {str(ip)}.")

        for ports in range(scan_port[0], scan_port[1]):
            
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) #1 Second Timeout
            try:
                tcp_result = tcp_socket.connect_ex((str(ip), ports))
                if tcp_result == 0:
                    print(f"- TCP Port {ports} is OPEN on {ip}")
                    list_open_ports.append(ports)
                else:
                    print(f"- TCP Port {ports} is CLOSED on {ip}")
            except socket.error as error:
                print(f"- Error connecting to {ip}:{ports} - {error}")
            except KeyboardInterrupt:
                open_ports_result(list_open_ports)
                ip = socket.gethostbyname(user)
                scanning_choices(ip, user)
            finally:
                tcp_socket.close()

            # Create UDP socket for UDP scanning
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.settimeout(1) # Set timout for UDP
            try:
                udp_socket.sendto(b'', (ip, ports))  # Send an empty packet
                udp_socket.recvfrom(1024)  # Wait for a response
                print(f"- UDP Port {ports} is OPEN on {ip}")
                list_open_ports.append(ports)
            except socket.timeout:
                print(f"- UDP Port {ports} is CLOSED on {ip}")  # No response means closed
            except socket.error as error:
                print(f"- Error connecting to {ip}:{ports} - {error}")
            finally:
                udp_socket.close()  # Close UDP socket after use

        open_ports_result(list_open_ports)

    def tcp_scanning(ip, int_port):
        # Create TCP socket for TCP scanning
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #1 Second Timeout
        try:
            # int_port = int(port)
            result = tcp_socket.connect_ex((ip, int_port))
            if result == 0:
                 print(f"- TCP Port {int_port} is OPEN on {ip}")
                 return result
            else:
                print(f"- TCP Port {int_port} is CLOSED on {ip}")
        except socket.error as error:
            print(f"Error connecting to {ip}:{int_port} - {error}")
        finally:
            tcp_socket.close()

    def udp_scanning(ip, int_port):
        # Create UDP socket for UDP scanning
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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

    # Tool Design
    def separator():
        terminal_width = os.get_terminal_size().columns
        separator = "=" * terminal_width
        print(separator)   

    def main():
        menu()

    while True:
        try:
            main()
            break
        except KeyboardInterrupt:
            print("\nReturning to main menu...")
            continue

if __name__ == "__main__":
    Port_Scanner()