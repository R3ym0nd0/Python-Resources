import subprocess as SP

try:

 while True:
      
      question = input("Type Nmap Command -sn/-sp/-o: ")
      
      if question in ["-sn", "-o", "-sp"]:
       IP_Address = input(f"nmap {question}: ").strip()
       
       if IP_Address.strip():
       
         Command = ["nmap", question, IP_Address]
         result = SP.run(Command, capture_output=True, text=True)
         print(result.stdout)
         print(result.stderr)
         
         while True:
           ask_scan_ports = input("Do you want to Scan Ports: ")
           
           if ask_scan_ports == "yes".lower():
           
             target_ip_address = input("Type IP Address you want to scan ports: ")
             
             if target_ip_address.strip():          
                Commands = ["nmap", target_ip_address]
                result = SP.run(Commands, capture_output=True, text=True)
                print(result.stdout)
                print(result.stderr)
                
             elif target_ip_address == "":
                print("Put some IP address!")
             
           elif ask_scan_ports == "":
             print("Just say Yes or NO!")
                 
           elif ask_scan_ports == "no".lower():
             print("Scanning Ports Cancel")
             break  
             
           else:
             print("Yes or No Only!")               
         
         while True:
         
           asking = input("Do You Want To Continue: ")
         
           if asking == "yes".lower():
            break
           elif asking == "no".lower():
            print("Bye!")
            exit()
           else:
            print(f"Yes or No Only! not {asking}")
            
       else:
         print("Put any IP Adress!")
        
      else:
       print("-sn, -sp, -os ONLY!")
      
except Exception as error:
    print(f"Something went wrong: {error}")



