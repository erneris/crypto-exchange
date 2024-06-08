from file_management import update_profile, get_profile
from sys import exit
from utils import clear, text_message
from termcolor import colored
from email import export
from market import sell, market, portfolio

def start_menu(id):
    while True:
        profile = get_profile(id)
        text_message(f"""Welcome, {profile["name"]} (${profile["money"]})!""")
        print(colored("Choose one of the menu options: ", "yellow"))
        print(colored("1| My portfolio\n2| Cryptocurrency market\n3| Sell assets\n4| Export data\n5| Cheats\n6| Log out\n7| Quit", "green"))
        try:
            item = int(input("").strip())
            if item < 1 and item > 7:
                raise ValueError
        except ValueError:
            pass

        if item == 1: #portfolio
            portfolio()
        elif item == 2: #crypto market
            market()
        elif item == 3: #sell assets
            sell()
        elif item == 4: #export data
            export()
        elif item == 5: #cheats
            clear()
            text_message("Cheat menu")
            print(colored(f"""Your funds: ${profile["money"]}""", "green"))
            while True:
                try:
                    print(colored("Type in desired ammount of money to be added your account: ", "yellow"), end = "")
                    ammount = float(input(""))
                    if ammount <= 0:
                        raise ValueError
                    clear()
                    print(colored("Money successfully added!", "green"))
                    new_profile = profile
                    new_profile["money"] = new_profile["money"] + ammount
                    update_profile(new_profile)
                    break

                except ValueError:
                    print(colored("Invalid value", "red"))
                    pass

        elif item == 6: #logout
            return 2
        elif item == 7: #quit
            clear()
            exit(0)