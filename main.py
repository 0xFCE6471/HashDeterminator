import time, sys, os, fade, random
from colorama import Fore
from core.hash_identifier import hash_type

def clear():
    if sys.platform == "win32":
        return os.system("cls")
    else:
        return os.system("clear")


def getTime():
    times = time.strftime("%H:%M:%S")
    times = str(times)
    return (times)

def random_color(logo):
    list = [fade.brazil(logo), fade.purpleblue(logo), fade.pinkred(logo), fade.fire(logo), fade.water(logo), fade.greenblue(logo),
            fade.purplepink(logo), fade.blackwhite(logo)]
    return random.choice(list)

def main():
    logo = """
      _    _           _           _      _                      _             _             
     | |  | |         | |         | |    | |                    (_)           | |            
     | |__| | __ _ ___| |__     __| | ___| |_ ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
     |  __  |/ _` / __| '_ \   / _` |/ _ \ __/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
     | |  | | (_| \__ \ | | | | (_| |  __/ ||  __/ |  | | | | | | | | | | (_| | || (_) | |   
     |_|  |_|\__,_|___/_| |_|  \__,_|\___|\__\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_|   
                                                                                            Author: 0xKEYSEX                                                                          
    """
    print(random_color(logo))
    hash = input(f"{Fore.MAGENTA} Indicate the hash : ")

    if len(hash) == 0:
        print(f"{Fore.RED}[/!\] You must indicate the hash! {Fore.RESET}")
        time.sleep(1)
        clear()
        return main()
    else:
        try:
            hash_type(hash)
            print("\n")
            choice = input(f"{Fore.MAGENTA}[?] What do you want to do now : (r)research (e)exit {Fore.RESET}")

            if choice == "R" or "r":
                print(f"{Fore.MAGENTA} Reloading . . .")
                time.sleep(1)
                clear()
                return main()
            else:
                clear()
                print(f"{Fore.MAGENTA} Bye ! {Fore.RESET}")
                sys.exit(0)

        except KeyboardInterrupt:
            clear()
            print(f"{Fore.MAGENTA} Bye ! {Fore.RESET}")
            sys.exit(0)


if __name__ == '__main__':
    main()