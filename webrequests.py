from colorama import Fore, Back, Style, init
import requests


url = input('Enter a domain:')

with open('domians-list.txt', 'r') as file:
    words = [line.strip() for line in file]

for i in words:
    http = requests.get(url + '/' + i)
    if http.status_code == 200:
        print(Fore.GREEN + ' [+] ' + Fore.WHITE + url+"/"+i)
    else:
        print(Fore.RED + " [!] " + Fore.YELLOW + url + '/' + i)

