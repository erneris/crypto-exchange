from os import get_terminal_size, system
from termcolor import colored


def clear():
    system('clear')

def text_message(text):
    element = "#" * round((get_terminal_size()[0] - len(text) - 2)//2)
    print(colored(f"{element} {text} {element}", "blue"))