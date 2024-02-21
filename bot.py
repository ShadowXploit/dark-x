import useragent
import os
import sys
import time
import platform
import requests
import re
import json
import urllib
import colorama
import instaloader
from time import sleep
from datetime import datetime
from instaloader import instaloader
from colorama import init, Fore

def owlsint3():
  ### colors
  RED = "\033[91m"
  GREEN = "\033[92m"
  BLUE = "\033[94m"
  YELLOW = "\033[1;93m"
  WHITE = "\033[1;97m"
  NORMAL = "\033[0;37m"
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  YE = '\033[1;33m'
  BOLD = '\033[1m'
  ENDC = '\033[0m'
  CRED2 = "\33[91m"
  CBLUE2 = "\33[94m"
  ENDC = "\033[0m"
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  ### banner
  def banner():
              print (f"""
{OKGREEN}Version 1.2 - 2023 coded by Mr,OwlBird05""")
  def start():
              os.system("clear")
              banner()
              import instaloader, sys
              from instaloader import instaloader
              #2 MODULE

              x = instaloader.Instaloader()

              try:
                        print ()
                        sleep(1)
                        uname = input(f"\033[32mEnter a username instagram \033[0m:{CRED2}➤ \033[37m") #INPUT USER
                        if uname == "":
                                        print("\033[1;31mUnknown command!\n")
                                        sys.exit()


                        f = instaloader.Profile.from_username(x.context,uname)

                        print("\033[32mUsername\033[0m :", f.username)
                        print("\033[32mID\033[0m :", f.userid)
                        print("\033[32mNama lengkap\033[0m :", f.full_name)
                        print("\033[32mBiografi\033[0m :", f.biography)
                        print("\033[32mNama kategori bisnis\033[0m :", f.business_category_name)
                        print("\033[32mURL eksternal\033[0m :", f.external_url)
                        print("\033[32mDiikuti orang\033[0m :", f.followed_by_viewer)
                        print("\033[32mMengikuti\033[0m :", f.followees)
                        print("\033[32mPengikut\033[0m :", f.followers)
                        print("\033[32mMengikuti orang\033[0m :", f.follows_viewer)
                        print("\033[32mDiblokir orang\033[0m :", f.blocked_by_viewer)
                        print("\033[32mPernah memblokir orang\033[0m :", f.has_blocked_viewer)
                        print("\033[32mPunya sorotan\033[0m :", f.has_highlight_reels)
                        print("\033[32mPunya cerita publik\033[0m :", f.has_public_story)
                        print("\033[32mTelah meminta orang\033[0m :", f.has_requested_viewer)
                        print("\033[32mDiminta orang\033[0m :", f.requested_by_viewer)
                        print("\033[32mMemiliki cerita yang dapat dilihat\033[0m :", f.has_viewable_story)
                        print("\033[32mIGTV\033[0m :", f.igtvcount)
                        print("\033[32mAkun bisnis\033[0m :", f.is_business_account)
                        print("\033[32mAkun pribadi\033[0m :", f.is_private)
                        print("\033[32mDiverifikasi\033[0m :", f.is_verified)
                        print("\033[32mPostingan\033[0m :", f.mediacount)
                        print("\033[32mURL foto profil\033[0m :", f.profile_pic_url)
                        print ()

              except KeyboardInterrupt:
                        print("\033[33mI understand!")

              except EOFError:
                        print("\033[33mWhy?")
  ### Start tools
  start()
  ### CODED BY MR,OWLBIRD05 / +6283848301116

