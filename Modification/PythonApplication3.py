#from socket import *
#import time
#import json


#s = socket(AF_INET, SOCK_STREAM) # создаем сокет tcp
#host = input('Введите адрес хоста: ')
#s.bind((host, 65043)) # присваиваем порт
#print(host)
#s.listen(5) # пять запросов максимум
#while True: # пока выполняется условие (пока есть запросы на подключение от клиента)
#    client, addr = s.accept() # принимаем запрос на соединение
#    data = client.recv(1000000) # указываем максимальное количество данных, которое можно принять от клиента
#    print('message: ', data.decode('utf-8'), ', пришло от него: ', addr)
#    msg = 'Симметричное шифрование'
#    client.send(msg.encode('utf-8')) # передаем данные, предварительно упаковав их в байты
#client.close()

# Внедрить код в интерфейс
# при подключении к другой сети проверять IP-адрес, чтобы установить хост
# В программе если оставлять Вернама, то подумать о сохранении ключа в файл
# с последующей передачей к клиенту
# Может, объединить шифры и ключом сделать число символов при шифре Цезаря по mod 10.
# Создать правило шифрования (по примеру выше)
# Заменить Виженера на AES.
#
#
#



#import numpy as np
#from pylfsr import LFSR

#state = [1, 1, 0, 0, 0] # Ключ (начальное значение)
#fpoly = [5,3,2,1] # Неприводимый полином
#L = LFSR(fpoly=fpoly,initstate =state, verbose=True)
#L.info()
#tempseq = L.runKCycle(40) # Период
#L.set(fpoly=[5,3,2,1])





#import math
#import random
#flag=True
#N = 30 # Число генераций
#print("""Значения по умолчанию:
#a = 3
#c = 5
#m = 7
#T(0) = 0
#""")
#print('Параметр а: Нажать 1')
#print('Параметр c: Нажать 2')
#print('Параметр m: Нажать 3')
#print('Параметр T(0): Нажать 4')
#while flag: # выбор для изменения определенного параметра
#    press = input('Какой параметр изменить: ')
#    if press == '1':
#        a = int(input('Введите число а: '))
#        print ('a = ',a)
#        m = 7
#        print ('m = ',m) # число m
#        c = 5 # число c
#        print ('c = ',c)
#        T0 = 1 #  число T(0)
#        print ('T(0) = ', T0)
#    elif press == '2':
#        c = int(input('Введите число c: '))
#        print ('c = ',c)
#        m = 17
#        print ('m = ',m) 
#        a = 3
#        print ('a = ',a)
#        T0 = 2
#        print ('T(0) = ', T0)
#    elif press == '3':
#        m = int(input('Введите число m: '))
#        print ('m = ',m)
#        c = 5
#        print ('c = ',c)
#        a = 3
#        print ('a = ',a)
#        T0 = 3
#        print ('T(0) = ', T0)
#    elif press == '4':
#        T0 = int(input('Введите число T(0): ')) 
#        print ('T(0) = ', T0)
#        m = 17
#        print ('m = ',m)
#        a = 3
#        print ('a = ',a)
#        c = 5
#        print ('c = ',c)
#    elif press == '':
#        m = 7 
#        a = 3 
#        c = 5
#        T0 = 0 
 
#    def lkm(): # объявление функцию
#        global x # создаем глобальную переменную
#        x = (a*x + c) % m # формула (a*Ti + c) (mod m) 
#        return int(x) # вернуть x как целое число
 
#    x=T0 # начиная с числа T(0)
#    for i in range(0,N): # цикл 
#        print(lkm())

#    flag = True if input('Начать заново?(y/n)') == 'y' else False



#import math
#import random
#flag=True
#N = 20 # Число генераций

#while flag: # выбор для изменения определенного параметра
#    press = input('Какой параметр изменить: ')
#    if press == '1':
#        m = 15
#        print ('m = ',m) 
#        a = 3
#        print ('a = ',a)
#        T0 = 4
#        print ('T(0) = ', T0)
#        #a = int(input('Введите число а: '))
#        def RandomPrime(): # Генерация D, взаимно простого с m
#            prime = False
#            while prime == False:
#                c = random.randint(2, m)
#                if (a*T0 + c) % m == 1:
#                    prime = True
#                    break
#                else:
#                    prime = False
#            return c
#        print ('c = ', RandomPrime())
 
#    def lkm(): # объявление функцию
#        global x # создаем глобальную переменную
#        x = (a*x + RandomPrime()) % m # формула (a*Ti + c) (mod m) 
#        return int(x) # вернуть x как целое число
 
#    x=T0 # начиная с числа T(0)
#    for i in range(0,N): # цикл 
#        print(lkm())

#    flag = True if input('Начать заново?(y/n)') == 'y' else False
 
 

import os
from functools import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from random import randint
from re import findall
from math import floor
import numpy as np 
from itertools import chain, islice
import re
import copy
import sys 
from socket import *
import time
import json

from tkinter import *
from tkinter import messagebox
from pprint import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as NavigationToolbar2TkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import datetime as dt
import sqlite3
class db:
    def sql(sql,data):
        with sqlite3.connect('logins.db') as db: # Подключение к базе данных
            cursor = db.cursor() # позволяет взаимодействовать с БД
            cursor.execute(sql,data)
            return (cursor.fetchall())
            db.commit()
    def getuserid(username,password):
        auth = db.sql("SELECT `userId` FROM `logins` WHERE `username` = ? AND `passwd` = ?",(username,password)) # Создание базы
        if (len(auth)==0):return -1
        else: return auth[0][0]
    def isadmin(user_id):
        auth = db.sql("SELECT `is_admin` FROM `logins` WHERE `userId` = ?",(user_id,)) # Создание админа в БД
        if(auth[0][0]==0):return False
        else:
            return True
    def register(username,password):
        db.sql("INSERT INTO `logins`(`username`,`passwd`) VALUES (?,?)",(username,password)) # добавление нового пользователя после регистрации
        return
    def getinfo(userid):
        return db.sql("SELECT * FROM `logins` WHERE `userId` = ?",(userid,)) # отображает информацию о пользователе по его ID
    
    #def user_sales_timeline(userid): #column 1 = date, column 2 = sales amt
    #    result = db.sql("SELECT DATE(SaleDate) AS 'Date', SUM(SaleValue) FROM Sales WHERE User = ? GROUP BY Date ORDER BY Date",(userid,))
    #    plot = [[],[]]
    #    for c in result:
    #        plot[0].append(c[0])
    #        plot[1].append(c[1])
    #    plot[0] = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in plot[0]]
    #    return plot
    #def sales_pie_chart():
    #    result = db.sql("SELECT (SELECT username FROM logins WHERE userId = User), SUM(SaleValue)*100/(SELECT SUM(SaleValue) FROM Sales) FROM Sales GROUP BY User",())
    #    plot = [[],[]]
    #    for c in result:
    #        plot[0].append(c[0])
    #        plot[1].append(c[1])
    #    return plot


