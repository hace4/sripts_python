from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.CYAN)
print(Fore.BLACK)
print("Введите время")
t = int(input())
print("Введите скорость")
v = int(input())
print(v*t)
if v > 0:
    l = (v*t)%109
else: 
    print(Fore.BLACK)
    print(Back.RED) 
    l = 109 - (- v*t)%109
print(l)