def IP_Track():
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[1;93m"
    WHITE = "\033[1;97m"
    NORMAL = "\033[0;37m"
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    YE = '\033[1;33m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(" \033[1;93mVersion 1.2 - 2023 coded by Mr,OwlBird05")
    sleep(1)
    ip = input(f"{WHITE}\n Enter IP target :{CRED2}➤ ") #INPUT IP ADDRESS
    print()
    print(f' {NORMAL}============= {YELLOW}SHOW INFORMATION IP ADDRESS {NORMAL}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}") #API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{NORMAL}\n IP target       :{YELLOW}", ip)
    sleep(0.1)
    print(f"{NORMAL} Type IP         :{YELLOW}", ip_data["type"])
    sleep(0.1)
    print(f"{NORMAL} Country         :{YELLOW}", ip_data["country"])
    sleep(0.1)
    print(f"{NORMAL} Country Code    :{YELLOW}", ip_data["country_code"])
    sleep(0.1)
    print(f"{NORMAL} City            :{YELLOW}", ip_data["city"])
    sleep(0.1)
    print(f"{NORMAL} Continent       :{YELLOW}", ip_data["continent"])
    sleep(0.1)
    print(f"{NORMAL} Continent Code  :{YELLOW}", ip_data["continent_code"])
    sleep(0.1)
    print(f"{NORMAL} Region          :{YELLOW}", ip_data["region"])
    sleep(0.1)
    print(f"{NORMAL} Region Code     :{YELLOW}", ip_data["region_code"])
    sleep(0.1)
    print(f"{NORMAL} Latitude        :{YELLOW}", ip_data["latitude"])
    sleep(0.1)
    print(f"{NORMAL} Longitude       :{YELLOW}", ip_data["longitude"])
    sleep(0.1)
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    sleep(0.1)
    print(f"{NORMAL} Maps            :{YELLOW}",f"https://www.google.com/maps/@{lat},{lon},8z")
    sleep(0.1)
    print(f"{NORMAL} EU              :{YELLOW}", ip_data["is_eu"])
    sleep(0.1)
    print(f"{NORMAL} Postal          :{YELLOW}", ip_data["postal"])
    sleep(0.1)
    print(f"{NORMAL} Calling Code    :{YELLOW}", ip_data["calling_code"])
    sleep(0.1)
    print(f"{NORMAL} Capital         :{YELLOW}", ip_data["capital"])
    sleep(0.1)
    print(f"{NORMAL} Borders         :{YELLOW}", ip_data["borders"])
    sleep(0.1)
    print(f"{NORMAL} Country Flag    :{YELLOW}", ip_data["flag"]["emoji"])
    sleep(0.1)
    print(f"{NORMAL} ASN             :{YELLOW}", ip_data["connection"]["asn"])
    sleep(0.1)
    print(f"{NORMAL} ORG             :{YELLOW}", ip_data["connection"]["org"])
    sleep(0.1)
    print(f"{NORMAL} ISP             :{YELLOW}", ip_data["connection"]["isp"])
    sleep(0.1)
    print(f"{NORMAL} Domain          :{YELLOW}", ip_data["connection"]["domain"])
    sleep(0.1)
    print(f"{NORMAL} ID              :{YELLOW}", ip_data["timezone"]["id"])
    sleep(0.1)
    print(f"{NORMAL} ABBR            :{YELLOW}", ip_data["timezone"]["abbr"])
    sleep(0.1)
    print(f"{NORMAL} DST             :{YELLOW}", ip_data["timezone"]["is_dst"])
    sleep(0.1)
    print(f"{NORMAL} Offset          :{YELLOW}", ip_data["timezone"]["offset"])
    sleep(0.1)
    print(f"{NORMAL} UTC             :{YELLOW}", ip_data["timezone"]["utc"])
    sleep(0.1)
    print(f"{NORMAL} Current Time    :{YELLOW}", ip_data["timezone"]["current_time"])
    print ()
    sleep(0.1)
  ### IP Track CODED BY MR,OWLBIRD05 / +6283848301116

def logo():
     print (f"""\033[1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣏⠉⠉⠉⠉⠉⠉⢡⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀
⠈⣿⣿⣿⣿⣦⣽⣦⡀⠀⠀⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⡟⢿⠻⠛⠙⠉⠋⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠈⠙⢿⡇⣠⣤⣶⣶⣾⡉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⢇⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⢤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣬⣭⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣠⣴⣾⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣘⡛⠿⢿⡿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠿⠛⠉⠁⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠟⠛⠃⠀⠀⠀⠉⠉⠉⠛⠛⠛⠿⠿⠿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
 \033[1;34m██████\033[1;31m╗    \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╗   \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗             \033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╗
 \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m║ \033[1;34m██\033[1;31m╔╝             ╚\033[1;34m██\033[1;31m╗\033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m███████\033[1;31m║  \033[1;34m██████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╔╝    \033[1;34m███████\033[1;31m╗   ╚\033[1;34m███\033[1;31m╔╝
 \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗  \033[1;34m██\033[1;31m╔═\033[1;34m██\033[1;31m╗    ╚══════╝   \033[1;34m██\033[1;31m╔\033[1;34m██\033[1;31m╗
 \033[1;34m██████\033[1;31m╔╝  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m╗             \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╗
 \033[1;31m╚═════╝   ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝             ╚═╝  ╚═╝     
\033[1;34m╔═══════════════════════════════════════════════════════════╗
\033[1;34m║ \033[1;31mAuthor      \033[1;36m: \033[1;37mShadow Xploit                               \033[1;34m║
\033[1;34m║ \033[1;31mContact     \033[1;36m: \033[1;37mt.me/ShadowXploit                           \033[1;34m║
\033[1;34m║ \033[1;31mTeam        \033[1;36m: \033[1;37mDARK XPLOITER | OFC                         \033[1;34m║
\033[1;34m╚═══════════════════════════════════════════════════════════╝
║                           \033[1;31mMENU                            \033[1;34m║
╔═══════════════════════════════════════════════════════════╗
\033[1;34m║ \033[1;31m[\033[1;37m1\033[1;31m] \033[1;34m║ \033[1;36mDATABASE LEAKER  ️                                   \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m2\033[1;31m] \033[1;34m║ \033[1;36mSTALKING INSTAGRAM ACCOUNT                          \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m3\033[1;31m] \033[1;34m║ \033[1;36mIP INFORMATION                                      \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m4\033[1;31m] \033[1;34m║ \033[1;36mLINUX BANNER                                        \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m5\033[1;31m] \033[1;34m║ \033[1;36mBRUTEFORCE ZIP \033[1;31m(Khusus Angka)                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m0\033[1;31m] \033[1;34m║ \033[1;36mEXIT                                                \033[1;34m║
\033[1;34m╚═══════════════════════════════════════════════════════════╝
""")

os.system("clear")
logo()
while True:
        message = input("\033[1;34m┌──(\033[1;31mdark㉿localhost\033[1;34m)-[\033[1;37m~\033[1;34m]\n└─\033[1;31m#\033[1;37m ")
        if message.strip():
            if message == '00' or message == '0':
                print("\033[1;33mProgram dihentikan...\n")
                time.sleep(1)
                break
            elif message == '01' or message == '1':
                time.sleep(1)
                print("")
                target = input("\033[1;34mDomain target \033[1;31m(ex. kpu.go.id) : \033[1;37m")
                filetype = input("\033[1;34mFiletype \033[1;31m(ex. pdf,xlsx,docx,csv / wordlist.txt) : \033[1;37m")
                page = input("\033[1;34mJumlah halaman \033[1;31m(ex. 3): \033[1;37m")
                os.system("clear")
                time.sleep(1)
                os.system(f"bash Sh -t {target} -e {filetype} -p {page}")
                print("")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("clear")
                logo()
            elif message == '02' or message == '2':
                owlsint3()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("clear")
                logo()
            elif message == '03' or message == '3':
                IP_Track()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("clear")
                logo()
            elif message == '04' or message == '4':
                os.system("clear")
                time.sleep(1)
                os.system("bash d")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("clear")
                logo()
            elif message == '05' or message == '5':
                time.sleep(1)
                print("")
                os.system("python2 b")
                print("")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("clear")
                logo()
            else:
                print("\033[1;31mInvalid options...!!!")
                time.sleep(1)
                os.system("clear")
                logo()