class client:
    def __init__(self,user_id):
        if(user_id == -1):
            #создание макета полей
            self.username = None
            self.is_admin = None
            self.user_id = None
        else:
            result = db.getinfo(user_id)
            self.username = result[0][1]
            self.is_admin = (result[0][3]==1)
            self.user_id = user_id

class mainUI(Frame): ##################################### Здесь код на создание нового окна с приложением шифрования
    def logout(self):
        self.controller.user = client(-1)
        self.controller.show_frame("LoginFrame")
    #def deleteuser(userid):
    #    with sqlite3.connect('logins.db') as db: # Подключение к базе данных
    #        cursor = db.cursor() # позволяет взаимодействовать с БД
    #        db.sql("DELETE FROM `logins` where id = ?",(userid,))
    #        return (cursor.fetchall())
    #        db.commit()
        
    #    # Вводим данные для удаления
    #    srh = input('Введите ФИО')
    #    db.sql("DELETE FROM `logins` where id = ?",(userid,))
    #    cursor.close()
    #    conn.close()
    #    return

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.welcome_msg = StringVar(parent)
        #Label (self,textvariable = self.welcome_msg).grid(row=1,column=0,sticky='NW')
        Button (self, text="Выйти", command=self.logout).grid(row=1,column=2,sticky='NE')
        Button (self, text="Открыть программу", command=self.main_win).grid(row=2,column=2,sticky='NE')
        Button (self, text="Удалить пользователя", command=self.deleteuser).grid(row=3,column=2,sticky='NE')
        self.content = StringVar()
        #Label (self,textvariable = self.content).grid(row=2,column=0,columnspan=2,sticky='NSEW')
    
    def main_win(self): # СОЗДАНИЕ ОКНА ПРОГРАММЫ
        

        def revtxt(txt, mess):          #ОБРАБОТКА ТЕКСТА ПРИ РАСШИФРОВКЕ
            askrd = txt
            if (mess == "decode"):
                askrd = askrd.replace("ПРБЛ", " ")
                askrd = askrd.replace("ДВТЧ", ":")
                askrd = askrd.replace("ТИРЕ", "-")
                askrd = askrd.replace("ТЧЗТ", ";")
                askrd = askrd.replace("ВПРС", "?")
                askrd = askrd.replace("ВСКЛ", "!")
                askrd = askrd.replace("ЗПТ", ",")
                #askrd = askrd.replace("ТЧ ", "ТЧК")
                askrd = askrd.replace("ТЧК", ".")
        
                #askrd = askrd[:-1]
                # переменные для заполнения 
                n = ""
                p = ''
                message = askrd.split('.')
                for i in range(len(message)):
                    if message[i].startswith(' '):
                        message[i]=message[i][1:]
                    n = message[i][0:1].upper() + message[i][1:].lower() + "." # возвращают заглавные буквы
                    p = p + n
                p = p.replace(". . .","...")
                #p = p[:-2]
                askrd = p
            return askrd

        def worktxt(ask, sif):       #ОБРАБОТКА ТЕКСТА # ask - текст верхнего поля, sif - шифр
            askrd = str(ask.get(0.0, END))
            askrd = askrd.upper()
            askrd = askrd.replace(" ", "ПРБЛ")
            askrd = askrd.replace(":", "ДВТЧ")
            askrd = askrd.replace("-", "ТИРЕ")
            askrd = askrd.replace(";", "ТЧЗТ")
            askrd = askrd.replace("?", "ВПРС")
            askrd = askrd.replace("!", "ВСКЛ")
            askrd = askrd.replace(",", "ЗПТ")
            askrd = askrd.replace(".", "ТЧК")
            return askrd

        def createwin(sif, name):        #СОЗДАНИЕ СТАНДАРТА СТРАНИЦЫ. Зачищение нижних полей
            ask.delete(0.0, END) # верхнее поле
            key.delete(0, END) # поле ключа
            ans.delete(0.0, END) # нижнее поле

            if (sif == shenon):
                    key.insert(END, "Ключ не требуется")

            if (sif == diffihelfman):
                    key.insert(END, "g p a b")
                
        
            lab1.configure(text = name,bg = "#f7f7f7", fg = "red", font=("Courier",15)) # тескт сверху (названия)
            key.bind("<Return>", partial(sif, "code")) # горячие клавиши
            key.bind("<Double-Return>", partial(sif, "decode"))
            btn0.config(command = partial(sif, "code", "e")) # переназначение кнопок - шшифровать
            btn1.config(command = partial(sif, "decode", "e")) # расшифровать   e - event 

        def vijener(mess, e):     #ФУНКЦИЯ ШИФРОВКИ ПО ВИЖЕНЕРУ

            final=""
            message = worktxt(ask, None).upper().replace("\n","")
            #message = message.replace('.', 'тчк').upper() # Если в сообщении попадется точка, она заменется на тчк
            #message = message.replace(',', 'зпт').upper()
            #message = message.replace('-', 'тире').upper()
            #message = message.replace(';', 'тире').upper()
            #message = message.replace(' ', '')
            keyq = str(key.get().upper()).split("\n")
            keyq[:] = keyq[0]
            keyq *=((len(message))//len(keyq)+1)
            for index, symbol in enumerate(message):
                if mess == 'code': # если выбран 'cod'
                    if enumerate(message) != ' ':
                        temp = ord(symbol) + ord(keyq[index]) # подставляем символ текста с символом ключа и записываем полученный зашифрованный символ
                        #print(message)
                        #print (temp)
                if mess == "decode":
                    if symbol != ' ':
                        temp = ord(symbol) - ord(keyq[index]) # иначе делаем обратную замену символов для восстановления открытого текста

                final += chr(temp % 32 + ord('А')) # К переменной final прибавить получившийся символ

            #final = final.replace('ТЧК', '.') # Если в сообщении попадется точка, она заменется на тчк
            #final = final.replace('ЗПТ', ',') # Если в сообщении попадется запятая, она заменется на зпт
            #final = final.replace('ТИРЕ', '-') # Если в сообщении попадется тире, символ заменется на тире
            #final = final.replace('ТЧЗП', ';') # Если в сообщении попадется знак, символ заменется на тчзп
            #final = final [0:-1]
            ans.delete(0.0, END)
            ans.insert(END, revtxt(final, mess))

        def shenon(mess, e):
            def compress(key, val):         # аналогично itertools.compress - сжать строку на основе ASCII
                key = list(''.join(key))    # сделать все в одном списке ['........']
                val = list(''.join(val))
                return ''.join(v for v, k in zip(val, key) if k=='X') 

            from collections import Counter

            # Создание таблицы значений
            def divide_table(table):
                optimal_difference = sum(table.values())
                optimal_index = 0

                for i in range(len(table)):
                    current_difference = abs(sum(list(table.values())[:i]) - sum(list(table.values())[i:]))

                    if current_difference < optimal_difference:
                        optimal_difference = current_difference
                        optimal_index = i
                return dict({item for i, item in enumerate(table.items()) if i < optimal_index}), \
                        dict({item for i, item in enumerate(table.items()) if i >= optimal_index})

            # Преобразование 
            def shenon_get_codes(table, value='', codes={}):
                if len(table) != 1:
                    a, b = divide_table(table)
                    shenon_get_codes(a, value + '0', codes)
                    shenon_get_codes(b, value + '1', codes)
                else:
                    codes[table.popitem()[0]] = value
                return codes

            # Функция расшифровки символов
            def decode_symbol(table, code, index=0):
                if len(table) != 1:
                    a, b = divide_table(table)
                    if code[index] == '0':
                        return decode_symbol(a, code, index + 1)
                    else:
                        return decode_symbol(b, code, index + 1)
                else:
                    return table.popitem()[0]

            data = worktxt(ask, None)
            counter = Counter(data)

            # Символы первичного алфавита по убыванию вероятностей.
            sorted_freq = sorted(set(data), key=lambda letter: counter[letter], reverse=True)
            sorted_freq_dict = {letter: counter[letter] for letter in sorted_freq}

            code_table = shenon_get_codes(sorted_freq_dict)  # таблица символов со значениями частоты

            print(sorted_freq_dict)
            for symbol, key in sorted(code_table.items(), key=lambda item: len(item[1])):
                print(symbol, key, sep=': ')

                # Шифрование 
            encoded = [code_table[letter] for letter in data] # перебираем каждый символ
            encoded_bits = ''.join(encoded) # шифруем по битам
            encoded_str = [chr(int(encoded_bits[i:i + 8], 2)) for i in range(0, len(encoded_bits), 8)]

            # Вывод результатов
            print('исходный текст ({} bits): '.format(len(data) * 8), data)
            print('сжатый текст ({} bits): '.format(len(encoded_str) * 8), ''.join(encoded_str))
            print('Зашифрованные данные: {}'.format(encoded_bits))

            index = 0
            decoded_str = ''

            while index < len(encoded_bits):
                current = decode_symbol(sorted_freq_dict, encoded_bits, index)  # расшифровать очередной символ
                decoded_str += current             # добавить его в результат
                index += len(code_table[current])  # перейти на следующий

            print('расшифрованный текст: ', decoded_str)

            if mess == 'code':
                final = encoded_bits
                #ask.delete(0.0, END)
                #ask.insert(END, encoded_bits)
            if mess == 'decode':
                #ask.delete(0.0, END)
                final = revtxt(decoded_str, mess)
            final = final [0:-2]
            ans.delete(0.0, END)
            ans.insert(END, final)
            #ans.insert(END,revtxt(data, mess))

        def aes(mess, e):
            if __name__ == '__main__':

                import os
                import time

                #import aes128

                nb = 4  # число колонок состояния (для AES = 4)
                nr = 10  # количество раундов цикла cipher (если nb = 4 nr = 10)
                nk = 4  # длина ключа (в 32-битных словах)

                # Этот словарь будет использоваться в SubBytes(). 
                hex_symbols_to_int = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

                sbox = [
                    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
                    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
                    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
                    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
                    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
                    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
                    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
                    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
                    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
                    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
                    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
                    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
                    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
                    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
                    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
                    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
                ]

                # Обратный S-box для процедуры InvSubBytes
                inv_sbox = [
                    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
                    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
                    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
                    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
                    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
                    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
                    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
                    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
                    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
                    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
                    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
                    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
                    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
                    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
                    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
                    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
                ]

                # массив, который состоит из битов 32-разрядного слова и является постоянным для данного раунда.
                rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
                        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
                ]


                def encrypt(input_bytes, keyq):
                    """Функция шифрует input_bytes в соответствии с алгоритмом AES (128), используя ключ
                        Параметр args:
                        input_bytes -- список int менее 255, т. е. список байт. Длина input_bytes постоянно составляет 16
                        ключ - строка обычного текста. Эта же строка используется и при расшифровке
                        Возвращается:
                        Список int
                    """

                    # подготовим наши вводные данные: массив состояний (state) и KeySchedule
                    state = [[] for j in range(4)]
                    for r in range(4):
                        for c in range(nb):
                            state[r].append(input_bytes[r + 4 * c])
                    #print(state)

                    key_schedule = key_expansion(keyq)
                    #print('key_schedule ', key_schedule)
                    state = add_round_key(state, key_schedule)
                    #print(state)
                    for rnd in range(1, nr):
                        state = sub_bytes(state)
                        state = shift_rows(state)
                        state = mix_columns(state)
                        state = add_round_key(state, key_schedule, rnd)

                    state = sub_bytes(state)
                    state = shift_rows(state)
                    state = add_round_key(state, key_schedule, rnd + 1)

                    output = [None for i in range(4 * nb)]
                    for r in range(4):
                        for c in range(nb):
                            output[r + 4 * c] = state[r][c]

                    return output


                def decrypt(cipher, keyq):
                    """Функция расшифровывает шифр по алгоритму AES (128) с использованием ключа
                        Параметр args:
                        шифр -- список int менее 255, т.е. список байтов
                        ключ - строка обычного текста. Эта же строка используется и при расшифровке
                        Возвращается: Список int
                    """

                    # Подготовим алгоритм ввода данных: массив состояний и KeySchedule
                    state = [[] for i in range(nb)]
                    for r in range(4):
                        for c in range(nb):
                            state[r].append(cipher[r + 4 * c])

                    key_schedule = key_expansion(keyq)

                    state = add_round_key(state, key_schedule, nr)

                    rnd = nr - 1
                    while rnd >= 1:
                        state = shift_rows(state, inv=True)
                        state = sub_bytes(state, inv=True)
                        state = add_round_key(state, key_schedule, rnd)
                        state = mix_columns(state, inv=True)

                        rnd -= 1

                    state = shift_rows(state, inv=True)
                    state = sub_bytes(state, inv=True)
                    state = add_round_key(state, key_schedule, rnd)

                    output = [None for i in range(4 * nb)]
                    for r in range(4):
                        for c in range(nb):
                            output[r + 4 * c] = state[r][c]

                    return output


                def sub_bytes(state, inv=False):
                    """Эта трансформация заменяет каждый элемент массива на элемент из информации sbox
                        согласно алгоритму: в шестнадцатеричной системе счисления элемент из состояния
                        состоят из двух значений: 0x<val1><val2>. Необходимо забрать элемент с переправы
                        val1-строка и val2-столбец в Sbox и поместитть его вместо элемента в состояние.
                        Если расшифровка-преобразование включено (inv = = True), он использует InvSbox вместо Sbox.
                        Параметр args:
                        inv -- If value = = False означает, что функция является шифрованием-преобразованием.
                        Истина-расшифровка-трансформация
                    """

                    if inv == False:  # Шифрование
                        box = sbox
                    else:  # Расшифрование
                        box = inv_sbox

                    for i in range(len(state)):
                        for j in range(len(state[i])):
                            row = state[i][j] // 0x10
                            col = state[i][j] % 0x10

                            # Наш Sbox-это плоский массив, а не таблица. Находим элементы:
                            # Не менять список sbox!
                            box_elem = box[16 * row + col]
                            state[i][j] = box_elem

                    return state


                def shift_rows(state, inv=False):
                    """Это преобразование сдвигает строки состояния: вторые вращаются более чем на 1 байт,
                        третий вращается на 2 байта, четвертый-на 3 байта. А трансформация-не
                        прикасается к первому ряду. При шифровании преобразования используется сдвиг влево, при расшифровке-сдвиг вправо
                        Параметр args:
                        inv: если значение = = False означает, что функция находится в режиме шифрования. Режим истинной расшифровки
                    """

                    count = 1

                    if inv == False:  # Зашифрование
                        for i in range(1, nb):
                            state[i] = left_shift(state[i], count)
                            count += 1
                    else:  # Расшифрование
                        for i in range(1, nb):
                            state[i] = right_shift(state[i], count)
                            count += 1

                    return state


                def mix_columns(state, inv=False):
                    """При шифровании преобразование умножает каждый столбец состояния на
                        фиксированный полиномиал a (x) = {03}x**3 + {01}x**2 + {01}x + {02} в поле Галуа.
                        При расшифровке умножается на a'(x) = {0b}x* * 3 + {0d}x* * 2 + {09}x + {0e}
                        Параметр args:
                        inv: если значение = = False означает, что функция находится в режиме шифрования. Режим истинной расшифровки
                    """

                    for i in range(nb):

                        if inv == False:  # Зашифрование
                            s0 = mul_by_02(state[0][i]) ^ mul_by_03(state[1][i]) ^ state[2][i] ^ state[3][i]
                            s1 = state[0][i] ^ mul_by_02(state[1][i]) ^ mul_by_03(state[2][i]) ^ state[3][i]
                            s2 = state[0][i] ^ state[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(state[3][i])
                            s3 = mul_by_03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ mul_by_02(state[3][i])
                        else:  # Расшифрование
                            s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(state[2][i]) ^ mul_by_09(state[3][i])
                            s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(state[2][i]) ^ mul_by_0d(state[3][i])
                            s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(state[2][i]) ^ mul_by_0b(state[3][i])
                            s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(state[2][i]) ^ mul_by_0e(state[3][i])

                        state[0][i] = s0
                        state[1][i] = s1
                        state[2][i] = s2
                        state[3][i] = s3

                    return state


                def key_expansion(keyq):
                    """Он составляет список круглых клавиш для функции AddRoundKey.
                    """

                    key_symbols = [ord(symbol) for symbol in keyq]

                    # ChipherKey должен содержать 16 символов, чтобы заполнить 4*4 блок. Если это меньше, нужно дополнить ключ с помощью "0x01"
                    if len(key_symbols) < 4 * nk:
                        for i in range(4 * nk - len(key_symbols)):
                            key_symbols.append(0x01)

                    # сделать ChipherKey (который является основой KeySchedule)
                    key_schedule = [[] for i in range(4)]
                    for r in range(4):
                        for c in range(nk):
                            key_schedule[r].append(key_symbols[r + 4 * c])

                    # Продолжайте заполнять таблицу ключей (KeySchedule)
                    for col in range(nk, nb * (nr + 1)):  # col - номер колонки
                        if col % nk == 0:
                            # возьмем сдвинутую (col - 1) - ю колонку...
                            tmp = [key_schedule[row][col - 1] for row in range(1, 4)]
                            tmp.append(key_schedule[0][col - 1])

                            # измененить его элементы, используя информацию sbox-таблицу, как в SubBytes...
                            for j in range(len(tmp)):
                                sbox_row = tmp[j] // 0x10
                                sbox_col = tmp[j] % 0x10
                                sbox_elem = sbox[16 * sbox_row + sbox_col]
                                tmp[j] = sbox_elem

                            # и наконец XOR из 3 столбцов
                            for row in range(4):
                                s = (key_schedule[row][col - 4]) ^ (tmp[row]) ^ (rcon[row][int(col / nk - 1)])
                                key_schedule[row].append(s)

                        else:
                            # сделать XOR из 2 столбцов
                            for row in range(4):
                                s = key_schedule[row][col - 4] ^ key_schedule[row][col - 1]
                                key_schedule[row].append(s)

                    return key_schedule


                def add_round_key(state, key_schedule, round=0):
                    """Это преобразование объединяет состояние и KeySchedule вместе. Xor состояния и RoundSchedule (часть KeySchedule).
                    """

                    for col in range(nk):
                        # nb * round-это сдвиг, который указывает на начало части ключевого графика
                        s0 = state[0][col] ^ key_schedule[0][nb * round + col]
                        s1 = state[1][col] ^ key_schedule[1][nb * round + col]
                        s2 = state[2][col] ^ key_schedule[2][nb * round + col]
                        s3 = state[3][col] ^ key_schedule[3][nb * round + col]

                        state[0][col] = s0
                        state[1][col] = s1
                        state[2][col] = s2
                        state[3][col] = s3

                    return state


                # Небольшой блок полезных функций

                def left_shift(array, count):
                    """Повернуть массив в течение подсчета раз влево"""

                    res = array[:]
                    for i in range(count):
                        temp = res[1:]
                        temp.append(res[0])
                        res[:] = temp[:]

                    return res


                def right_shift(array, count):
                    """Повернуть массив в течение подсчета раз вправо"""

                    res = array[:]
                    for i in range(count):
                        tmp = res[:-1]
                        tmp.insert(0, res[-1])
                        res[:] = tmp[:]

                    return res


                def mul_by_02(num):
                    """Функция умножается на 2 в пространстве Галуа"""

                    if num < 0x80:
                        res = (num << 1)
                    else:
                        res = (num << 1) ^ 0x1b

                    return res % 0x100


                def mul_by_03(num):
                    """Функция умножается на 3 в пространстве Галуа
                    пример: 0x03*num = (0x02 + 0x01)num = num*0x02 + num
                    Дополнение в поле Галуа-это операция XOR
                    """
                    return (mul_by_02(num) ^ num)


                def mul_by_09(num):
                    return mul_by_02(mul_by_02(mul_by_02(num))) ^ num


                def mul_by_0b(num):
                    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num


                def mul_by_0d(num):
                    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num


                def mul_by_0e(num):
                    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)
    

        

                #print('Шаг 1:')
                #while True:
                #    print('Нажмите 1 для зашифрования или 2 для расшифрования')
                #    way = input()
                #    if way not in ['1', '2']:
                #        print('Сказано же, 1 или 2 :)')
                #        continue
                #    else:
                #        break
                #print()

                #print('Шаг 2:')
                #while True:
                #    print('Введите полное название файла(с расширением)')
                #    print('my_proverb.txt - для работы с пословицей')
                #    print('my_text.txt - для работы с текстом')
                #    input_path = os.path.abspath(input('Название файла: '))

                #    if os.path.isfile(input_path):
                #        break
                #    else:
                #        print('Это не правильный файл')
                #        continue
                #print()

                print('Шаг 3:')
                while True:
                    print('Введите свой ключ для шифрования / расшифрования. Ключ должен быть не больше 16 символов. Пожалуйста, не забывайте об этом!')
                    #keyq = key.get().upper()
                    keyq = key.get().upper()
                
        
                    if len(keyq) > 16:
                        print('Слишком длинный ключ. Попробуйте снова')
                        continue
        
                    for symbol in keyq:
                        if ord(symbol) > 0xff:
                            print('Этот ключ не сработает. Попробуйте другой, используя только латинский алфавит и цифры')
                            continue
        
                    break
                print('\r\nПожалуйста, подождите...')

                time_before = time.time()

                # Входные данные(путь к файлу)
                #with open(input_path, 'rb') as f:
            
                with open('my_proverb.txt', 'rb') as f:
                     data = f.read()
                #print(data)
                if mess == 'code':
                    crypted_data = []
                    temp = []
                    for byte in data:
                        temp.append(byte)
                        if len(temp) == 16:
                            crypted_part = encrypt(temp, keyq)
                            crypted_data.extend(crypted_part)
                            del temp[:]
                    else:
                        #padding v1
                        # crypted_data.extend(temp)

                        # padding v2
                        if 0 < len(temp) < 16:
                            empty_spaces = 16 - len(temp)
                            for i in range(empty_spaces - 1):
                                temp.append(0)
                            temp.append(1)
                            crypted_part = encrypt(temp, keyq)
                            crypted_data.extend(crypted_part)
            
                    out_path = os.path.join(os.path.dirname('my_proverb.txt') , 'crypted_' + os.path.basename('my_proverb.txt'))

                    # Входные данные
                    with open(out_path, 'wb') as ff:
                        ff.write(bytes(crypted_data))
                    final = bytes(crypted_data)

                if mess == 'decode':
                    decrypted_data = []
                    temp = []
                    for byte in data:
                        temp.append(byte)
                        if len(temp) == 16:
                            decrypted_part = decrypt(temp, keyq)
                            decrypted_data.extend(decrypted_part)
                            del temp[:] 
                    #else:
 
                    #    if 0 < len(temp) < 16:
                    #        empty_spaces = 16 - len(temp)
                    #        for i in range(empty_spaces - 1):
                    #            temp.append(0)
                    #        temp.append(1)
                    #        decrypted_part = encrypt(temp, keyq)
                    #        decrypted_data.extend(crypted_part) 
            
                    out_path = os.path.join(os.path.dirname('crypted_my_proverb.txt') , 'decrypted_' + os.path.basename('crypted_my_proverb.txt'))

                    # Выходные данные
                    #with open(out_path, 'r') as ff:
                    #    ff.write(decrypted_data)
                    #final = decrypted_data
                    with open('my_proverb.txt', 'r') as f:
                        data = f.read()
                    final = data

                time_after = time.time()
    
            print('Новый файл здесь:', out_path, '--', time_after - time_before, ' секунд')
            print('Если что-то не так, проверьте ключ')

            #final = final [0:-2]
            ans.delete(0.0, END)
            #ans.insert(END, bytes(crypted_data))
            ans.insert(END, final)
            #ans.insert(END,revtxt(data, mess)) 1q2w3e4r5t6y7u8i

        def diffihelfman(mess, e):
            class DH_Endpoint(object):
                    def __init__(self, public_key1, public_key2, private_key):
                            self.public_key1 = public_key1
                            self.public_key2 = public_key2
                            self.private_key = private_key
                            self.full_key = None
                        # Генерация открытого ключа
                    def generate_partial_key(self):
                            partial_key = self.public_key1**self.private_key
                            partial_key = partial_key % self.public_key2
                            return partial_key
                        # Вычисление секретного ключа
                    def generate_full_key(self, partial_key_r):
                            full_key = partial_key_r**self.private_key
                            full_key = full_key % self.public_key2
                            self.full_key = full_key
                            return full_key
            keyin = key.get().split(" ")
            g=int(keyin[0])
            p=int(keyin[1])
            a=int(keyin[2])
            b=int(keyin[3])
            Alice = DH_Endpoint(g, p, a)
            Bob = DH_Endpoint(g, p, b)

            # Алиса генерирует этот частичный ключ и отправим его Бобу по сети
            A=Alice.generate_partial_key()
            ask.delete(0.0, END)
            alisatxt="Открытый ключ Алисы: A = g**a mod p =" + str(g) + ' ^ ' + str(a) + ' mod ' + str(p) +" = " + str(A)
            ask.insert(END,alisatxt) 

            # Таким же образом Бобь посылает мне свои частичные ключи и передает их Алисе через сеть.
            B=Bob.generate_partial_key()
            Bobtxt="Открытый ключ Боба: B = g**b mod p =" + str(g) + ' ^ ' + str(b) + ' mod ' + str(p) +" = " + str(B)
            ans.delete(0.0, END)
            ans.insert(END,Bobtxt) 
        
            #Сравнение двух расчетов частичных ключей

            # Это код получения секретного ключа s Алисы
            a_full=Alice.generate_full_key(B)
            ask.insert(END,("\nАлиса вычисляет секретный ключ s: " + str(a_full))) 
        
            #А вот код Боба, полученный с использованием открытого ключа Алисы:
            b_full=Bob.generate_full_key(A)
            ans.insert(END,("\nБоб подсчитывает: " + str(b_full)))

        def color_config(widget, color, event):         #ФУНКЦИЯ ИЗМЕНЕНИЯ ЦВЕТА КЛАВИШ(СЛЕВА)
            widget.configure(bg = color)

        def close_win():        #ФУНКЦИЯ ЗАКРЫТИЯ ОКНА
            self.destroy()

        def openMenu(widget, e):        #ОТКРЫТИЕ МЕНЮ ДЛЯ ТЕКСТОВЫХ ПОЛЕЙ
            def Open_file(widget):          #ОТКРЫТИЕ ФАЙЛА
                    try:
                            of = askopenfilename()
                            file = open(of, "r")
                            widget.delete(0.0, END)
                            sub_of_file = file.read()
                            sub_of_file = sub_of_file[:-1]
                            widget.insert(END, sub_of_file)
                            file.close()
                    except:
                            pass
            def save_as(widget):            #СОХРАНЕНИЕ ФАЙЛА
                    try:
                            sf = asksaveasfilename()
                            ftxt = widget.get(1.0, END)
                            file = open (sf, "w")
                            file.write(ftxt)
                            file.close()
                    except UnicodeEncodeError:
                            showerror("ОШИБКА!!!","Файл не был сохранён!\nПрисутствуют запрещённые символы!")
                    except :
                            pass

            def sendmess(widget):           #ОТПРАВКА СООБЩЕНИЯ
                    def send(from_adr, e):
                        txt = widget.get(0.0 , END)[:-1]
                        #print (txt) # +
                        fa = str(from_adr.get()) 
                        #print (fa)# +

                        s = socket(AF_INET, SOCK_STREAM) # создаем сокет tcp
                        s.bind((fa, 65043)) # присваиваем порт
                        #print (fa) # +
                                
                        s.listen(5) # пять запросов максимум
                        #txt = txt.as_string()
                        #while True: # пока выполняется условие (пока есть запросы на подключение от клиента)
                        client, addr = s.accept() # принимаем запрос на соединение
                        data = client.recv(1000000) # указываем максимальное количество данных, которое можно принять от клиента
                                
                        print('message: ', data.decode('utf-8'), ', пришло от него: ', addr)
                        client.send(txt.encode('utf-8')) # передаем данные, предварительно упаковав их в байты
                        client.close()
                        answw.insert(END, data)

                        showinfo("УСПЕХ", "Сообщение было отправлено")
                            #except:
                                    #showerror("ОШИБКА", "Оправка сообщения не была произведена")
                            #answw.delete(0.0, END)
                            #answw.insert(END, pol)  
                        
                    #ОБЪЯВЛЕНИЕ ДОЧЕРНЕГО ОКНА
                
                    slave = Toplevel(self)
                    slave.title("Отправка сообщения")
                    slave.geometry("270x270+600+450")
                    slave.resizable(width = False, height = False)
                    slave.bind("<Escape>", lambda e: slave.destroy())
                    #ДОБАВЛЕНИЕ ПОЛЕЙ ВВОДА
                    lab1 = Label(slave, text = "Введите адрес хоста:")
                    lab1.place(x=10, y = 10)

                    from_addr = Entry(slave, width = 40)
                    from_addr.place(x = 10, y = 30)

                    lab2 = Label(slave, text = "Ответ получателя:")
                    lab2.place(x = 10 , y = 60)
                    answw = Text(slave, width = 30)
                    answw.place(x = 10 , y = 80, height = 150)

                    btnY = Button(slave, text = "Отправить",command = partial(send, from_addr, e))
                    btnY.place(x = 130, y = 235)

                    btnN = Button(slave, text = "Отмена", command = lambda: slave.destroy())
                    btnN.place(x = 200, y = 235)
                
                    slave.grab_set()
                    slave.focus_set()
                    slave.wait_window()
        
            l1 = Menu(self, tearoff = 0)
            l1.add_command(label="Open File", command = partial(Open_file, widget))
            l1.add_command(label="Save as...", command = partial(save_as, widget))
            l1.add_command(label="Send to...", command = partial(sendmess, widget))
            l1.post(e.x_root, e.y_root)    

        #ОБЪЯВЛЕНИЕ РОДИТЕЛЬСКОГО ОКНА                
        self = Tk()
        self.geometry('820x650+300+250')
        self.title("Shifr++")
        self.configure(bg = "#f7f7f7")
        self.resizable(width = False, height = False)
        self.bind("<Escape>", lambda e: self.destroy())

        #ДЕЛЕНИЕ РОДИТЕЛЬСКОГО ОКНА НА ФРЭЙМЫ
        frame1 = Frame(self, width = 150)
        frame1.pack(side = "left", fill = X)

        #СТАРТОВАЯ ИНФОРМАЦИЯ        
        lab1 = Label(self, text = "ШИФР ВЕРНАМА", bg = "#f7f7f7", fg = "red", font=("Courier",15))
        lab1.pack()

        word1 = Label(self,text = 'Исходное сообщение:' , bg = "#f7f7f7")
        ask = Text(self)
        word2 = Label(self,text = 'Ключ сообщения:', bg = "#f7f7f7" )
        key = Entry(self)
        word3 = Label(self,text = 'Преобразованное сообщение:', bg = "#f7f7f7")
        ans = Text(self)

        btn0 = Button(self,text = 'Шифровать')
        btn0.place(x = 625,y = 310,height = 25)

        btn1 = Button(self,text = 'Расшифровать')
        btn1.place(x = 706,y = 310, height = 25)

        btn0.config(command = partial(shenon, "code", "e")) # первоначальное окно
        btn1.config(command = partial(shenon, "decode", 'e'))

        ask.bind("<Button-3>", partial(openMenu, ask))
        ans.bind("<Button-3>", partial(openMenu, ans))
        key.bind("<Return>", partial(shenon, "code"))
        key.bind("<Double-Return>", partial(shenon, "decode"))
        key.insert(END, "Ключ не требуется")

        word1.place(x = 220,y=35)
        ask.place(x = 220,y=60, width = 575, height = 245)
        word2.place(x = 220,y=310)
        key.place(x = 330,y=313, width = 285)
        word3.place(x = 220, y =335)
        ans.place(x = 220,y= 360,width = 575, height = 240)

        lab2 = Label(self, text = "Created by \n Маковей Сергей 171-341")
        lab2.configure( bg = "#f7f7f7", fg = "red", font=("Courier",8))
        lab2.place(x = 630, y = 607)

        #ОБЪЯВЛЕНИЕ КНОПОК ВЫЗОВА ОКОН ШИФРОВОК
         # объявление, расположение, текст, размер
        button1 = Button(frame1,text = "ШИФР ВЕРНАМА", width = 26, height = 10, command = partial(createwin, shenon, "ШИФР ВЕРНАМА"))
        button1.pack()
        button1.bind("<Enter>", partial(color_config, button1, "#adff2f"))#зеленый
        button1.bind("<Leave>", partial(color_config, button1, "#f0f0f0"))

        button2 = Button(frame1,text = "ШИФР ВИЖЕНЕРА", width = 26, height = 10, command = partial(createwin, vijener, "ШИФР ВИЖЕНЕРА"))
        button2.pack()
        button2.bind("<Enter>", partial(color_config, button2, "#adff2f"))#зеленый
        button2.bind("<Leave>", partial(color_config, button2, "#f0f0f0"))

        button3 = Button(frame1,text = "AES", width = 26, height = 10, command = partial(createwin, aes, "AES"))
        button3.pack()
        button3.bind("<Enter>", partial(color_config, button3, "#adff2f"))#зеленый
        button3.bind("<Leave>", partial(color_config, button3, "#f0f0f0"))

        button4 = Button(frame1,text = "ОБМЕН КЛЮЧАМИ", width = 26, height = 11, command = partial(createwin, diffihelfman, "ОБМЕН КЛЮЧАМИ ПО ДИФФИ-ХЕЛМАНУ"))
        button4.pack()
        button4.bind("<Enter>", partial(color_config, button4, "#adff2f"))#зеленый
        button4.bind("<Leave>", partial(color_config, button4, "#f0f0f0"))

        self.protocol('WM_DELETE_WINDOW', close_win)
        
        self.mainloop()

    def refresh(self): # Очищение окон при переходах
        #add graph to column three
        
        ###f = Figure(figsize = (5,5), dpi = 100)
        ###a = f.add_subplot(111)
        ###plot = db.user_sales_timeline(self.controller.user.user_id)
        ###a.plot(plot[0],plot[1])
        ###f.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        ###f.gca().xaxis.set_major_locator(mdates.DayLocator())
        ###f.autofmt_xdate()
        
        #bring up the canvas
        canvas = FigureCanvasTkAgg(self)
        canvas.show()
        canvas.get_tk_widget().grid(row=3,columnspan = 2, sticky = 'NSEW')
        #navigation toolbar
        self.toolbar_frame = Frame(self).grid(row=4, columnspan = 2, sticky = 'NSEW')
        toolbar_frame = Frame(self)
        toolbar_frame.grid(row=4,columnspan = 2, sticky = S+E+W)
        toolbar = NavigationToolbar2TkAgg( canvas, toolbar_frame )
        #toolbar = NavigationToolbar2TkAgg(self, self.toolbar_frame)
        toolbar.update()
        canvas._tkcanvas.grid()
        self.welcome_msg.set("Hello %s!" %self.controller.user.username)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        if(self.controller.user.is_admin):
            self.content.set("You are an admin!")
        else:
            self.content.set("You are a user.")
        if(self.controller.user.is_admin):
            ###pie = db.sales_pie_chart()
            # Plot
            ###f = Figure(figsize = (5,5), dpi = 100)
            ###a = f.add_subplot(111)
            ###a.pie(pie[1], autopct='%1.1f%%', shadow=True, labels = pie[0])
            ###a.axis('equal')
            
            #plt.show()
            canvas = FigureCanvasTkAgg(self)
            canvas.show()
            canvas.get_tk_widget().grid(row=5,columnspan = 2, sticky = 'NSEW')
            
        
