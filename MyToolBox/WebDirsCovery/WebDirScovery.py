import requests as rq
import socket
import os

from colorama import Fore, init
from typing import Union

# Automatically resets the color after each print statement
init(autoreset=True) 

# Get the terminal width for centering text
terminal_width: int = os.get_terminal_size().columns

def WebDirsCovery() -> None:
    def tool_intro() -> None:
        tool_name = Fore.LIGHTRED_EX + r"""
 __          __ ___   ______  _           ______                          
 \ \        / / | |   |  __ \(_)         / ____|                         
  \ \  /\  / /__| |__ | |  | |_ _ __ ___| |     _____   _____ _ __ _   _ 
   \ \/  \/ / _ \ '_ \| |  | | | '__/ __| |    / _ \ \ / / _ \ '__| | | |
    \  /\  /  __/ |_) | |__| | | |  \__ \ |___| (_) \ V /  __/ |  | |_| |
     \/  \/ \___|_.__/|_____/|_|_|  |___/\_____\___/ \_/ \___|_|   \__, |
                                                                    __/ |
                                                                   |___/ 
        """
        separator()
        print(tool_name)
        separator()
        print(Fore.RED + f"[*] {Fore.YELLOW + "Tool Name:"} {Fore.LIGHTGREEN_EX + "WebDirsCovery"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Version:"} {Fore.LIGHTGREEN_EX + "1.0"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Coded By:"} {Fore.LIGHTGREEN_EX + "Reymond Joaquin"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Description:"} {Fore.LIGHTGREEN_EX + "WebDirsCovery is a tool designed to identify and discover hidden directories on web servers"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Purpose:"} {Fore.LIGHTGREEN_EX + "For ethical hacking and penetration testing to uncover security vulnerabilities in web applications."}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Disclaimer:"} {Fore.LIGHTGREEN_EX + "Please use responsibly and ensure you have permission before scanning any website."}")
        separator()

    def enter_target() -> Union[str, socket.gethostbyname, None]:
        while True:
            tool_intro()
            try:
                user: str = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + "Enter the domain name (Type 'q' to quit)"}: ").strip().lower()
                if user == "q":
                    exit()
                elif user == "":
                    print("Please Enter Your Target")
                else:
                    socket.gethostbyname(user)
                    separator()
                    return user 
            except socket.gaierror:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please type a valid domain name or check your internet connection"} {Fore.RED + "!!"}")

    def option() -> str:
        while True:
            print(f"{Fore.RED + "[*]"} {Fore.YELLOW + "CHOOSE A DIRECTORY SCANNER"}\n")

            print(f"{Fore.LIGHTMAGENTA_EX + "[1]"} {Fore.LIGHTCYAN_EX + "Automated Directory Scan (This will automatically scan common directories on a website)"}")
            print(f"{Fore.LIGHTMAGENTA_EX + "[2]"} {Fore.LIGHTCYAN_EX  + "Custom Directory Scan (You need to enter your own list of directories)"}")
            print(f"{Fore.LIGHTMAGENTA_EX + "[3]"} {Fore.LIGHTCYAN_EX + "Manual Directory Scan (You need to enter a specific directory)"}")
            separator()

            user_option: str = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + "Choose an option (Type 1 - 3 or 'q' to quit)"}: ").strip().lower()
            
            if user_option in ["1", "2", "3", "q"]:
                return user_option
            else:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Invalid Option, Please try again"} {Fore.RED + "!!"}")
                separator()

    def Automated_Directory_Scan(user: str) -> list[str]:
        OK_url: list[str] = []
        forbidden_url: list[str] = []
        moved_permanent_url: list[str] = []
        list_directories: list[str] = [
                            # General Directories
                            "admin",
                            "login",
                            "dashboard",
                            "config",
                            "backup",
                            "uploads",
                            "assets",
                            "css",
                            "js",
                            "images",

                            # Sensitive Files
                            ".git",
                            ".env",
                            ".htaccess",
                            ".htpasswd",

                            # WordPress
                            "wp-admin",
                            "wp-content",
                            "wp-includes",
                            "wp-login.php",
                            "xmlrpc.php",

                            # Joomla
                            "administrator",
                            "components",
                            "modules",
                            "plugins",

                            # Deprecated Directories
                            "old",
                            "test",
                            "dev",
                            "staging",

                            # Panels
                            "phpmyadmin",
                            "cpanel"
                            ]

        separator()
        print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Scanning Automatically directories, checking status codes...."}\n")

        for directory in list_directories:
            try:
                full_url: str = f"https://{user}/{directory.strip()}"
                base_url = rq.get(full_url)
                status_code: int = base_url.status_code

                print(f"{Fore.LIGHTGREEN_EX + "[URL]"} {Fore.LIGHTCYAN_EX + full_url} - {Fore.WHITE + "Status Code: "} {status_code_color(base_url)}")
                check_status_code(status_code, OK_url, forbidden_url, moved_permanent_url, full_url)

            except rq.exceptions.ConnectionError:
                print(f"[URL] {full_url} - Status Code: {Fore.RED + "Connection Error"}")

        separator()
        return OK_url, forbidden_url, moved_permanent_url

    def Custom_Directory_Scan(user: str) -> None:
        OK_url: list = []
        forbidden_url: list = []
        moved_permanent_url: list = []

        while True:
            try:
                directories: str = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + "Enter the file path containing your list of directory paths (Type 'q' to quit):"} ").strip()
                if directories == "q":
                    separator()
                    return None

                separator()
                print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Scanning directories from your file, checking status codes..."}\n")

                with open(directories, "r") as file:
                    for directory in file.readlines():
                        full_url: str = f"https://{user}/{directory.strip()}"
                        base_url = rq.get(full_url)
                        status_code: int = base_url.status_code

                        print(f"URL: {full_url} - Status Code: {status_code_color(base_url)}")
                        check_status_code(status_code, OK_url, forbidden_url, moved_permanent_url, full_url)

                    separator()
                    summary_result(OK_url, forbidden_url, moved_permanent_url)

            except FileNotFoundError:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + f"The file '{directories}' was not found."} {Fore.RED + "!!"}")
                separator()
            except PermissionError:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "You don't have permission to access that file"} {Fore.RED + "!!"}")
                separator()
            except rq.exceptions.ConnectionError:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Can't Connect to the target, Please check your internet connection"} {Fore.RED + "!!"}")
                separator()
            except Exception:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Something went wrong, Please try again"} {Fore.RED + "!!"}")
                separator()

    def check_status_code(status_code, OK_url, forbidden_url, moved_permanent_url, full_url) -> None:
        if status_code == 200:
            OK_url.append(full_url)
        elif status_code == 301:
            moved_permanent_url.append(full_url)
        elif status_code == 403:
            forbidden_url.append(full_url)

    def Manual_Directory_Scan(user: str) -> None:
        while True:
            try:
                directory = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + f"Enter a directory to scan for [ https://{user}/ ] (Type 'q' to quit):"} ").strip()
                if directory.lower() == "q":
                    separator()
                    return None

                full_url = f"https://{user}/{directory.strip()}"
                base_url = rq.get(full_url)
                status_code = status_code_color(base_url)
                separator()
                print("Result\n".center(terminal_width))
                print(f"{full_url} - Status Code: {status_code}".center(terminal_width))
                separator()
            except rq.exceptions.ConnectionError:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Connection Error, Please check your internet connection"} {Fore.RED + "!!"}")
                separator()

    def status_code_color(base_url) -> str:
        if  base_url.status_code == 200:
            return Fore.GREEN + f"{base_url.status_code} OK"
        elif base_url.status_code == 301:
            return Fore.YELLOW + f"{base_url.status_code} Moved Permanently"
        elif base_url.status_code == 403:
            return Fore.RED + f"{base_url.status_code} Forbidden"
        elif base_url.status_code == 404:
            return Fore.LIGHTRED_EX + f"{base_url.status_code} Not Found"
        elif base_url.status_code == 405:
            return Fore.LIGHTMAGENTA_EX+ f"{base_url.status_code} Method not allowed"
        elif base_url.status_code == 500:
            return Fore.MAGENTA + f"{base_url.status_code} Internal Server Error"
        else:
            return Fore.LIGHTYELLOW_EX + f"{base_url.status_code} Unidentified"

    def summary_result(OK_url: list[str], forbidden_url: list[str], moved_permanent_url: list[str]) -> None:
        def result(path_url, status_code, color) -> None:
            print(f"{Fore.GREEN + "[*]"} {Fore.LIGHTMAGENTA_EX + "Summary of"} {color + status_code} {Fore.LIGHTMAGENTA_EX + "Status Code Result:"}\n")
            for num, url in enumerate(path_url):
                print(f"{Fore.WHITE + f"[{num +1}]"} {Fore.LIGHTCYAN_EX + url} - {Fore.WHITE + "Status Code:"} {color + status_code}")
            print()

        result(OK_url, "200 OK", color = Fore.GREEN)
        result(moved_permanent_url, "301 Moved Permanently", color = Fore.YELLOW)
        result(forbidden_url, "403 Forbidden", color = Fore.RED)
        separator()

    def separator() -> None:
        # Get the width of the terminal (how many characters fit in one line)
        terminal_width: int = os.get_terminal_size().columns

        # Make a line of '=' characters that is as wide as the terminal
        separator: int = Fore.RED + "=" * terminal_width

        # Print the line of '=' characters
        print(separator)
    
    def main() -> None:
        while True:
            try:
                user = enter_target()

                # user choices
                while True:
                    user_choice = option()
                    if  user_choice == "q":
                            break

                    while True:
                        if user_choice == "1":
                            OK_url, forbidden_url, moved_permanent_url = Automated_Directory_Scan(user)
                            summary_result(OK_url, forbidden_url, moved_permanent_url)
                            break
                        elif user_choice == "2":
                            if Custom_Directory_Scan(user) is None:
                                break
                        elif user_choice == "3":
                            if Manual_Directory_Scan(user) is None:
                                break
            except KeyboardInterrupt:
                print()
                main()
    main()

if __name__ == "__main__":
    WebDirsCovery()