from colorama import Fore, init
from Helper_Function import separator

# Initialize colorama to automatically reset color after each print
init(autoreset=True)

def calculation_guide(num) -> None:
    if num == "1":
        separator()
        print(f"{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}How to Calculate in Fixed-Length Subnet Masking (FLSM) {Fore.MAGENTA}[*]")
        print(f"""
{Fore.LIGHTMAGENTA_EX}What is Fixed-Length Subnet Masking (FLSM)?
 
    {Fore.WHITE}FLSM is a subnetting technique where all subnets use the same subnet mask,
  resulting in equal-sized subnets with the same number of hosts. 
  It is simple and efficient in networks requiring uniform subnet sizes but can waste 
  IP addresses if subnet requirements vary.     

{Fore.LIGHTMAGENTA_EX}Step 1: {Fore.LIGHTCYAN_EX}Identify your network and subnet requirements

  {Fore.RED}Example:

    {Fore.WHITE}IP Network: {Fore.LIGHTGREEN_EX}192.168.43.0/24
    {Fore.WHITE}How Many Subnets: {Fore.LIGHTGREEN_EX}4

  {Fore.RED}Details for Each Subnets:

    {Fore.LIGHTCYAN_EX}Subnet (1, 2, 3, 4):

      {Fore.WHITE}Network Address:
      {Fore.WHITE}Broadcast Address:
      {Fore.WHITE}Subnet Mask:
      {Fore.WHITE}Prefix Length:
      {Fore.WHITE}Number of Available Host:
      {Fore.WHITE}Usable IP Range:

{Fore.LIGHTMAGENTA_EX}Step 2: {Fore.LIGHTCYAN_EX}Calculate the number of bits needed

  {Fore.MAGENTA}- {Fore.WHITE}To split the network into subnets, we need to determine how many bits to borrow.
  {Fore.MAGENTA}- {Fore.WHITE}Use the formula: {Fore.GREEN}2**n {Fore.WHITE}(where {Fore.GREEN}'n' {Fore.WHITE}means number of subnets, in this case, {Fore.GREEN}4{Fore.WHITE}).
  {Fore.MAGENTA}- {Fore.WHITE}For {Fore.GREEN}4 {Fore.WHITE}subnets, {Fore.GREEN}2**2 = 4{Fore.WHITE}, so it means we need to borrow {Fore.GREEN}2 bits{Fore.WHITE}.

{Fore.LIGHTMAGENTA_EX}Step 3: {Fore.LIGHTCYAN_EX}Identify the new Prefix-Length

  {Fore.MAGENTA}- {Fore.WHITE}The original prefix length is {Fore.GREEN}/24{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}The new prefix-length is found by adding the number of bits borrowed to the original network's prefix length.
  {Fore.MAGENTA}- {Fore.WHITE}Since we borrowed {Fore.GREEN}2 bits{Fore.WHITE}, the new prefix length will be {Fore.GREEN}/26 {Fore.WHITE}({Fore.GREEN}/24 + 2 = /26{Fore.WHITE}).
  {Fore.MAGENTA}- {Fore.WHITE}The new CIDR notation for the network is {Fore.GREEN}192.168.43.0/26{Fore.WHITE}.

{Fore.LIGHTMAGENTA_EX}Step 4: {Fore.LIGHTCYAN_EX}Identify the Available Host on the new Prefix-Length
              
  {Fore.MAGENTA}- {Fore.WHITE}Use the formula: {Fore.GREEN}2**h - 2 {Fore.WHITE}(where {Fore.GREEN}'h' {Fore.WHITE}is the number of host bits).
  {Fore.MAGENTA}- {Fore.WHITE}In the case of a {Fore.GREEN}/26 subnet ({Fore.WHITE}which has {Fore.GREEN}6 host bits{Fore.WHITE}: {Fore.GREEN}32 - 26 = 6{Fore.WHITE})
  {Fore.MAGENTA}- {Fore.GREEN}2**6 -2 = 62 usable hosts {Fore.WHITE}(the {Fore.GREEN}-2 {Fore.WHITE}is for the {Fore.GREEN}network address {Fore.WHITE}and the {Fore.GREEN}broadcast address{Fore.WHITE})
  {Fore.MAGENTA}- {Fore.WHITE}Therefore, a /26 network provides {Fore.GREEN}62 usable IP addresses per subnet{Fore.WHITE}.
              
{Fore.LIGHTMAGENTA_EX}Step 5: {Fore.LIGHTCYAN_EX}Find the Network Address of Each Subnet
              
  {Fore.MAGENTA}- {Fore.WHITE}The network address is the first IP in each subnet, which identifies the subnet itself.
  {Fore.MAGENTA}- {Fore.WHITE}Start with the original IP network {Fore.GREEN}192.168.43.0/26 {Fore.WHITE}(ignore the {Fore.GREEN}/26 {Fore.WHITE}prefix-length for now).
  {Fore.MAGENTA}- {Fore.WHITE}To find the next network address, add the current network address({Fore.GREEN}192.168.43.0{Fore.WHITE}) and the total number of
  {Fore.WHITE}IP addresses, which is {Fore.GREEN}64{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.GREEN}192.168.43.0 + 64 = 192.168.43.64
  {Fore.MAGENTA}- {Fore.WHITE}Therefore, the next network address is {Fore.GREEN}192.168.43.64/26{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}Since the requirement is for {Fore.GREEN}4 subnets{Fore.WHITE}, we need to create {Fore.GREEN}4 network addresses{Fore.WHITE}:
    
    {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.43.0
    {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.43.64
    {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.43.128
    {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.192
              
{Fore.LIGHTMAGENTA_EX}Step 6: {Fore.LIGHTCYAN_EX}Find the Broadcast Address of Each Subnet
  
  {Fore.MAGENTA}- {Fore.WHITE}The broadcast address is the last IP address in each subnet, used to communicate with all devices in that subnet.
  {Fore.MAGENTA}- {Fore.WHITE}Start with the {Fore.GREEN}192.168.43.0 {Fore.WHITE}and find the next network address. The broadcast address is the last IP just before the
  {Fore.WHITE}next network address.
  {Fore.MAGENTA}- {Fore.WHITE}For the subnet {Fore.GREEN}192.168.43.0/26 {Fore.WHITE}(network address), the next subnet is {Fore.GREEN}192.168.43.64{Fore.WHITE}. The broadcast address is
  {Fore.GREEN}192.168.43.63{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}To easily find it, look at the second subnet, {Fore.GREEN}192.168.43.64/26{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}Simply {Fore.GREEN}subtract 1 {Fore.WHITE}from the second network address ({Fore.GREEN}192.168.43.64{Fore.WHITE}) to get the broadcast address for the
  {Fore.WHITE}first subnet: {Fore.GREEN}192.168.43.63{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}Repeat this process for each subnet:

    {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.43.0/26 {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}Broadcast: {Fore.LIGHTCYAN_EX}192.168.43.63
    {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.43.64/26 {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}Broadcast: {Fore.LIGHTCYAN_EX}192.168.43.127
    {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.43.128/26 {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}Broadcast: {Fore.LIGHTCYAN_EX}192.168.43.191
    {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.192/26 {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}Broadcast: {Fore.LIGHTCYAN_EX}192.168.43.255
              
{Fore.LIGHTMAGENTA_EX}Step 7: {Fore.LIGHTCYAN_EX}Find the Subnet Mask of Each Subnet
  
  {Fore.MAGENTA}- {Fore.WHITE}The subnet mask determines the range of IP addresses that can belong to a subnet.
  {Fore.MAGENTA}- {Fore.WHITE}Since we already know the subnet prefix length ({Fore.GREEN}/26{Fore.WHITE}), we can easily calculate the subnet mask.
  {Fore.MAGENTA}- {Fore.WHITE}Convert the {Fore.GREEN}/26 {Fore.WHITE}into binary. To do this, write {Fore.GREEN}26 ones in the structure of an IP address, and the rest as zeros{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}When converting an IP address into binary, each octet contains {Fore.GREEN}8 bits{Fore.WHITE}. It looks like this:
    {Fore.GREEN}xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
  {Fore.MAGENTA}- {Fore.WHITE}This is what it looks like:
    {Fore.GREEN}11111111.11111111.11111111.11000000 {Fore.WHITE}| There are {Fore.GREEN}26 ones{Fore.WHITE}, and the rest are {Fore.GREEN}zeros{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}Convert that binary into {Fore.GREEN}decimal {Fore.WHITE}now. To do this, follow these steps:
                     
    {Fore.LIGHTGREEN_EX}2**7 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}128
    {Fore.LIGHTGREEN_EX}2**6 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}64
    {Fore.LIGHTGREEN_EX}2**5 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}32             
    {Fore.LIGHTGREEN_EX}2**4 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}16                             
    {Fore.LIGHTGREEN_EX}2**3 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}8
    {Fore.LIGHTGREEN_EX}2**2 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}4
    {Fore.LIGHTGREEN_EX}2**1 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}2
    {Fore.LIGHTGREEN_EX}2**0 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}1   
                    
     ------------------------------------      
    | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
     ------------------------------------  

    {Fore.RED}Example:
                
      {Fore.LIGHTGREEN_EX}11111111
    
    {Fore.RED}Process: {Fore.WHITE}Imagine every bits in {Fore.GREEN}11111111 {Fore.WHITE}as 128, 64, and so on.
                        
      {Fore.LIGHTGREEN_EX}1(128) + 1(64) + 1(32) + 1(16) + 1(8) + 1(4) + 1(2) + 1(1) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}255 in decimal
                  
    {Fore.WHITE}Now, for {Fore.GREEN}11111111.11111111.11111111.11000000{Fore.WHITE}, break it into {Fore.GREEN}4 octets{Fore.WHITE}:
      
      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}11111111 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}11111111 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}11111111 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}11000000 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192
      {Fore.RED}Note: {Fore.WHITE}The first bit on the left is always {Fore.GREEN}128{Fore.WHITE}.
      
      {Fore.LIGHTCYAN_EX}Subnet Mask Result: {Fore.LIGHTGREEN_EX}255.255.255.192
              
{Fore.LIGHTMAGENTA_EX}Step 8: {Fore.LIGHTCYAN_EX}Find the Usable IP Range in Each Subnet
  
  {Fore.MAGENTA}- {Fore.WHITE}The usable IP range is the set of addresses in a subnet,
  excluding the {Fore.GREEN}network address (first address) {Fore.WHITE}and the {Fore.GREEN}broadcast address (last address){Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}To find the range, first is list the {Fore.GREEN}network address {Fore.WHITE}and {Fore.GREEN}broadcast address {Fore.WHITE}of each subnet.
  
    {Fore.LIGHTCYAN_EX}Subnet 1:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.0
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.63

    {Fore.LIGHTCYAN_EX}Subnet 2:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.64
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.127

    {Fore.LIGHTCYAN_EX}Subnet 3:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.128
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.191
    
    {Fore.LIGHTCYAN_EX}Subnet 3:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.192
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.255
              
  {Fore.MAGENTA}- {Fore.WHITE}all you need to do is add {Fore.GREEN}+1 {Fore.WHITE}in each network address while {Fore.GREEN}-1 {Fore.WHITE}into broadcast address for example:
  
    {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.0 +1
    {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.64 -1
  
  {Fore.MAGENTA}- {Fore.WHITE}This is the Usable IP Range now:
              
    {Fore.RED}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.1 - 192.168.43.63
              
  {Fore.MAGENTA + "-"} {Fore.WHITE + "Repeat this process on the 4 subnet:"}

    {Fore.LIGHTCYAN_EX}Subnet 1:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.0
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.63
      {Fore.RED}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.1 - 192.168.43.62

    {Fore.LIGHTCYAN_EX}Subnet 2:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.64
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.127
      {Fore.RED}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.65 - 192.168.43.126
            
    {Fore.LIGHTCYAN_EX}Subnet 3:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.128
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.191
      {Fore.RED}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.129 - 192.168.43.190
                
    {Fore.LIGHTCYAN_EX}Subnet 4:

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.192
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.255  
      {Fore.RED}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.193 - 192.168.43.254
              
{Fore.LIGHTMAGENTA_EX}Step 9: {Fore.LIGHTCYAN_EX}Provide all the details of the subnet from Step 1

  {Fore.LIGHTCYAN_EX}Subnet 1: {Fore.RED}192.168.43.0/26

    {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.0
    {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.63
    {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.192
    {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/26
    {Fore.WHITE}Number of Available Host: {Fore.LIGHTGREEN_EX}62
    {Fore.WHITE}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.1 - 192.168.43.62

  {Fore.LIGHTCYAN_EX}Subnet 2: {Fore.RED}192.168.43.64/26"

    {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.64
    {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.127
    {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.192
    {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/26
    {Fore.WHITE}Number of Available Host: {Fore.LIGHTGREEN_EX}62
    {Fore.WHITE}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.65 - 192.168.43.126
          
  {Fore.LIGHTCYAN_EX}Subnet 3: {Fore.RED}192.168.43.128/26

    {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.128
    {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.191
    {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.192
    {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/26
    {Fore.WHITE}Number of Available Host: {Fore.LIGHTGREEN_EX}62
    {Fore.WHITE}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.129 - 192.168.43.190
              
  {Fore.LIGHTCYAN_EX}Subnet 4: {Fore.RED}192.168.43.192/26

    {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.192
    {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.255
    {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.192
    {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/26
    {Fore.WHITE}Number of Available Host: {Fore.LIGHTGREEN_EX}62
    {Fore.WHITE}Usable IP Range: {Fore.LIGHTGREEN_EX}192.168.43.193 - 192.168.43.254

{Fore.LIGHTMAGENTA_EX}Conclusion and Acknowledgements:
              
    {Fore.WHITE}This is how FLSM calculation works. As you can see, it can be quite complex when you do it
  from scratch, but it's essential to learn if you want to dive into networking and fields like ethical 
  hacking, and so on. But don't worry! IPnetSolver is here to assist you. You can use this tool as your 
  buddy to work together and automate the process. Just be sure to use it responsibly, okay?

  Thank you for reading, and I hope my IPnetSolver tool helps you. 
  - Reymond Joaquin""")
        separator()

    elif num == "2": 
        separator() 
        print(f"""{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}How to Calculate in Variable-Length Subnet Masking (VLSM) {Fore.MAGENTA}[*]
              
{Fore.LIGHTMAGENTA_EX}What is Variable-Length Subnet Masking (VLSM)?

    {Fore.WHITE}VLSM is a subnetting technique where an IP address space is divided into
  subnets of varying sizes based on the specific needs of a network, allowing
  for more efficient IP address allocation.  

{Fore.LIGHTMAGENTA_EX}Step 1: {Fore.LIGHTCYAN_EX}Identify your network and the host requirements
  
  {Fore.RED}Example (Scenario: Your boss assigns you this task):

    {Fore.WHITE}IP Network: {Fore.LIGHTGREEN_EX}192.168.43.0/24
    {Fore.WHITE}Host List:

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}IT Department: {Fore.WHITE}64 Host
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}HR Department: {Fore.WHITE}32 Host
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}Finance Department: {Fore.WHITE}16 Host
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}Guest Wifi: {Fore.WHITE}8 Host

  {Fore.RED}Details for Each Subnets:

    {Fore.LIGHTCYAN_EX}Subnet (1, 2, 3, 4):

      {Fore.WHITE}Network Address:
      {Fore.WHITE}Broadcast Address:
      {Fore.WHITE}Subnet Mask:
      {Fore.WHITE}Prefix Length:
      {Fore.WHITE}Number of Available Host:
      {Fore.WHITE}"Usable IP Range:

{Fore.LIGHTMAGENTA_EX}Step 2: {Fore.LIGHTCYAN_EX}Identify every host bits needed in every host

  {Fore.MAGENTA}- {Fore.WHITE}Use the formula {Fore.GREEN}2 ^ b {Fore.WHITE}(where {Fore.GREEN}'b' {Fore.WHITE}is the host bits)
    
    {Fore.RED}Example:
    
      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}IT Department: {Fore.WHITE}64 Host
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}HR Department: {Fore.WHITE}32 Host
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}Finance Department: {Fore.WHITE}16 Host
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}Guest Wifi: {Fore.WHITE}8 Host

    {Fore.RED}Formula ({Fore.LIGHTCYAN_EX}2 ^ b{Fore.RED}):

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}2 ^ 6 {Fore.WHITE}= {Fore.GREEN}64 {Fore.WHITE}({Fore.GREEN}6 {Fore.WHITE}is the {Fore.GREEN}host bits {Fore.WHITE}needed)
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}2 ^ 5 {Fore.WHITE}= {Fore.GREEN}32 {Fore.WHITE}({Fore.GREEN}5 {Fore.WHITE}is the {Fore.GREEN}host bits {Fore.WHITE}needed)
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}2 ^ 4 {Fore.WHITE}= {Fore.GREEN}16 {Fore.WHITE}({Fore.GREEN}4 {Fore.WHITE}is the {Fore.GREEN}host bits {Fore.WHITE}needed)
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}2 ^ 3 {Fore.WHITE}= {Fore.GREEN}8  {Fore.WHITE}({Fore.GREEN}3 {Fore.WHITE}is the {Fore.GREEN}host bits {Fore.WHITE}needed)

{Fore.LIGHTMAGENTA_EX}Step 3: {Fore.LIGHTCYAN_EX}Identifying the Prefix Length

  {Fore.MAGENTA}- {Fore.WHITE}Now that we have determined the required host bits, we can calculate the {Fore.GREEN}subnet prefix length {Fore.WHITE}for each subnet.
  {Fore.MAGENTA}- {Fore.WHITE}Use the formula {Fore.GREEN}32 - b {Fore.WHITE}(where {Fore.GREEN}'32' {Fore.WHITE}is the {Fore.GREEN}prefix length of single IP Address {Fore.WHITE}and {Fore.GREEN}'b' {Fore.WHITE}is the host bits)

    {Fore.RED}Formula ({Fore.LIGHTCYAN_EX}32 - b{Fore.RED}):

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}32 - 6 {Fore.WHITE}= {Fore.GREEN + "26"} {Fore.WHITE}({Fore.GREEN}/26 {Fore.WHITE}is the {Fore.GREEN}prefix length{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}32 - 5 {Fore.WHITE}= {Fore.GREEN + "27"} {Fore.WHITE}({Fore.GREEN}/27 {Fore.WHITE}is the {Fore.GREEN}prefix length{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}32 - 4 {Fore.WHITE}= {Fore.GREEN + "28"} {Fore.WHITE}({Fore.GREEN}/28 {Fore.WHITE}is the {Fore.GREEN}prefix length{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}32 - 3 {Fore.WHITE}= {Fore.GREEN + "29"} {Fore.WHITE}({Fore.GREEN}/29 {Fore.WHITE}is the {Fore.GREEN}prefix length{Fore.WHITE})

{Fore.LIGHTMAGENTA_EX}Step 4: {Fore.LIGHTCYAN_EX}Identifying the Subnet Masks
  
  {Fore.MAGENTA}- {Fore.WHITE}Now that we have determined the prefix length, we can now determine the {Fore.GREEN}subnet mask for each prefix length{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}When converting an IP address into binary, each octet contains {Fore.GREEN}8 bits{Fore.WHITE}. It looks like this:
    {Fore.GREEN}xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
  {Fore.MAGENTA}- {Fore.WHITE}Convert the {Fore.GREEN}prefix length into binary{Fore.WHITE}:
    
    {Fore.RED}Example:

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}/26 {Fore.WHITE}= {Fore.GREEN}11111111.11111111.11111111.11000000 {Fore.WHITE}(Write {Fore.GREEN}26 ones(1){Fore.WHITE}, and the rest is {Fore.GREEN}zeros(0){Fore.WHITE})
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}/27 {Fore.WHITE}= {Fore.GREEN}11111111.11111111.11111111.11100000 {Fore.WHITE}(Write {Fore.GREEN}27 ones(1){Fore.WHITE}, and the rest is {Fore.GREEN}zeros(0){Fore.WHITE})
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}/28 {Fore.WHITE}= {Fore.GREEN}11111111.11111111.11111111.11110000 {Fore.WHITE}(Write {Fore.GREEN}28 ones(1){Fore.WHITE}, and the rest is {Fore.GREEN}zeros(0){Fore.WHITE})
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}/29 {Fore.WHITE}= {Fore.GREEN}11111111.11111111.11111111.11111000 {Fore.WHITE}(Write {Fore.GREEN}29 ones(1){Fore.WHITE}, and the rest is {Fore.GREEN}zeros(0){Fore.WHITE})

  {Fore.MAGENTA}- {Fore.WHITE}Convert that {Fore.GREEN}binary into decimal {Fore.WHITE}now. To do this, follow these steps:

    {Fore.LIGHTGREEN_EX}2**7 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}128
    {Fore.LIGHTGREEN_EX}2**6 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}64
    {Fore.LIGHTGREEN_EX}2**5 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}32            
    {Fore.LIGHTGREEN_EX}2**4 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}16                           
    {Fore.LIGHTGREEN_EX}2**3 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}8
    {Fore.LIGHTGREEN_EX}2**2 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}4
    {Fore.LIGHTGREEN_EX}2**1 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}2
    {Fore.LIGHTGREEN_EX}2**0 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}1   
                    
     ------------------------------------      
    | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
     ------------------------------------

    {Fore.RED}Example:

      {Fore.LIGHTGREEN_EX}11111110

      {Fore.RED}Process: {Fore.WHITE}Imagine every bits in {Fore.GREEN}11111110 {Fore.WHITE}as {Fore.GREEN}128{Fore.WHITE}, {Fore.GREEN}28{Fore.WHITE}, {Fore.WHITE}and so on ({Fore.GREEN}besides 0{Fore.WHITE}).

        {Fore.LIGHTGREEN_EX}1(128) + 1(64) + 1(32) + 1(16) + 1(8) + 1(4) + 1(2) + 0(0) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}254 in decimal

      {Fore.WHITE}Now, for {Fore.GREEN}11111111.11111111.11111111.11000000{Fore.WHITE}, break it into {Fore.GREEN}4 octets{Fore.WHITE}:
      
      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}11111111 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}11111111 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}11111111 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}11000000 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192
      {Fore.RED}Note: {Fore.WHITE}The first bit on the left is always {Fore.GREEN}128{Fore.WHITE}.
      
      {Fore.LIGHTCYAN_EX}Subnet Mask Result: {Fore.LIGHTGREEN_EX}255.255.255.192

  {Fore.MAGENTA}- {Fore.WHITE}Now, for every {Fore.GREEN}binary address of prefix length{Fore.WHITE}, here is the decimal result:

    {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}11111111.11111111.11111111.11000000 {Fore.WHITE}({Fore.GREEN}/26 {Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255.255.255.192
    {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}11111111.11111111.11111111.11100000 {Fore.WHITE}({Fore.GREEN}/27 {Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255.255.255.224
    {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}11111111.11111111.11111111.11110000 {Fore.WHITE}({Fore.GREEN}/28 {Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255.255.255.240
    {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}11111111.11111111.11111111.11111000 {Fore.WHITE}({Fore.GREEN}/29 {Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}255.255.255.248

{Fore.LIGHTMAGENTA_EX}Step 5: {Fore.LIGHTCYAN_EX}Incrementing

  {Fore.MAGENTA}- {Fore.WHITE}Now that we have determined the hosts for each prefix length, we can calculate the {Fore.GREEN}subnet increments{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}To do this, start with the {Fore.GREEN}given IP network {Fore.WHITE}from the step 1: {Fore.LIGHTGREEN_EX}192.168.43.0/24{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}Instead of using /24 in 192.168.43.0/24, we will use the {Fore.GREEN}smallest subnet with the highest prefix length{Fore.WHITE},
    which is {Fore.GREEN}/26{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}This is because {Fore.GREEN}/24 {Fore.WHITE}represents the {Fore.GREEN}total network range{Fore.WHITE}, while {Fore.GREEN}/26 {Fore.WHITE}defines a {Fore.GREEN}subnet within that range{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}To increment, start with the first subnet {Fore.GREEN}192.168.43.0/26
  {Fore.MAGENTA}- {Fore.WHITE}Next is use the formula {Fore.GREEN}192.168.43.X + b {Fore.WHITE}(where {Fore.GREEN}'X' {Fore.WHITE}is the {Fore.GREEN}last assigned subnet address{Fore.WHITE}, while {Fore.GREEN}'b' {Fore.WHITE}is the
    {Fore.GREEN}block size of the previous subnet's prefix length.{Fore.WHITE})
    
    {Fore.RED}Process:
      
      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.43.0/26
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.43.0 + 64 {Fore.WHITE}({Fore.GREEN}Block size of /26{Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.64
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.43.64 + 32 {Fore.WHITE}({Fore.GREEN}Block size of /27{Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.96
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.96 + 16 {Fore.WHITE}({Fore.GREEN}Block size of /28{Fore.WHITE}) {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.112
    
    {Fore.RED}Result:

      {Fore.LIGHTGREEN_EX}1. {Fore.WHITE}192.168.43.0/26
      {Fore.LIGHTGREEN_EX}2. {Fore.WHITE}192.168.43.64/27
      {Fore.LIGHTGREEN_EX}3. {Fore.WHITE}192.168.43.96/28
      {Fore.LIGHTGREEN_EX}4. {Fore.WHITE}192.168.43.112/29

{Fore.LIGHTMAGENTA_EX}Step 6: {Fore.LIGHTCYAN_EX}Identifying the Network Address and Broadcast Address
  
  {Fore.MAGENTA}- {Fore.WHITE}Now that we've finished incrementing the subnets, we can easily determine the {Fore.GREEN}Network and Broadcast Address
    for each one.
  {Fore.MAGENTA}- {Fore.WHITE}To do this, follow this process:

    {Fore.LIGHTGREEN_EX}Identifying Network Address:

      {Fore.RED}Remember:

        {Fore.MAGENTA}- {Fore.WHITE}Every subnet result from {Fore.GREEN}Step 5 (incrementing) {Fore.WHITE}is already the {Fore.GREEN}Network Address of that subnet{Fore.WHITE}.
        {Fore.MAGENTA}- {Fore.WHITE}All you need to do is {Fore.GREEN}remove the prefix length{Fore.WHITE}, and you get the {Fore.GREEN}network address{Fore.WHITE}.

      {Fore.RED}Removing prefix length:

        {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.43.0/26 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.0 {Fore.WHITE}({Fore.GREEN}Network Address of Subnet 1{Fore.WHITE})
        {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.43.64/27 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.64 {Fore.WHITE}({Fore.GREEN}Network Address of Subnet 2{Fore.WHITE})
        {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.43.96/28 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.96 {Fore.WHITE}({Fore.GREEN}Network Address of Subnet 3{Fore.WHITE})
        {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.112/29 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.112 {Fore.WHITE}({Fore.GREEN}Network Address of Subnet 4{Fore.WHITE})

    {Fore.LIGHTGREEN_EX}Identifying Broadcast Address:

      {Fore.RED}Remember:

        {Fore.MAGENTA}- {Fore.WHITE}Every {Fore.GREEN}last IP Address in every subnet {Fore.WHITE}is already the {Fore.GREEN}Broadcast Address of that subnet{Fore.WHITE}.
        {Fore.MAGENTA}- {Fore.WHITE}To know {Fore.GREEN}every last IP Address{Fore.WHITE}, use this formula:

      {Fore.RED}Formula:

        {Fore.LIGHTCYAN_EX}192.168.43.X + b -1 {Fore.WHITE}(where {Fore.GREEN}'X' {Fore.WHITE}is the {Fore.GREEN}Network Address of a subnet{Fore.WHITE}, while {Fore.GREEN}'b' {Fore.WHITE}is the
        {Fore.GREEN}block size of every prefix length subnet{Fore.WHITE})

        {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.43.0/26 {Fore.WHITE}-> {Fore.GREEN}192.168.43.0 + 64 -1 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.63 {Fore.WHITE}({Fore.GREEN}Broadcast Address of 1st Subnet{Fore.WHITE})
        {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.43.64/27 {Fore.WHITE}-> {Fore.GREEN}192.168.43.64 + 32 -1 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.95 {Fore.WHITE}({Fore.GREEN}Broadcast Address of 2nd Subnet{Fore.WHITE})
        {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.43.96/28 {Fore.WHITE}-> {Fore.GREEN}192.168.43.96 + 16 -1 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.111 {Fore.WHITE}({Fore.GREEN}Broadcast Address of 3rd Subnet{Fore.WHITE})
        {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.112/29 {Fore.WHITE}-> {Fore.GREEN}192.168.43.112 + 8 -1 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}192.168.43.119 {Fore.WHITE}({Fore.GREEN}Broadcast Address of 4th Subnet{Fore.WHITE})

{Fore.LIGHTMAGENTA_EX}Step 7: {Fore.LIGHTCYAN_EX}Identifying the host range

  {Fore.MAGENTA}- {Fore.WHITE}Now that we know the network address and broadcast address, we can easily identify the {Fore.GREEN}usable IP range {Fore.WHITE}for each
    subnet.
  {Fore.MAGENTA}- {Fore.WHITE}Use the formula {Fore.GREEN}Network Address +1 {Fore.WHITE}and {Fore.GREEN}Broadcast Address -1 {Fore.WHITE}to identify the {Fore.GREEN}IP Range of every subnet

    {Fore.RED}Process:

    {Fore.LIGHTGREEN_EX}1.
      {Fore.WHITE}Network Address: {Fore.LIGHTCYAN_EX}192.168.43.0 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.0 +1
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTCYAN_EX}192.168.43.63 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.63 -1
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.1 - 192.168.43.62

    {Fore.LIGHTGREEN_EX}2.
      {Fore.WHITE}Network Address: {Fore.LIGHTCYAN_EX}192.168.43.64 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.63 +1
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTCYAN_EX}192.168.43.95 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.95 -1
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.65 - 192.168.43.94

    {Fore.LIGHTGREEN_EX}3.
      {Fore.WHITE}Network Address: {Fore.LIGHTCYAN_EX}192.168.43.96 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.96 +1
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTCYAN_EX}192.168.43.111 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.111 -1
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.97 - 192.168.43.110

    {Fore.LIGHTGREEN_EX}4.
      {Fore.WHITE}Network Address: {Fore.LIGHTCYAN_EX}192.168.43.112 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.112 +1
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTCYAN_EX}192.168.43.119 {Fore.WHITE}-> {Fore.LIGHTGREEN_EX}192.168.43.119 -1
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.113 - 192.168.43.118

{Fore.LIGHTMAGENTA_EX}Step 8: {Fore.LIGHTCYAN_EX}Identifying the usable hosts

  {Fore.MAGENTA}- {Fore.WHITE}Now that we know the network address and broadcast address, we can easily determine the {Fore.GREEN}usable hosts in each
    subnet.
  {Fore.MAGENTA}- {Fore.WHITE}Use the formula: {Fore.GREEN}2^b - 2 {Fore.WHITE}(where {Fore.GREEN}'b' {Fore.WHITE}is the {Fore.GREEN}host bits for each subnet{Fore.WHITE}).

    {Fore.RED}Process:

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}64 Hosts {Fore.WHITE}(for {Fore.GREEN}/26{Fore.WHITE}) → {Fore.GREEN}2^6 - 2 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}62 {Fore.WHITE}({Fore.GREEN}Usable Hosts in Subnet 1{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}32 Hosts {Fore.WHITE}(for {Fore.GREEN}/27{Fore.WHITE}) → {Fore.GREEN}2^6 - 2 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}30 {Fore.WHITE}({Fore.GREEN}Usable Hosts in Subnet 2{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}16 Hosts {Fore.WHITE}(for {Fore.GREEN}/28{Fore.WHITE}) → {Fore.GREEN}2^6 - 2 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}14 {Fore.WHITE}({Fore.GREEN}Usable Hosts in Subnet 3{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}8 Hosts {Fore.WHITE}(for {Fore.GREEN}/29{Fore.WHITE}) →  {Fore.GREEN}2^6 - 2 {Fore.WHITE}= {Fore.LIGHTGREEN_EX}6 {Fore.WHITE}({Fore.GREEN}Usable Hosts in Subnet 4{Fore.WHITE})

{Fore.LIGHTMAGENTA_EX}Step 9: {Fore.LIGHTCYAN_EX}Summarize the Result

  {Fore.WHITE}IP Network: {Fore.LIGHTGREEN_EX}192.168.43.0/24
  {Fore.WHITE}Host List:

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}IT Department: {Fore.WHITE}64 Host
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}HR Department: {Fore.WHITE}32 Host
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}Finance Department: {Fore.WHITE}16 Host
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}Guest Wifi: {Fore.WHITE}8 Host

  {Fore.RED}Result:

    {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}IT Department: {Fore.RED}192.168.43.0/26

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.0
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.63
      {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.192
      {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/26
      {Fore.WHITE}Usable Hosts: {Fore.LIGHTGREEN_EX}62
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.1 - 192.168.43.62

    {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}HR Department: {Fore.RED}192.168.43.64/27

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.64
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.95
      {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.224
      {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/27
      {Fore.WHITE}Usable Hosts: {Fore.LIGHTGREEN_EX}30
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.65 - 192.168.43.94

    {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}Finance Department: {Fore.RED}192.168.43.96/28

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.96
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.111
      {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.240
      {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/28
      {Fore.WHITE}Usable Hosts: {Fore.LIGHTGREEN_EX}14
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.97 - 192.168.43.110

    {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}Guest Wifi: {Fore.RED}192.168.43.112/29

      {Fore.WHITE}Network Address: {Fore.LIGHTGREEN_EX}192.168.43.112
      {Fore.WHITE}Broadcast Address: {Fore.LIGHTGREEN_EX}192.168.43.119
      {Fore.WHITE}Subnet Mask: {Fore.LIGHTGREEN_EX}255.255.255.248
      {Fore.WHITE}Prefix Length: {Fore.LIGHTGREEN_EX}/29
      {Fore.WHITE}Usable Hosts: {Fore.LIGHTGREEN_EX}6
      {Fore.WHITE}Host Range: {Fore.LIGHTGREEN_EX}192.168.43.113 - 192.168.43.118

{Fore.LIGHTMAGENTA_EX}Conclusion and Acknowledgements:
              
    {Fore.WHITE}This is how VLSM calculation works. As you can see, it can be quite complex when you do it
  from scratch, but it's essential to learn if you want to dive into networking and fields like ethical 
  hacking, and so on. But don't worry! IPnetSolver is here to assist you. You can use this tool as your 
  buddy to work together and automate the process. Just be sure to use it responsibly, okay?

  Thank you for reading, and I hope my IPnetSolver tool helps you. 
  - Reymond Joaquin""")
        separator()

    elif num == "3":
        separator()
        print(f"""{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}How to Calculate in Supernetting {Fore.MAGENTA}[*]
        
{Fore.LIGHTMAGENTA_EX}What is Supernetting?

  {Fore.WHITE}is a technique used to combine multiple subnets into a larger network
by increasing the subnet size and reducing the number of routing entries. 
It helps in efficient IP management and reduces routing complexity by merging 
smaller networks into one.
        
{Fore.LIGHTMAGENTA_EX}Step 1: {Fore.LIGHTCYAN_EX}Identify the subnets to be combined

  {Fore.RED}Example {Fore.RED}(Scenario Your boss assigns you this task):

    {Fore.LIGHTGREEN_EX}1. {Fore.WHITE}192.168.40.0/24
    {Fore.LIGHTGREEN_EX}2. {Fore.WHITE}192.168.41.0/24
    {Fore.LIGHTGREEN_EX}3. {Fore.WHITE}192.168.42.0/24
    {Fore.LIGHTGREEN_EX}4. {Fore.WHITE}192.168.43.0/24
        
{Fore.LIGHTMAGENTA_EX}Step 2: {Fore.LIGHTCYAN_EX}Convert the Subnets to Binary

  {Fore.MAGENTA}- {Fore.WHITE}We need to convert the {Fore.GREEN}network address of the subnets into binary {Fore.WHITE}to identify which bits are the same across all
    subnets.
  {Fore.MAGENTA}- {Fore.WHITE}The {Fore.GREEN}matching bits across all subnets {Fore.WHITE}will help us determine the {Fore.GREEN}new subnet mask for the supernet{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}Ignore the {Fore.GREEN}prefix length {Fore.WHITE}for now.

    {Fore.RED}Process:

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.40.0/24 {Fore.WHITE}-> {Fore.GREEN}192.168.40.0
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.41.0/24 {Fore.WHITE}-> {Fore.GREEN}192.168.41.0
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.42.0/24 {Fore.WHITE}-> {Fore.GREEN}192.168.42.0
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.0/24 {Fore.WHITE}-> {Fore.GREEN}192.168.44.0

  {Fore.MAGENTA}- {Fore.WHITE}Now we just need to {Fore.GREEN}convert it into binary
  {Fore.MAGENTA}- {Fore.WHITE}When converting an IP address into binary, each octet contains {Fore.GREEN}8 bits{Fore.WHITE}. It looks like this:
    {Fore.GREEN}xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
  {Fore.MAGENTA}- {Fore.WHITE}To convert IP Address into binary, we need know that every {Fore.GREEN}ones(1) {Fore.WHITE}bits in octets have {Fore.GREEN}value{Fore.WHITE}, while {Fore.GREEN}zeros(0)
    {Fore.WHITE}have {Fore.GREEN}none

    {Fore.LIGHTGREEN_EX}2**7 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}128
    {Fore.LIGHTGREEN_EX}2**6 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}64
    {Fore.LIGHTGREEN_EX}2**5 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}32              
    {Fore.LIGHTGREEN_EX}2**4 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}16                              
    {Fore.LIGHTGREEN_EX}2**3 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}8
    {Fore.LIGHTGREEN_EX}2**2 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}4
    {Fore.LIGHTGREEN_EX}2**1 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}2
    {Fore.LIGHTGREEN_EX}2**0 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}1     
                    
     ------------------------------------      
    | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
     ------------------------------------
            
  {Fore.MAGENTA}- {Fore.WHITE}Break every Network Address into {Fore.GREEN}4 octets{Fore.WHITE}:

    {Fore.RED}Example: {Fore.LIGHTCYAN_EX}192.168.40.0"

      {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192 {Fore.WHITE}= {Fore.GREEN}11000000 {Fore.WHITE}({Fore.GREEN}128 {Fore.WHITE}+ {Fore.GREEN}64 {Fore.WHITE}+ 0 + 0 + 0 + 0 + 0 + 0 = {Fore.LIGHTGREEN_EX}192{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}168 {Fore.WHITE}= {Fore.GREEN}11100000 {Fore.WHITE}({Fore.GREEN}128 {Fore.WHITE}+ {Fore.GREEN}64 {Fore.WHITE}+ {Fore.GREEN}32 {Fore.WHITE}+ 0 + 0 + 0 + 0 + 0 = {Fore.LIGHTGREEN_EX}168{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}40  {Fore.WHITE}= {Fore.GREEN}00101000 {Fore.WHITE}({Fore.WHITE}0 + 0 + {Fore.GREEN}32 {Fore.WHITE}+ 0 + {Fore.GREEN}8 {Fore.WHITE}+ 0 + 0 + 0 = {Fore.LIGHTGREEN_EX}40{Fore.WHITE})
      {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}0   {Fore.WHITE}= {Fore.GREEN}00000000 {Fore.WHITE}({Fore.WHITE}0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = {Fore.LIGHTGREEN_EX}0{Fore.WHITE})
          
    {Fore.RED}Result: {Fore.GREEN}11000000.11100000.00101000.00000000
  
  {Fore.MAGENTA}- {Fore.WHITE}Now just follow the steps above and here is the {Fore.GREEN}binary results{Fore.WHITE}:
         
    {Fore.LIGHTGREEN_EX}1. {Fore.LIGHTCYAN_EX}192.168.40.0 {Fore.WHITE}= {Fore.GREEN}11000000.10101000.00101000.00000000
    {Fore.LIGHTGREEN_EX}2. {Fore.LIGHTCYAN_EX}192.168.41.0 {Fore.WHITE}= {Fore.GREEN}11000000.10101000.00101001.00000000
    {Fore.LIGHTGREEN_EX}3. {Fore.LIGHTCYAN_EX}192.168.42.0 {Fore.WHITE}= {Fore.GREEN}11000000.10101000.00101010.00000000
    {Fore.LIGHTGREEN_EX}4. {Fore.LIGHTCYAN_EX}192.168.43.0 {Fore.WHITE}= {Fore.GREEN}11000000.10101000.00101011.00000000
      
{Fore.LIGHTMAGENTA_EX}Step 3: {Fore.LIGHTCYAN_EX}Identify the Matching Bits in Every Binary Address
              
  {Fore.MAGENTA}- {Fore.WHITE}After converting the Network Addresses into binary, we can now identify the {Fore.GREEN}matching bits across all subnets{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}The matching bits will determine the {Fore.GREEN}new subnet prefix length for the supernet{Fore.WHITE}.
  {Fore.MAGENTA}- {Fore.WHITE}To do this, compare each {Fore.GREEN}binary address bit by bit {Fore.WHITE}and {Fore.GREEN}count how many bits remain the same{Fore.WHITE}. Ignore the
    differing bits.     

    {Fore.RED}Process:

      {Fore.MAGENTA}Before: {Fore.LIGHTCYAN_EX}List all binary addresses (from Step 2):
                      
        {Fore.GREEN}11000000.10101000.00101000.00000000
        11000000.10101000.00101001.00000000
        11000000.10101000.00101010.00000000
        11000000.10101000.00101011.00000000
      
      {Fore.MAGENTA}After: {Fore.LIGHTCYAN_EX}Separate the matching and non-matching bits:

            {Fore.WHITE}Matching Bits           Changing Bits
              
        {Fore.GREEN}11000000.10101000.00101  {Fore.WHITE}|  {Fore.GREEN}000.00000000
        {Fore.GREEN}11000000.10101000.00101  {Fore.WHITE}|  {Fore.GREEN}001.00000000
        {Fore.GREEN}11000000.10101000.00101  {Fore.WHITE}|  {Fore.GREEN}010.00000000
        {Fore.GREEN}11000000.10101000.00101  {Fore.WHITE}|  {Fore.GREEN}011.00000000
  
  {Fore.MAGENTA}- {Fore.WHITE}Now count The {Fore.GREEN}Matching Bits {Fore.WHITE}(Only the {Fore.GREEN}above Binary Address{Fore.WHITE}, not all Binary Address since they are similar)
    
    {Fore.RED}Process:
              
            {Fore.WHITE}Matching Bits
              
      {Fore.GREEN}11000000.10101000.00101
      11000000.10101000.00101    
      11000000.10101000.00101    
      11000000.10101000.00101
              
    {Fore.RED}Result: {Fore.GREEN}22 {Fore.WHITE}(This means the new prefix length for the supernet is {Fore.GREEN}/22{Fore.WHITE})

{Fore.LIGHTMAGENTA_EX}Step 4: {Fore.LIGHTCYAN_EX}Determine the Supernet Address
              
  {Fore.MAGENTA}- {Fore.WHITE}Now that we know the matching bits from Step 3 (which gave us a /22 prefix), we can determine the {Fore.GREEN}final supernet
    address.
  {Fore.MAGENTA}- {Fore.WHITE}The {Fore.GREEN}supernet address {Fore.WHITE}is simply the {Fore.GREEN}first network address {Fore.WHITE}({Fore.GREEN}smallest IP{Fore.WHITE}) in the group, but with the new {Fore.GREEN}/22 prefix{Fore.WHITE}.

    {Fore.RED}Process:
      
      {Fore.LIGHTGREEN_EX}1. {Fore.YELLOW}Take the first subnet from Step 1:
              
        {Fore.WHITE}192.168.40.0/24
      
      {Fore.LIGHTGREEN_EX}2. {Fore.YELLOW}Apply the new prefix length from Step 3:
      
        {Fore.WHITE}192.168.40.0/24 {Fore.RED}-> {Fore.WHITE}192.168.40.0/22
    
      {Fore.LIGHTGREEN_EX}3. {Fore.YELLOW}Final Result or Supernet Result:
              
        {Fore.WHITE}192.168.40.0/22

{Fore.LIGHTMAGENTA_EX}Conclusion and Acknowledgements:
              
    {Fore.WHITE}This is how Supernetting calculation works. As you can see, it can be quite complex when you do it
  from scratch, but it's essential to learn if you want to dive into networking and fields like ethical 
  hacking, and so on. But don't worry! IPnetSolver is here to assist you. You can use this tool as your 
  buddy to work together and automate the process. Just be sure to use it responsibly, okay?

  Thank you for reading, and I hope my IPnetSolver tool helps you. 
  - Reymond Joaquin""")
        separator()

    elif num == "4":
        separator()
        print(f"""{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}How to Convert Whole Numbers into Binary {Fore.MAGENTA}[*]
                
{Fore.LIGHTMAGENTA_EX}Step 1: {Fore.LIGHTCYAN_EX}Choose a whole number to convert to binary.
              
  {Fore.RED}Example:
    
    {Fore.WHITE}442
              
{Fore.LIGHTMAGENTA_EX}Step 2: {Fore.LIGHTCYAN_EX}Divide the number by 2 repeatedly and note the remainders.
  
    {Fore.MAGENTA}- {Fore.WHITE}Use the formula: {Fore.GREEN}Whole Number ÷ 2
    {Fore.MAGENTA}- {Fore.WHITE}Keep dividing the number by {Fore.GREEN + "2"}{Fore.WHITE}, and for each step, write down the remainder ({Fore.GREEN}0 or 1{Fore.WHITE}).
    {Fore.MAGENTA}- {Fore.WHITE}Continue dividing until you reach {Fore.GREEN}0{Fore.WHITE}.
              
      {Fore.RED}Process:
        
        {Fore.LIGHTGREEN_EX}442 ÷ 2 {Fore.WHITE}= {Fore.GREEN}221   {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}0
        {Fore.LIGHTGREEN_EX}221 ÷ 2 {Fore.WHITE}= {Fore.GREEN}110   {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}1 
        {Fore.LIGHTGREEN_EX}110 ÷ 2 {Fore.WHITE}= {Fore.GREEN}55    {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}0
        {Fore.LIGHTGREEN_EX}55 ÷ 2  {Fore.WHITE}= {Fore.GREEN}27    {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}1 
        {Fore.LIGHTGREEN_EX}27 ÷ 2  {Fore.WHITE}= {Fore.GREEN}13    {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}1 
        {Fore.LIGHTGREEN_EX}13 ÷ 2  {Fore.WHITE}= {Fore.GREEN}6     {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}1 
        {Fore.LIGHTGREEN_EX}6 ÷ 2   {Fore.WHITE}= {Fore.GREEN}3     {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}0
        {Fore.LIGHTGREEN_EX}3 ÷ 2   {Fore.WHITE}= {Fore.GREEN}1     {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}1 
        {Fore.LIGHTGREEN_EX}1 ÷ 2   {Fore.WHITE}= {Fore.GREEN}0     {Fore.YELLOW}remainder {Fore.WHITE}→ {Fore.LIGHTGREEN_EX}1   {Fore.WHITE}({Fore.LIGHTCYAN_EX}Stop here{Fore.WHITE})
          
{Fore.LIGHTMAGENTA_EX}Step 3:  {Fore.LIGHTCYAN_EX}Reverse the Remainders
              
  {Fore.MAGENTA}- {Fore.WHITE}The binary number is formed by reading the remainders from {Fore.GREEN}bottom to top{Fore.WHITE}.
      
    {Fore.RED}Result:

      {Fore.GREEN}442 {Fore.WHITE}({Fore.GREEN}Decimal{Fore.WHITE}) → {Fore.LIGHTGREEN_EX}110111010 {Fore.WHITE}({Fore.LIGHTGREEN_EX}Binary{Fore.WHITE})
      
{Fore.LIGHTMAGENTA_EX}Step 4: {Fore.LIGHTCYAN_EX}Verify the Binary Conversion (Optional)
              
  {Fore.MAGENTA}- {Fore.WHITE}To check if the conversion is correct, convert {Fore.GREEN}110111010 (Binary) back to Decimal{Fore.WHITE}:
    {Fore.RED}Process:

      {Fore.LIGHTGREEN_EX}(1 * 2⁸) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}256
      {Fore.LIGHTGREEN_EX}(1 * 2⁷) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}128
      {Fore.LIGHTGREEN_EX}(0 * 2⁶) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}0
      {Fore.LIGHTGREEN_EX}(1 * 2⁵) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}32
      {Fore.LIGHTGREEN_EX}(1 * 2⁴) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}16
      {Fore.LIGHTGREEN_EX}(1 * 2³) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}8
      {Fore.LIGHTGREEN_EX}(0 * 2²) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}0
      {Fore.LIGHTGREEN_EX}(1 * 2¹) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}2
      {Fore.LIGHTGREEN_EX}(0 * 2⁰) {Fore.WHITE}= {Fore.LIGHTCYAN_EX}0

        
      {Fore.LIGHTGREEN_EX}256 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}128 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}0 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}32 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}16 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}8 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}0 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}2 {Fore.WHITE}+ {Fore.LIGHTGREEN_EX}0 {Fore.WHITE}= {Fore.LIGHTCYAN_EX}442 {Fore.WHITE}({Fore.GREEN}Correct!{Fore.WHITE})

              
{Fore.MAGENTA}[*] {Fore.LIGHTCYAN_EX}How to Convert an IP Address into Binary {Fore.MAGENTA}[*]
              
{Fore.LIGHTMAGENTA_EX}Step 1: {Fore.LIGHTCYAN_EX}Understand the Structure of an IP Address
              
  {Fore.MAGENTA}- {Fore.WHITE}An {Fore.GREEN}IPv4 address {Fore.WHITE}consists of {Fore.GREEN}four octets{Fore.WHITE}, each separated by {Fore.GREEN}dots {Fore.WHITE}(.).
  {Fore.MAGENTA}- {Fore.WHITE}Each octet is an {Fore.GREEN}8-bit number {Fore.WHITE}(ranging from {Fore.GREEN}0-255{Fore.WHITE}).
      
    {Fore.RED}Example:
      
      {Fore.WHITE}192.168.40.0
              
{Fore.LIGHTMAGENTA_EX}Step 2: {Fore.LIGHTCYAN_EX}Convert Each Octet to Binary
              
  {Fore.MAGENTA}- {Fore.WHITE}Convert each decimal octet into an 8-bit binary number by using the {Fore.GREEN}powers of 2 method{Fore.WHITE}:
      
    {Fore.RED}Binary Values per Bit:
        
      {Fore.LIGHTGREEN_EX}2⁷ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}128 
      {Fore.LIGHTGREEN_EX}2⁶ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}64 
      {Fore.LIGHTGREEN_EX}2⁵ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}32 
      {Fore.LIGHTGREEN_EX}2⁴ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}16 
      {Fore.LIGHTGREEN_EX}2³ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}8 
      {Fore.LIGHTGREEN_EX}2² {Fore.WHITE}= {Fore.LIGHTCYAN_EX}4 
      {Fore.LIGHTGREEN_EX}2¹ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}2
      {Fore.LIGHTGREEN_EX}2⁰ {Fore.WHITE}= {Fore.LIGHTCYAN_EX}1
              
    {Fore.RED}Example: {Fore.WHITE}Convert {Fore.GREEN}192.168.40.0 {Fore.WHITE}into {Fore.GREEN}Binary
    
      {Fore.LIGHTGREEN_EX}92  {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}11000000
      {Fore.LIGHTGREEN_EX}168 {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}10101000
      {Fore.LIGHTGREEN_EX}40  {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}00101000
      {Fore.LIGHTGREEN_EX}0   {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}00000000
          
{Fore.LIGHTMAGENTA_EX}Step 3: {Fore.LIGHTCYAN_EX}Combine All Binary Octets
        
  {Fore.MAGENTA}- {Fore.WHITE}Join all the {Fore.GREEN}binary octets together with {Fore.GREEN}dots {Fore.WHITE}({Fore.GREEN}.{Fore.WHITE}) to form the {Fore.GREEN}full binary IP address{Fore.WHITE}:
      
    {Fore.LIGHTGREEN_EX}192.168.40.0  {Fore.WHITE}→  {Fore.LIGHTCYAN_EX}11000000.10101000.00101000.00000000
              
{Fore.LIGHTMAGENTA_EX}Step 4: {Fore.LIGHTCYAN_EX}Apply the Same Method to Any IP Address
            
  {Fore.MAGENTA}- {Fore.WHITE}You can use the {Fore.GREEN}same method {Fore.WHITE}to convert any IP address into binary.
        
    {Fore.RED}Example:
              
      {Fore.RED}IP: {Fore.WHITE}172.16.5.1
              
      {Fore.LIGHTGREEN_EX}172 {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}10101100
      {Fore.LIGHTGREEN_EX}16  {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}00010000
      {Fore.LIGHTGREEN_EX}5   {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}00000101
      {Fore.LIGHTGREEN_EX}1   {Fore.WHITE}→ {Fore.LIGHTCYAN_EX}00000001
              
    {Fore.RED}Final Binary Representation:
              
      {Fore.WHITE}172.16.5.1  →  {Fore.LIGHTCYAN_EX}10101100.00010000.00000101.00000001

{Fore.LIGHTMAGENTA_EX}Conclusion and Acknowledgements:
      
    {Fore.WHITE}This is how converting IP Addresses/Whole Number into binary works. As you can see, it 
  can be quite complex when you do it from scratch, but it's essential to learn if you want to dive into 
  networking and fields like ethical hacking, and so on. But don't worry! IPnetSolver is here to assist you. 
  You can use this tool as your buddy to work together and automate the process. Just be sure to use it responsibly, 
  okay?

  Thank you for reading, and I hope my IPnetSolver tool helps you. 
  - Reymond Joaquin""")
        separator()