class RegisterFrame(Frame): # Поле регистрации
    def refresh(self):
        self.pass1.set('')
        self.pass2.set('')
        self.usEntry_reg.set('')
    def create_account(self):
        if(self.pass1.get()!=self.pass2.get()):
            self.pass1.set('')
            self.pass2.set('')
            messagebox.showwarning("Пароль не совпадает.","Проверьте пароль ещё раз. Ну проверь.")
        elif(self.pass1.get() == ''):
            messagebox.showwarning("Пустые поля.","Все поля должны быть заполнены.")
        else:
            try:
                db.register(self.usEntry_reg.get(),self.pass1.get())
                messagebox.showinfo("Аккаунт создан.","Войдите в систему под вашими учетными данными. :)")
            except:
                messagebox.showwarning("Ошибочка.","Введите другое Username или обратитесь к админу.")
            self.controller.show_frame("LoginFrame")
            self.controller.frames['LoginFrame'].usEntry.set(self.usEntry_reg.get())
    def __init__(self,parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.usEntry_reg = StringVar(parent)
        Label(self, text="Имя пользователя").grid(row=0,column=0) #Создание поля для имени пользователя
        Entry(self, textvariable = self.usEntry_reg).grid(row=0,column=1) # установка позиции поля

        self.pass1 = StringVar(parent)
        self.pass1.set('')
        self.pass2 = StringVar(parent)
        self.pass2.set('')
        
        Label(self, text="Пароль").grid(row=1,column=0) # также для пароля
        Entry(self, show="*", textvariable=self.pass1).grid(row=1,column=1)

        Label(self, text="Повторите пароль").grid(row=2,column=0) # и также для повторного пароля
        Entry(self, show="*", textvariable=self.pass2).grid(row=2,column=1)

        # Расположение кнопок
        Button(self, borderwidth=4, text="Регистрация", width=10, pady=4, command=self.create_account).grid(row=3,column=1)
        Button(self, borderwidth=4, text="Назад", width=10, pady=4, command=lambda: self.controller.show_frame("LoginFrame")).grid(row=4,column=1)

class LoginFrame(Frame): # Поле для авторизации (начальное окно)
    def refresh(self):
        self.pwEntry.set('')
        self.lbl_status.set("Статус")
        self.usEntry.set('')
    def check_password(self):
        self.user_id = db.getuserid(self.usEntry.get(),self.pwEntry.get())
        self.pwEntry.set('')
        if(self.user_id == -1):
            self.login_failure()
        else:
            self.usEntry.set('')
            self.login_success()
    def login_success(self):
        self.lbl_status.set("Авторизация прошла успешно.")
        self.controller.user = client(self.user_id)
        self.controller.show_frame("mainUI") # После успешной авторизации переход в frame
        
    def login_failure(self):
        self.lbl_status.set("Ошибка авторизации.")
        self.wrongpass +=1
        if(self.wrongpass >= 3):
            self.btn_login.configure(state = DISABLED)
            self.lbl_status.set("Отказано в доступе.")
        
    def __init__(self,parent,controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.wrongpass = 0
        #self = Frame(root, padx=20, pady=20)
        self.grid(row=0,column=0) # Создание рамки и установка ее положения
        self.usEntry = StringVar()
        self.pwEntry = StringVar()
        Label(self, text="Имя пользователя").grid(row=0,column=0) #Создание поля для имени пользователя
        Entry(self,textvariable = self.usEntry).grid(row=0,column=1)

        Label(self, text="Пароль").grid(row=1,column=0) #Создание поля для пароля
        Entry(self, show="*",textvariable = self.pwEntry).grid(row=1,column=1)

        self.btn_login = Button(self, borderwidth=4, text="Войти", width=10, pady=4, command=self.check_password) # Создание и расположение кнопкок
        self.btn_login.grid(row=2,column=1,columnspan=2)
        self.lbl_status = StringVar(parent)
        self.lbl_status.set("waiting input...")
        Button(self, borderwidth=4, text="Регистрация", width=10, pady=4, command=lambda: self.controller.show_frame("RegisterFrame")).grid(row=3,column=1,columnspan=2)
        
        Label(self,textvariable= self.lbl_status).grid(row=4,column=0,columnspan=2,sticky='W')
class SampleApp(Tk):
    def onFrameConfigure(self,canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))
    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width = canvas_width)
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.canvas = Canvas(self, borderwidth=0, background="#ffffff")
        # Графическое расположение контейнеров
        self.user = client(-1)
        container = Frame(self.canvas)
        vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_frame = self.canvas.create_window((4,4), window=container, anchor="nw")

        container.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure(canvas))
        self.canvas.bind('<Configure>', self.FrameWidth)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginFrame, RegisterFrame,mainUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # поместить все страницы в одно и то же место;
            # Который находится в верхней части порядка укладки
            # тот и будет виден.
            frame.grid(row=0, column=0, sticky="nsew") # ошибка при выходе из программы

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        try:
            frame.refresh()
        except AttributeError:
            pass
        # создание построенного окна
        frame.tkraise()

class Login(Tk):
    def register(self):
        pass
    

def main(): # Бесперебойная работа программы
    app = SampleApp()
    app.mainloop()

if __name__ == '__main__': main()