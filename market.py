from file_management import update_profile
from utils import clear, text_message, get_terminal_height, loading_screen
from termcolor import colored
from requests import get
from crypto_info import get_currencies, get_data

def portfolio(profile):
    clear()
    currencies = get_currencies()
    text_message(f"""{profile["name"]} portfolio""")
    print(colored(f"""Available funds: ${profile["money"]}\n""", "green"))
    print(colored(f"""Your assets:""", "yellow"))
    value = profile["money"]

    for asset in profile["assets"]:
        asset_data = {}
        for currency in currencies:
            if currency["symbol"] == asset["symbol"]:
                asset_data = currency
        price = round(asset["ammount"] * asset_data["price"], 2)    
        value += price
        print(colored(f"""{asset_data["name"]} ({asset_data["symbol"]}) - {asset["ammount"]} = ${price}""", "blue"))
    print(colored(f"Total account value - ${value}\n", "yellow"))
            
    print(colored("Enter anything to continue: ", "green"), end = "")
    input("")

def market(profile):
    loading_screen()
    height = get_terminal_height()
    currencies = get_currencies()
    ammount_of_currencies = len(currencies)
    pages = ammount_of_currencies // (height - 3) + 1
    last_page_size = ammount_of_currencies % (height - 3)
    
    current_page = 1
    clear()
    while True:
        text_message("Cryptocurrency marketplace")
        print(colored("Type in symbol of cryptocurrency you would like to purchase, < or > to switch between pages or done to leave.", "green"))
        first = None
        last = None
        if current_page == pages:
            last = ammount_of_currencies
            first = ammount_of_currencies - last_page_size
        else:
            first = (current_page - 1) * (height - 3)
            last = first + height - 3

        for currency in currencies[first:last]:
            print(colored(f"""{currency["name"]} --- {currency["symbol"]}""", "yellow"), end = "")
            print(colored(f"""  Price for 1: ${currency["price"]}""", "green"))
            
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
                            price = round(ammount * currency["price"], 2)
                            print(colored(f"Final price would be ${price}, would like to purchase? (y/n): ", "yellow"), end = "")
                            answer = input("").strip().lower()
                            if answer == "y" or answer == "yes":
                                if price > profile["money"]:
                                    clear()
                                    print(colored("Not enough money to complete purchase", "red"))
                                    break
                                else:
                                    profile["money"] -= price
                                    found = False
                                    for asset in profile["assets"]:
                                        if asset["symbol"].lower() == currency["symbol"].lower():
                                            asset["ammount"] += ammount
                                            found = True
                                    if not found:
                                       profile["assets"].append({"symbol": currency["symbol"], "ammount": ammount})
                                    update_profile(profile)
                                    clear()
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
    
