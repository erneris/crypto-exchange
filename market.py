from file_management import update_profile
from utils import clear, text_message, get_terminal_height, loading_screen
from termcolor import colored
from requests import get
from crypto_info import get_currencies, get_data

def portfolio(profile):
    pass

def market(profile):
    loading_screen()
    height = get_terminal_height()
    currencies = get_currencies()
    ammount_of_currencies = len(currencies)
    pages = ammount_of_currencies // (height - 3) + 1
    
    current_page = 1
    clear()
    while True:
        text_message("Cryptocurrency marketplace")
        print(colored("Type in symbol of cryptocurrency you would like to purchase, < or > to switch between pages or done to leave.", "green"))

        #todo print out cryptos

        text_message(f"(<) {current_page} page out of {pages} (>)")


        control = input("").strip().lower()
        if control == "<":
            if current_page == 1:
                current_page = pages
            else:
                current_page -= 1

        elif control == ">":
            if current_page == pages:
                current_page = 1
            else:
                current_page += 1
                
        elif control == "done":
            return 0

        elif get_data(control):
            clear()
            currency = get_data(control)
            while True:
                try:
                    text_message(f"""Purchase {currency["name"]}""")
                    print(colored(f"""Your available balance: ${profile["money"]}""", "green"))
                    print(colored(f"""Price of 1 {currency["name"]}: ${currency["price"]}""", "yellow"))
                    print(colored(f"""Enter how much {currency["symbol"]} your would like to purchase (min 0.0001) or done to quit: """), end = "")
                    ammount = input("").strip().lower()
                    if ammount == "done":
                        break
                    ammount = float(ammount)
                    if ammount < 0.0001:
                        clear()
                        print(colored("Purchase ammount lower than minimum", "red"))
                        pass
                    else:
                        while True:
                            clear()
                            price = ammount * currency["price"]
                            print(colored(f"Final price would be ${price}, would like to purchase? (y/n): ", "yellow"), end = "")
                            answer = input("").strip().lower()
                            if answer == "y" or answer == "yes":
                                if price > profile["money"]:
                                    clear()
                                    print(colored("Not enough money to complete purchase", "red"))
                                    break
                                else:
                                    profile["money"] -= price
                                    profile["assets"].append({"symbol": currency["symbol"], "ammount": ammount})
                                    update_profile(profile)
                                    break
                            elif answer == "n" or answer == "no":
                                clear()
                                break
                            

                except ValueError:
                    clear()
                    print(colored("Invalid input", "red"))
                    pass

        clear()


def sell(profile):
    pass
    
