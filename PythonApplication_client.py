from socket import *
import json

stdate = """
[
    {
        "action": "presence",
        "type": "status",
        "user":{
            "account_name": "Sergo",
            "status": "User is online"
            }
    }
]"""


s = socket(AF_INET, SOCK_STREAM) # Создаем сокет TCP
server = input ('Введите адрес хоста: ')
s.connect((server, 65043)) # коннект к серверу
print ('Соединение с ', server)
list_obj = json.loads(stdate)
s.send(stdate.encode('utf-8'))
data = s.recv(1000000) #получаем не более 1000000 байт
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт') #получаем сообщение от сервера, декодировав байты юникод
s.close()
