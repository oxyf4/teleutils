from telethon import TelegramClient, sync
from telethon import functions, types
from telethon.errors.rpcerrorlist import *
from telethon.errors import *
import os

api_id = 15080432
api_hash = '6ff114e09ffca27d18934e612e996884'

if not os.path.exists("session"):
   os.makedirs("session")
def session():
    print("Создать сессию")
    phone = input("Введите телефон в формате (+7XXXXXXXXXX): ")
    client = TelegramClient("session/"+phone, api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone)
            client.sign_in(phone, input("Введите код: "))
            print("Создание сессии")
            print("Успешно создано! "+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except SessionPasswordNeededError:
            client.start(phone, input('Введите 2FA: '))
            print("Создание сессии")
            print("Успешно создано! "+phone)
            with open("list.txt","a") as file:
                file.write(phone+"\n")
        except Exception as e:
            print(R, e, " ", phone)
        client.disconnect()
    else:
        print("Сессия уже создана "+phone)
        client.disconnect()
    print("="*40)
while(True):
    session()