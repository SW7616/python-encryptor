from cryptography.fernet import Fernet
import os
import time
from colorama import Fore, Back

newkeyperm = True
def keygen():
    if newkeyperm==True:
        global key; key = Fernet.generate_key()
        with open('enckey.key', 'wb') as filekey:
          filekey.write(key)
    return key
        
    

if (os.path.isfile("./enckey.key")==True):
    key = open("enckey.key", "rb")
    key = key.read()
    newkeyperm = False
    try:
        testtext = "hello"
        encryptiontest = Fernet(key).encrypt(testtext.encode())
    except ValueError:
        input(Fore.RED + "The key found in the file enckey.key is invalid. please delete the file for the program to work. \n Press enter to exit \n")
        exit()
    

print(Fore.WHITE +"Menu")
print("1. Encrypting")
print("2. Decrypting")


inp = input(">> ")
if(inp=="1"):
   keygen() 
   print("Key:", key.decode())
   inp = input("1. File \n 2. Text \n >>>> ")
   if(inp=="1"):
        path = input('Enter path of file: ')
        print('The path of file : ', path)
        
        try:
            with open(path, 'rb') as file:
                original = file.read()
        except FileNotFoundError:
            print(Fore.RED + "Please enter a valid directory next time.")
            input("Press enter to exit the program \n")
            exit()
        print('Note : Dont lose your key.')
        encrypted = Fernet(key).encrypt(original)
        with open(path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted) 
    
        file.close()
    
        print('Encryption Done...')
        time.sleep(5)
        input("press enter to exit \n") 
        exit()
   elif(inp=="2"):
        text = input("enter your text to encrypt \n >>> ")
        encMessage = Fernet(key).encrypt(text.encode())
        print("The encrypted message: " + encMessage.decode())
        print("Remember your key, store it in a safe place before you shut the program.")
        time.sleep(5)
        input("press enter to exit the program. ") 
elif(inp=="2"):
    inp = input("1. Text \n 2. File \n >>>> ")
    if(inp=="1"):
        dekey = input("Enter the key of the encrypted text: ")
        encMessage = input("Now enter the encrypted message: ")
        try:
            decMessage = Fernet(dekey).decrypt(encMessage).decode()
        except ValueError:
            print(Fore.RED + "The specified key is an invalid key, please make sure your key is 32 characters and isnt wrapped with b'' ")
            input("Press enter to exit the program \n")
            exit()
        print("The message is: " + decMessage)
        time.sleep(2)
        input("press enter to exit the program. ") 
    elif(inp=="2"):
        path = input('Enter path of file: ')
        
        try:
            with open(path, 'rb') as file:
                original = file.read()
        except FileNotFoundError:
            print(Fore.RED + "Please enter a valid directory next time.")
            input("Press enter to exit the program \n")
            exit()
        key = input('Enter the key: ')
        try:
            decrypted = Fernet(key).decrypt(original)
        except ValueError:
            print(Fore.RED + "The specified key is an invalid key, please make sure your key is 32 characters and isnt wrapped with b'' ")
            input("Press enter to exit the program \n")
            exit()
        with open(path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted) 
    
        file.close()
    
        print('Decryption Done...')
        time.sleep(5)
        input("press enter to exit \n") 
        exit()