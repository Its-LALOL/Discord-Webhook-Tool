import os
os.system('cls && title Webhook Tool By LALOL' if os.name == 'nt' else 'clear')
import requests
import threading
import time
import json
import colorama
from colorama import init, Fore, Back, Style
init(convert=True)

number=0

Intro=Fore.MAGENTA + """
[1] Webhook Spammer
[2] Webhook Creator
[3] Webhook Deleter
"""
def Spammer(webhook, jsoncode):
	while True:
		try: response=requests.post(webhook, json=jsoncode)
		except: break
		if response.status_code==200 or response.status_code==202 or response.status_code==204:
			global number
			number+=1
			print(Fore.GREEN + f"Sent {number} message!")
		if response.status_code==404:
			break
		if response.status_code==429:
			json_data = json.loads(response.text)
			if 100 > json_data['retry_after']:
				time.sleep(json_data['retry_after'])
def Menu():
	os.system('cls && title Webhook Tool By LALOL - Menu' if os.name == 'nt' else 'clear')
	print(Fore.GREEN + "Webhook Tool By LALOL")
	print(Intro + Fore.YELLOW)
	option=input("Please select option: ")
	if option=="1":
		input("Press Enter to start spam")
		with open("message.json", "r", encoding="utf-8") as f:
			jsoncode = json.load(f)
		file = open('webhooks.txt', encoding='utf-8')
		os.system('cls && title Webhook Tool By LALOL - Spammer' if os.name == 'nt' else 'clear')
		for webhook1 in file:
			webhook = webhook1.rstrip('\n')
			for i in range(5):
				t = threading.Thread(target=Spammer, args=(webhook, jsoncode))
				t.start()
		print(Fore.MAGENTA + "Spam has started!")
	elif option=="2":
		os.system('cls && title Webhook Tool By LALOL - Webhook Creator' if os.name == 'nt' else 'clear')
		token=input("Enter Account Token: ")
		headers = {'Authorization': token}
		token_check = requests.get('https://discord.com/api/v9/users/@me/library', headers=headers)
		if token_check.status_code == 200 or token_check.status_code == 202:
			guildid=input("Enter guild id: ")
			webhookname=input("Enter Webhook name: ")
			input("Press Enter to start create webhook (After this operation, all old webhooks will be deleted from the file!)")
			response=requests.get(f'https://discord.com/api/v8/guilds/{guildid}/channels', headers=headers)
			info = response.json()
			channelids=[]
			for channelid in info:
				if channelid["type"] == 0:
					channelids.append(channelid['id'])
			f=open("webhooks.txt", "w", encoding='utf-8')
			for id in channelids:
				response=requests.post(f"https://discord.com/api/v9/channels/{id}/webhooks", headers=headers, json={"name": webhookname})
				json_data = json.loads(response.text)
				f.write(f"https://discord.com/api/webhooks/{json_data['id']}/{json_data['token']}\n")
			f.close()
			print(Fore.GREEN + "All webhooks have been successfully written to the file!")
			time.sleep(5)
			Menu()
		else:
			print(Fore.RED + "Token invalid!")
			time.sleep(3)
			Menu()
	elif option=="3":
		os.system('cls && title Webhook Tool By LALOL - Webhook Deleter' if os.name == 'nt' else 'clear')
		input("Press Enter to start delete all webhooks from file")
		file = open('webhooks.txt', encoding='utf-8')
		for webhook1 in file:
			webhook = webhook1.rstrip('\n')
			try: response=requests.delete(webhook)
			except: pass
		print(Fore.GREEN + "All webhooks have been successfully removed!")
		time.sleep(5)
		Menu()
	else:
		print(Fore.RED + "Invalid option!")
		time.sleep(3)
		Menu()
print(Fore.RED +"""
██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░░░░
██║░░░░░███████║██║░░░░░██║░░██║██║░░░░░
██║░░░░░██╔══██║██║░░░░░██║░░██║██║░░░░░
███████╗██║░░██║███████╗╚█████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝
""")
print(Fore.GREEN + "Webhook Tool By LALOL")
time.sleep(5)
Menu()