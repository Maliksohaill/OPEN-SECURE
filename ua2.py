#coding = utf-8

'''
Assalam u Aleakum , mne socha tha community ki help krunga kuch new chze bna k donga but afsos ye log deserve nhi krta, maximum copy pasters h yhn or khudko piro smjty h jo log rat bhr jag k khudki coding krte h ye unki mhnt pe dagh lgadete h, munafik h ye or scam krte logo sath,.. me kch wakt skip kr rha hu , log copy bolty h to ye dkhlo script khn ki copy h ye?
jisko mzed help chahye ho kise chz se related koi suggestions ho koch new bnanay ka to mujy msg krdna
whatsapp : +923152056613
fb id : facebook.com/dilute840
insta id : @codesbyaqib
Enjoy Kro Sab
'''


import re , requests,sys,time,os
from time import sleep as sp
url = 'https://user-agents.net/random'

ses = requests.Session()
S = "\033[1;96m"
clr=lambda x:f"\001b[38;5;{x}m"
blue=clr(117)
rst="\001b[0;1m"
grn=clr(82)
def clear():
	os.system("clear")
def logo():
	print(f'''
\t##     ##    ###    
\t##     ##   ## ##   
\t##     ##  ##   ##  
\t##     ## ##     ## 
\t##     ## ######### 
\t##     ## ##     ## 
\t #######  ##     ##
--------------------------------------------------
  [•] Random Working User Agent Generator Online
--------------------------------------------------
  [•] Tool Coded  : Aqib X Siam
  [•] Aqib Github : Dcofficial
  [•] Siam Github : SIAM-AHMED-CP
  [•]\033[1;92m One Single Vulnerability All An Attacker Needs \033[0m
--------------------------------------------------''')
def main():
	clear()
	logo()
	os.system("")
	try:
		limit = int(input("  [•] Put UA Limit : "))
	except(ValueError):
		limit = 100
	try:
		sav = input("  [•] Save Path :- ")
		if sav =="":
			sav = "/sdcard/ua.txt"
	except(FileNotFoundError):
		sav = "/sdcard/ua.txt"
	ua(limit,sav)
	print(f"\n  [•] Proccess Has Been Completed \n  [•] Your File Saved in : {sav} ")
	print(51*'-')
def ua(limit,sav):
	n=[]
	data = {
	'limit':f"{limit}",
	'action':'generate'
	}
	t = open(sav,"a")
	try:
		r = ses.post(url=url,data=data).text
		for x in re.findall('href\=\"/string/(.*?)">(.*?)<',r):
			n.append(x[1])
			t.write(x[1]+'\n')
			sys.stdout.write(f"\r  [•] Getting UA: [{len(n)}] ");sys.stdout.flush();sp(0.009)
	except ConnectionError:
		print(f" [•] Please Check Your Internet Connection ..")
		exit()
main()
