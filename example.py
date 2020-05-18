from termcolor import colored
import pyfiglet

t = colored("This is it! You're progressing", color="blue", on_color="on_magenta", attrs=["blink"])
print(t)

help(pyfiglet)