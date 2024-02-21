echo "Chcking Package..."
sleep 1
bin=$PREFIX/bin
dir=$(pwd)
echo -e "\033[1;97m Updating Packages!"
pkg update && pkg upgrade -y
if [ -e $bin/git ]; then 
  echo -e "\u001b[32mSkip install git but already installed!"
else 
  echo -e "\u001b[31mInstaling \u001b[31mgit!"
  pkg install git -y
  echo -e "\u001b[32mDone install git!"
fi
if [ -e $bin/python ]; then 
  echo -e "\u001b[32mSkip install python but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mpython!"
  pkg install python -y
  echo -e "\u001b[32mDone install python!"
fi
if [ -e $bin/python2 ]; then
  echo -e "\u001b[32mSkip install python2 but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mpython2!"
  pkg install python2 -y
  echo -e "\u001b[32mDone install python2!"
fi
if [ -e $bin/bash ]; then
  echo -e "\u001b[32mSkip install bash but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mbash!"
  pkg install bash -y
  echo -e "\u001b[32mDone install bash!"
fi
if [ -e $bin/curl ]; then
  echo -e "\u001b[32mSkip install curl but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mcurl!"
  pkg install curl -y
  echo -e "\u001b[32mDone install curl!"
fi
if [ -e $bin/ruby ]; then 
  echo -e "\u001b[32mSkip install ruby but already installed!"
else 
  echo -e "\u001b[31mInstaling \u001b[31mruby!"
  pkg install ruby -y 
  echo -e "\u001b[32mDone install ruby!"
fi
if [ -e $bin/nano ]; then 
  echo -e "\u001b[32mSkip install nano but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mnano!"
  pkg install nano -y 
  echo -e "\u001b[32mDone install nano!"
fi
if [ -e $bin/cowsay ]; then
  echo -e "\u001b[32mSkip install cowsay but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mcowsay!"
  pkg install cowsay -y
  echo -e "\u001b[32mDone install cowsay!"
fi
if [ -e $bin/toilet ]; then
  echo -e "\u001b[32mSkip install toilet but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mtoilet!"
  pkg install toilet -y
  echo -e "\u001b[32mDone install toilet!"
fi
if [ -e $bin/figlet ]; then
  echo -e "\u001b[32mSkip install figlet but already installed!"
else
  echo -e "\u001b[31mInstaling \u001b[31mfiglet!"
  pkg install figlet -y
  echo -e "\u001b[32mDone install figlet!"
fi
echo -e "\u001b[32mInstalling pip"
sleep 1
pip3 install colorama
pip2 install colorama
pip install requests
pip2 install requests
pip install datetime
pip2 install datetime
pip install useragent
pip install pyfiglet
pip3 install instaloader
echo -e "\u001b[32mDone installing pip!"

