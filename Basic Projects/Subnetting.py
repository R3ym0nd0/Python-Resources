import ipaddress as IP

def get_valid_ip_range():

    while True:
        try:
            ip_range = input("Type your IP Range (e.g., '192.168.43.0/24'): ")
            ip = IP.ip_network(ip_range, strict=False)
            return ip
        except ValueError as error:
            print(f"Invalid IP range format. Please try again: {error}")

def get_num_subnets():

    while True:
        try:
            num_subnets = int(input("Type how many networks to divide: "))
            if num_subnets < 1 or num_subnets > 256:
                print("1 - 256 Only!")
            else:
                return num_subnets
        except ValueError:
            print("Number Only!")

def calculate_subnets(ip, num_subnets):

    network_address = ip.network_address.exploded.split(".")
    host_address = int(network_address[3])
    prefixlen = ip.prefixlen
    
    subnet_details = []
    
    for subnet in range(num_subnets):
        if num_subnets == 1:
            host = 256
            citr = "/24"
            subnet_mask = "255.255.255.0"
        elif num_subnets == 2 or num_subnets == 3:
            host = 128 
            citr = "/25"
            subnet_mask = "255.255.255.128"
        elif num_subnets == 4:
            host = 64 
            citr = "/26"
            subnet_mask = "255.255.255.192"
        elif num_subnets >= 5 and num_subnets <= 8:
            host = 32 
            citr = "/27"
            subnet_mask = "255.255.255.224"
        elif num_subnets >= 9 and num_subnets <= 16:
            host = 16 
            citr = "/28"
            subnet_mask = "255.255.255.240"
        elif num_subnets >= 17 and num_subnets <= 32:
            host = 8 
            citr = "/29"
            subnet_mask = "255.255.255.248"
        elif num_subnets >= 33 and num_subnets <= 64:
            host = 4 
            citr = "/30"
            subnet_mask = "255.255.255.252"
        elif num_subnets >= 65 and num_subnets <= 128:
            host = 2 
            citr = "/31"
            subnet_mask = "255.255.255.254"
        elif num_subnets >= 129 and num_subnets <= 256:
            host = 1 
            citr = "/32"
            subnet_mask = "255.255.255.255"

        #Network ID
        network_id_parts = network_address[:-1]
        network_id_parts.append(str(host_address) + subnet * host)
        network_id = f"{network_id_parts[0]}.{network_id_parts[1]}.{network_id_parts[2]}.{network_id_parts[3]}"

        #Broadcast ID
        broadcast_id_parts = network_address[:-1]
        broadcast_id_parts.append(str(int(network_id_parts[3]) + host - 1))
        broadcast_id = f"{broadcast_id_parts[0]}.{broadcast_id_parts[1]}.{broadcast_id_parts[2]}.{broadcast_id_parts[3]}"

        #Hosts ID Range
        network_range = int(network_id_parts[3]) + 1
        broadcast_range = int(broadcast_id_parts[3]) - 1
        host_id_range = f"{network_id_parts[0]}.{network_id_parts[1]}.{network_id_parts[2]}.{network_range} TO {network_id_parts[0]}.{network_id_parts[1]}.{network_id_parts[2]}.{broadcast_range}"

        subnet_details.append({
            "subnet_mask": subnet_mask,
            "citr": citr,
            "network_id": network_id,
            "broadcast_id": broadcast_id,
            "usable_hosts": host - 2,
            "host_id_range": host_id_range
        })
    
    return subnet_details

def print_subnet_details(subnet_details):

    for i, details in enumerate(subnet_details):
        print()
        print(f"Subnet {i + 1} result:")
        print()
        print(f"Subnet Mask: {details['subnet_mask']}")
        print(f"CITR Notation: {details['citr']}")
        print(f"Network ID: {details['network_id']}")
        print(f"Broadcast ID: {details['broadcast_id']}")
        print(f"Number of Usable Host: {details['usable_hosts']}")
        print(f"Host ID Range: {details['host_id_range']}")
        print()

def main():
    print("Subnetting Program (Class C)\n")
    
    ip = get_valid_ip_range()
    num_subnets = get_num_subnets()
    subnet_details = calculate_subnets(ip, num_subnets)
    print_subnet_details(subnet_details)
    
    while True:
        ask_user = input("Do you want to translate it into binary (Y or N): ").lower()
        if ask_user == "y":
            pass
        elif ask_user == "n":
            print("Thanks For using this program :)")
            exit()
        else:
            print("Y or N only!")

if __name__ == "__main__":
    main()
