from secrets import choice
from colorama import init, Fore
from pyfiglet import figlet_format 
from sys import exit

init(autoreset=True)

CHARSET = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

def new_pass(length: int, charset: str) -> str:
    if length < 8:
        raise ValueError('length too short')
    return ''.join(choice(charset) for _ in range(length))

def main():
    print(figlet_format(' Secure Password'))
    while True:
        try:
            length = int(input(' [#] Password length: '))

            if length < 8:
                print(f'{Fore.RED} [!] Password too short\n\n')
            else:
                print(f'{Fore.GREEN} [+] Password:{Fore.WHITE} {new_pass(length=length, charset=CHARSET)}\n\n')
        except ValueError:
            print(f'{Fore.RED} [!] Password length must be an integer\n\n')
        except KeyboardInterrupt:
            exit()
        except:
            print(f'{Fore.RED} [!] Unknown error\n\n')         

if __name__ == '__main__':
    main()