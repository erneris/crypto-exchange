import sys, os, csv, colorama, json
from termcolor import colored
DATA_FOLDER_NAME = "data"


        

def save_profiles():
    pass

def get_profiles():
    try:
        with open(f"{DATA_FOLDER_NAME}/profiles.json") as file:
            data = json.load(file)
            return data["profiles"]

    except FileNotFoundError: #if file isn't created
        with open(f"{DATA_FOLDER_NAME}/profiles.json", "w") as file:
            template = {"profiles": []}
            json.dump(template, file, ensure_ascii=False, indent=4) #arguments for better readability
            return []
        
def select_profile():
    profiles = get_profiles()
    print(profiles)
    if len(profiles) == 0:
        pass
        #create_profile(profiles)
    for profile in profiles:
        print(profile)

def main():
    clear()
    colorama.init()
    select_profile()

def clear():
    os.system('clear')

if __name__ == "__main__":
    main()