import json

DATA_FOLDER_NAME = "data"

def save_profiles(profiles):
        with open(f"{DATA_FOLDER_NAME}/profiles.json", "w") as file:
            template = {"profiles": profiles}
            json.dump(template, file, ensure_ascii=False, indent=4) #arguments for better readability

def get_profiles():
    try:
        with open(f"{DATA_FOLDER_NAME}/profiles.json") as file:
            data = json.load(file)
            return data["profiles"]

    except (FileNotFoundError, json.decoder.JSONDecodeError): #if file isn't created
        save_profiles([])
        return []

    
