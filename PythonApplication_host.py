from socket import *
import time
import json


s = socket(AF_INET, SOCK_STREAM) # создаем сокет tcp
host = input('Введите адрес хоста: ')
s.bind((host, 65043)) # присваиваем порт
print ('Текущий адрес хоста: ', host)
print('Подключение... ')
s.listen(5) # пять запросов максимум
while True: # пока выполняется условие (пока есть запросы на подключение от клиента)
    client, addr = s.accept() # принимаем запрос на соединение
    data = client.recv(1000000) # указываем максимальное количество данных, которое можно принять от клиента
    print('message: ', data.decode('utf-8'), ', пришло от него: ', addr)
    msg = 'Симметричное шифрование'
    client.send(msg.encode('utf-8')) # передаем данные, предварительно упаковав их в байты
client.close()


