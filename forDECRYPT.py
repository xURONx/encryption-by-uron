import imp
from cryptography.fernet import Fernet

file = open('passcode.txt','r')
key2 = file.read()
file.close()

pa = input("IF YOU WANT TO DECRYPT A FILE PLEASE ENTER PASSCODE: ")

if pa == key2:
    file = open('key.key','rb')
    key = file.read()
    file.close()

    with open('enFILE.txt.encrypt','rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open('decryptedFILE.txt.decrypt','wb') as f:
        f.write(decrypted)  