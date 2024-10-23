import subprocess as SP
import ipaddress as IP

def nmap():
    try:

        while True:

            question = input("Type Nmap Command (-sn/-o/-sp, etc...): ").strip()
            
            if question in ["-sn", "-O", "-sp","-sV"]:

                IP_Address = input(f"Enter IP Address for nmap {question}: ").strip()
                ip = IP.IPv4Address(IP_Address)

                if ip:
                    Command = ["nmap", question, IP_Address]
                    result = SP.run(Command, capture_output=True, text=True)
                    print(result.stdout)
                    print(result.stderr)
                    
                    asking = input("Do you want to continue? (yes to continue): ").strip().lower()
                    if asking != "yes":
                        print("Bye!")
                        break
                else:
                    print("Please provide a valid IP address!")
            else:
                print("Please enter a valid option: -sn, -O, -sp, -sV only!")

    except Exception as error:
        print(f"Something went wrong: {error}")

if __name__ == "__main__":
    nmap()