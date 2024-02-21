# -*- coding: utf-8 -*-
import zipfile,os,sys,time

def brute():
  filezip = raw_input("\033[1;90m(\033[1;95m+\033[1;90m) \033[1;96mEnter the Zip File Location (ex. /sdcard/folder/file.zip) \033[1;91m>\033[1;92m  ")
  wordlist = "angka.txt"
  print "\033[38;2;0;191;255mUnlock Zip File..."
  time.sleep(1)
  x = zipfile.ZipFile(filezip)
  p = open(wordlist, "r")
  a = 0
  for o in p.readlines():
    password = o.strip()
    try:
      x.extractall(pwd=password)
      print "\033[1;91m+\033[1;96m======================\033[1;91m+\033[1;96m=====================\033[1;91m+"
      print " \033[1;90m(\033[1;92m•\033[1;90m) \033[1;92mPassword Found"
      print " \033[1;90m(\033[1;92m•\033[1;90m) \033[1;92mPassword \033[1;90m~\033[1;96m•\033[1;93m>\033[1;95m",password
      break
    except:
      print " \033[1;90m(\033[1;91m+\033[1;90m) \033[1;91mFailed \033[1;90m~\033[1;96m•\033[1;93m>\033[1;96m",password


brute()
