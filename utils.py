from os import get_terminal_size, system
from termcolor import colored
from time import sleep

def clear():
    system('clear')

def text_message(text):
    element = "#" * round((get_terminal_size()[0] - len(text) - 2)//2)
    print(colored(f"{element} {text} {element}", "blue"))

def get_terminal_height():
    return get_terminal_size()[1] - 1

def loading_screen():
    get_terminal_size()[1]
    height = get_terminal_height()
    for _ in range(height):
        sleep(0.1)
        print(colored("Loading...", "green"))