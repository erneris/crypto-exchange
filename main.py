import sys, os, csv, colorama, re
from termcolor import colored
from file_management import get_profiles, save_profiles

def text_message(text):
    element = "#" * round((os.get_terminal_size()[0] - len(text) - 2)/2)
    print(colored(f"{element} {text} {element}", "blue"))

def create_profile():

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        name = str(input(colored("Your name: ", "yellow"))).capitalize()
        if len(name) > 0:
            break
    
    while True:
        email = input(colored("Your email: ", "yellow"))
        if re.match(email_regex, email):
            break
        else:
            print(colored("Invalid email adress!", "red"))

    while True:
        try:
            money = int(input(colored("Ammount of starting money(at least $500): ", "yellow")).replace("$", ""))
            if money < 500:
                print(colored("Starting money is too low!", "red"))  
            else:
                break         
        except ValueError:
            print(colored("Invalid input!", "red"))
            pass

    profiles = get_profiles()
    max_id = -1
    for profile in profiles:
        if profile["id"] > max_id:
            max_id = profile["id"]

    id = max_id + 1
    profiles.append({"id": id, "name": name, "email": email, "assets": []})
    save_profiles(profiles)
    
def select_profile():
    profiles = get_profiles()
    while True:
        if len(profiles) == 0:
            print(colored("You don't have any created profiles. Please create a new one.", "red"))
            create_profile()
            break
        else:  
            pass
            

def main():
    clear()
    colorama.init()
    text_message("Welcome to Cryptocurrency Exchange Emulator!")
    profile = select_profile()

def clear():
    os.system('clear')

if __name__ == "__main__":
    main()