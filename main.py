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
            money = int(input(colored("Ammount of starting money (at least $500): ", "yellow")).replace("$", ""))
            if money < 500:
                print(colored("Starting money is too low!", "red"))  
            else:
                break         
        except ValueError:
            print(colored("Invalid input!", "red"))
            pass
    clear()
    print(colored("Profile successfully created!", "green"))

    profiles = get_profiles()
    max_id = -1
    for profile in profiles:
        if profile["id"] > max_id:
            max_id = profile["id"]

    id = max_id + 1
    profile = {"id": id, "name": name, "email": email, "assets": []}
    profiles.append(profile)
    save_profiles(profiles)
    return profile
    
def select_profile():
    profiles = get_profiles()
    if len(profiles) == 0:
        print(colored("You don't have any created profiles. Please create a new one.", "red"))
        profile = create_profile()
        return profile
    else:  
        ids = []
        id = None
        print(colored("""Choose your account by typing its ID or type new to create a new profile""", "yellow"))
        for profile in profiles:
            ids.append(profile["id"])
            print(colored(f"""ID: {profile["id"]} | {profile["name"]}""", "cyan"))
        
        while True:
            try:
                input_id = input("")
                if input_id.lower() == "new":
                    clear()
                    profile = create_profile()
                    return profile
                    
                else:
                    if not int(input_id) in ids:
                        raise ValueError
                    id = int(input_id)
                    for profile in profiles:
                        if profile["id"] == id:
                            return profile

            except ValueError:
                print(colored("Invalid ID", "red"))
    


def main():
    clear()
    colorama.init()
    text_message("Welcome to Cryptocurrency Exchange Emulator!")
    profile = select_profile()
    print(profile)

def clear():
    os.system('clear')

if __name__ == "__main__":
    main()