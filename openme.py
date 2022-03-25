from cryptography.fernet import Fernet
import shutil
import os
import random
from time import sleep

print('THIS IS AN ENCRYPTION SOFTWARE BUILD BY URON......\n')
name = input('Enter the file name including extension: ')
print('your entered file will encrypt in...')
sleep(1)
print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)
os.system('cls')


def key():
    key = Fernet.generate_key()
    file = open('key.key','wb')
    file.write(key)
    file.close()

def encryption():
    file = open('key.key','rb')
    key = file.read()
    file.close()

    with open('yourFILES\\'+name,'rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open('enFILE.txt.encrypt','wb') as f:
        f.write(encrypted)
    
    shutil.rmtree('yourFILES')
    os.mkdir('yourFILES')

    check = os.path.isfile('passcode.txt')

    if check == False:
        up = '12345'
        do = '67890'
        c = up + do
        lenght = 4
        gen = "".join(random.sample(c,lenght))

        pa = open('passcode.txt','w')
        pa.write(str(gen))
        pa.close()
    
    else:
        pass

if os.path.isfile('key.key') == True:
    encryption()

if os.path.isfile('key.key') == False:
    key()
    encryption()
    