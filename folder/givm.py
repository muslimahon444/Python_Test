import random
from colorama import Fore,Style,init 
init(autoreset=True)
print(Fore.CYAN+ 'ДОбро пожаловать в нашу игру Угодай число :')
number = random.randint(1,11)
pop = 0
while True:
    user = int(input('введите число от 1 до 10 '))
    
    pop += 1
    if user < number:
        print(Fore.BLUE+'это число больше')
    elif user > number:
        print(Fore.BLUE+'Это число меньше')
    else:
        print(Fore.GREEN + f'Вы угодали число это было {number}')
        print(Fore.GREEN+ f'Поздравляю вас вы угодали за {pop} попыток ')
        break
if __name__ == '__main__':
    givm()