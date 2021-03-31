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
    def deleteuser(userid):
        db.sql("DELETE FROM `logins` where id = ?",(userid,))
        return

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.welcome_msg = StringVar(parent)
        #Label (self,textvariable = self.welcome_msg).grid(row=1,column=0,sticky='NW')
        Button (self, text="Выйти", command=self.logout).grid(row=1,column=1,sticky='NE')
        #Button (self, text="Открыть программу", command=self.createwin).grid(row=2,column=1,sticky='NE')
        #Button (self, text="Удалить пользователя", command=self.deleteuser).grid(row=3,column=1,sticky='NE')
        self.content = StringVar()
        #Label (self,textvariable = self.content).grid(row=2,column=0,columnspan=2,sticky='NSEW')

        

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