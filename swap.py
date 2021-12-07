from typing import Text
import requests
from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import getpass
import secrets
from discord_webhook import DiscordWebhook, DiscordEmbed

attempts = 0 
rl = 0

r = requests.Session()
cookie = secrets.token_hex(8)*2
colorama.init()
print("Instagram swapper - Developed by Hands.")
username = input ('Username: ')
password = getpass.getpass()
swap_type = input("Main/Fresh swap: ")
bio = input ("Custom Bio: ")
email = input("Email: ")
userid = input ('Target: ')

url = 'https://instagram.com/accounts/login/ajax/'
headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
req_login = r.post(url,headers=headers,data=data)
if ('userId') in req_login.text:
    r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
    print(Fore.GREEN + 'Signed In: [@' + username + ']')
    sleep(0.5)
    start2 = input("Start Claimer? Y/N: ")
    if start2 == "y" or "Y":
        while True:
            def claimit():

                global attempts, rl
                
                claimurl = 'https://instagram.com/accounts/edit/'
                sentdata = {
                                "username": userid,
                                "biography": bio,
                                "email": email,
                            }
                claim = r.post(claimurl, data=sentdata)
                if ("ok") in claim.text:
                    attempts += 1
                    print(Fore.GREEN + "Successfully swapped @" + userid + "!")
                    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/916807537007923250/PYR6H44Idgi6QIBUFsJfSTMwyNzZvxOKrz_ZiYGyWo9HN46EibWB_P4M8H0ZKLOrWAsC")
                    embed = DiscordEmbed(tittle="Izik won a swap, shocker!", color=242424)
                    embed.add_embed_field(name="Link", value=f"https://instagram.com/{userid}")
                    embed.add_embed_field(name="Attempts", value=f"{attempts}")
                    embed.add_embed_field(name="Swap Monitor", value=f"<@843585950231298078> swapped @{userid}")
                    embed.add_embed_field(name="Swap Type", value=f"{swap_type}")
                    
                    embed.set_footer(text="[Developed By Hands]")
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    sleep(1)
                    exit()
                elif ("spam") in claim.text:
                    rl += 1
                    attempts += 1
                    print(Fore.RED + "Rate Limited.")
                    sleep(1)
                    exit()
                else:
                    print(f"@{userid} - Attempts: {attempts} - RL: {rl}", end='\r', flush=True)
            claimit()
else:
        print('')
        print(Fore.RED + 'Bad Sign In.')
        sleep(3)
        exit()