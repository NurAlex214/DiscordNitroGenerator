import random
import string
import time
import os
import requests
from colorama import init, Fore, Back, Style

# Initialize colorama for colored output
init(autoreset=True)

ASCII_ART = f"""{Fore.MAGENTA + Style.BRIGHT}
███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Fore.CYAN + Style.BRIGHT}
                        【ＢＹ ＡＳＩＣＳ】
"""

def check_nitro(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}"
    response = requests.get(url)
    return response.status_code == 200

def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return code

def save_valid_code(code):
    with open('valid.txt', 'a') as f:
        f.write(f"https://discord.gift/{code}\n")

def save_invalid_code(code):
    with open('invalid.txt', 'a') as f:
        f.write(f"https://discord.gift/{code}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(ASCII_ART)
    print(f"{Fore.CYAN + Style.BRIGHT}╔════════════════════════════════════════╗")
    print(f"{Fore.CYAN + Style.BRIGHT}║{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}        Discord Nitro Generator v1.0       {Fore.CYAN + Style.BRIGHT}║")
    print(f"{Fore.CYAN + Style.BRIGHT}╚════════════════════════════════════════╝\n")
    
    try:
        amount = int(input(f"{Fore.LIGHTBLUE_EX + Style.BRIGHT}[?] How many codes do you want to generate? "))
        print(f"\n{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}[+] Starting generation process...")
        print(f"{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}[+] Checking {amount} Nitro gift links...\n")
        
        valid_codes = 0
        for i in range(amount):
            code = generate_nitro_code()
            is_valid = check_nitro(code)
            
            if is_valid:
                valid_codes += 1
                status_color = Fore.LIGHTGREEN_EX + Style.BRIGHT
                status = "VALID"
                save_valid_code(code)
                print(f"{Fore.LIGHTGREEN_EX + Style.BRIGHT}[!] Valid code found and saved to valid.txt!")
            else:
                status_color = Fore.LIGHTRED_EX + Style.BRIGHT
                status = "INVALID"
                save_invalid_code(code)
                
            print(f"{status_color}[{i+1}/{amount}] https://discord.gift/{code} - {status}")
            time.sleep(0.001)
            
        print(f"\n{Fore.LIGHTMAGENTA_EX + Style.BRIGHT}[+] Generation complete!")
        print(f"{Fore.LIGHTYELLOW_EX + Style.BRIGHT}[*] Statistics:")
        print(f"{Fore.LIGHTGREEN_EX + Style.BRIGHT}[✓] Valid codes: {valid_codes}")
        print(f"{Fore.LIGHTRED_EX + Style.BRIGHT}[✗] Invalid codes: {amount - valid_codes}")
        print(f"\n{Fore.LIGHTCYAN_EX + Style.BRIGHT}[+] Valid codes saved to: {Fore.LIGHTGREEN_EX}valid.txt")
        print(f"{Fore.LIGHTCYAN_EX + Style.BRIGHT}[+] Invalid codes saved to: {Fore.LIGHTRED_EX}invalid.txt")
        input(f"\n{Fore.LIGHTBLUE_EX + Style.BRIGHT}[?] Press Enter to exit...")
        
    except ValueError:
        print(f"{Fore.LIGHTRED_EX + Style.BRIGHT}[!] Please enter a valid number!")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main() 