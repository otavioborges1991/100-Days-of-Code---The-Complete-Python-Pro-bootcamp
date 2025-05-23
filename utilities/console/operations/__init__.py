from platform import platform
from os import system

def clear():
    os = platform.system()
    if os == 'Windows':
        system('cls')
    else:
        system('clear')
