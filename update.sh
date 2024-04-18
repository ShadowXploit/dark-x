cd $HOME
mv -f dark-x/node_modules .
rm -rf dark-x
git clone https://github.com/ShadowXploit/dark-x
mv -f node_modules dark-x
cd dark-x
bash module.sh
python3 bot.py
