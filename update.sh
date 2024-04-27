cd $HOME
mv -f dark-x/node_modules .
mv -f dark-x/.login.txt .
rm -rf dark-x
git clone https://github.com/ShadowXploit/dark-x
mv -f node_modules dark-x
mv -f .login.txt dark-x
cd dark-x
bash module.sh
python bot.py
