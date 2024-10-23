import ipaddress as IP

while True:

    try:

        #Creating IP Address Objects
        ip = IP.ip_address("192.168.43.182")
        print(ip)

        #Checking IP Address Type
        print(ip.is_private)

        #IPV4 Adress
        ip_address = input("Type IPAdress: ")
        ip = IP.IPv4Address(ip_address)
        print(ip)

        #IP Range
        ip_range = input("Type IP Range: ")
        ip = IP.ip_network(ip_range)
        print(ip)

        #Accessing Prefix Length
        prefix_length = ip.prefixlen

        #Accessing Network Information
        print(ip.network_address)
        print(ip.broadcast_address)

        #Host in network      
        ip_range = input("Type IP Range: ")
        range = IP.ip_network(ip_range)

        for ip in range.hosts():
            print(ip)

        #Check if an IP address is in network:
        ip = IP.ip_address("192.168.43.88")

        ip_range = input("Type IP Range: ")
        range = IP.ip_network(ip_range)
        print(f"The {ip} is in {range}")

        #Manipulating IP addresses
        ip_address = input("Type IPAdress: ")
        ip = IP.IPv4Address(ip_address)
        print(ip +1)
        print(ip -1)

        #Generating Subnets
        for subnet in ip.subnets(new_prefix=26):
            print(subnet)
        
        #Finding the Parent Network
        parent = ip.supernet(new_prefix=16)
        print(parent)
    except Exception as error:
        print(f"Something went wrong: {error}")

