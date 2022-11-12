from random import seed, randint, choice
from secrets import randbits
from colorama import init, Fore
from pyfiglet import figlet_format 
from sys import exit

class SPASS:
    def __init__(self):
        self.charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\!^£$%&/()=?_-,*[]@°§'
        self.title = ' Secure Password'
        init(autoreset=True)

    def isMinLength(self) -> bool:
        if self.length < 8:
            return False
        return True

    def randomize_seed(self) -> str:
        return '{:064x}'.format(randbits(randint(256, 512)))

    def new_pass(self) -> str:
        seed(self.randomize_seed())
        return ''.join(choice(self.charset) for _ in range(self.length))

    def run(self):
        print(figlet_format(self.title))
        while True:
            try:
                self.length = int(input(' [^] Password length: '))

                if self.isMinLength() is False:
                    print(f'{Fore.RED} [!] Password too short\n\n')
                elif self.isMinLength() is True:
                    print(f'{Fore.GREEN} [+] Password:{Fore.WHITE} {self.new_pass()}\n\n')
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print(f'{Fore.RED} [!] Password length must be an integer\n\n')
            except:
                print(f'{Fore.RED} [!] Unknown error\n\n')         

if __name__ == '__main__':
    spass = SPASS()
    spass.run()
