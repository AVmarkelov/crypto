
import os
from tkinter import *
from functools import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from random import randint
from re import findall
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import *
import time
import json

scet1 = 0
scet2 = 0
scet3 = 0   

def color_config(widget, color, event):         #ФУНКЦИЯ ИЗМЕНЕНИЯ ЦВЕТА КЛАВИШ(СЛЕВА)
        widget.configure(bg = color)
        

def cezarbtn(): #ОКНО ШИФРОВКИ ПО ЦЕЗАРЮ
        global scet1, scet2, scet3 ,word2,answer,digits,answer1,fintxt, word3, btn_0,\
               btn_00, lab
        scet2=0
        scet3=0
        closewin2()
        closewin3()
        if scet1==0:
                lab = Label(root)
                lab.configure(text = "ШИФР ЦЕЗАРЯ",bg = "#f7f7f7", fg = "red", font=("Courier",15))
                word2 = Label(root,text = 'Исходное сообщение:' , bg = "#f7f7f7")
                answer = Text(root)
                answer.bind("<Alt-s>", partial(unicoding, "cod"))
                answer.bind("<Alt-d>", partial(unicoding, "decod"))
                answer.bind("<Alt-x>", partial(unicoding, None))
                digits = Label(root,text = 'Ключ сообщения:', bg = "#f7f7f7" )
                answer1 = Entry(root)
                word3 = Text(root)
                fintxt = Label(root,text = 'Преобразованное сообщение:', bg = "#f7f7f7")
                btn_0 = Button(root,text = 'Шифровать',command = partial(unicoding, "cod", None))
                lab.pack()
                word2.place(x = 200,y=35)
                answer.place(x = 200,y=60, width = 550, height =200)
                digits.place(x = 200,y=265)
                answer1.place(x = 310,y=268, width = 260)
                fintxt.place(x = 200, y =295)
                word3.place(x = 200,y= 320,width = 550, height = 200 )
                btn_0.place(x = 580,y=265,height = 25)
                answer.bind("<Button-3>", partial(openMenu, answer))
                answer1.bind("<Return>", partial(unicoding, "cod"))
                answer1.bind("<Double-Return>", partial(unicoding, "decod"))
                word3.bind("<Button-3>", partial(openMenu, word3))
                btn_00 = Button(root,text = 'Дешифровать',command = partial(unicoding, "decod", None))
                btn_00.place(x = 661,y = 265, height = 25)
        scet1 = 1

def vernambtn(): #ОКНО ШИФРОВКИ ПО ВЕРНАМУ
        closewin1()
        closewin3()
        global scet1, scet2, scet3,label_2_0, word_2_0, ask_2_0, digits_2_0, txtForKey,word_2_1, ans_2_0,\
               btn_2_0, btn_2_1
        scet1 = 0
        scet3 = 0
        if scet2 == 0:
                label_2_0 = Label (root)
                label_2_0.configure(text = "ШИФР ВЕРНАМА",bg = "#f7f7f7", fg = "red", font=("Courier",15))
                label_2_0.pack()
                
                word_2_0 = Label(root,text = 'Исходное сообщение:' , bg = "#f7f7f7")        
                word_2_0.place(x = 200,y=35)

                ask_2_0 = Text()
                ask_2_0.place(x = 200,y=60, width = 550, height =200)
                ask_2_0.bind("<Alt-s>", partial(vernamshifr, "cod"))
                ask_2_0.bind("<Alt-d>", partial(vernamshifr, "decod"))
                ask_2_0.bind("<Alt-x>", partial(vernamshifr, None))
                ask_2_0.bind("<Button-3>", partial(openMenu, ask_2_0))
                
                digits_2_0 = Label(root,text ='Ключ сообщения(При шифровке задается случайно каждому символу)', bg = "#f7f7f7" )
                digits_2_0.place(x = 200,y=260)

                txtForKey = Entry(root)
                txtForKey.place(x = 200, y = 281, width = 370)
                txtForKey.bind("<Return>", partial(vernamshifr, "cod"))
                txtForKey.bind("<Double-Return>", partial(vernamshifr, "decod"))

                word_2_1 = Label(root,text = 'Преобразованное сообщение:', bg = "#f7f7f7")
                word_2_1.place(x = 200, y =300)
                
                ans_2_0 = Text(root)
                ans_2_0.place(x = 200,y= 325,width = 550, height = 200 )
                ans_2_0.bind("<Button-3>", partial(openMenu, ans_2_0))

                btn_2_0 = Button(root, text = "Шифровать", command = partial(vernamshifr, "cod", None))
                btn_2_0.place(x=580,y=280,height = 25)

                btn_2_1 = Button(root, text = "Дешифровать", command = partial(vernamshifr, "decod", None))
                btn_2_1.place(x=661,y=280,height = 25)
                                        
        scet2 = 1


def aesbtn():       #ОКНО ШИФРОВКИ ПО AES
        global scet1, scet2, scet3, label_3_0, word_3_0, ask_3_0, digits_3_0,word_3_1, ans_3_0,\
               btn_3_0, Key_3_0, btn_3_1
        
        scet1 = 0
        scet2 = 0
        if scet3 ==0:
                closewin1()
                closewin2()
                
                label_3_0 = Label (root)
                label_3_0.configure(text = "ШИФР AES",bg = "#f7f7f7", fg = "red", font=("Courier",15))
                label_3_0.pack()
                
                word_3_0 = Label(root,text = 'Исходное сообщение:' , bg = "#f7f7f7")        
                word_3_0.place(x = 200,y=35)

                ask_3_0 = Text()
                ask_3_0.place(x = 200,y=60, width = 550, height =200)
                ask_3_0.bind("<Button-3>", partial(openMenu, ask_3_0))
                ask_3_0.bind('<Alt-s>', partial(aesshifr, "cod"))
                ask_3_0.bind('<Alt-d>', partial(aesshifr, "decod"))
                                
                digits_3_0 = Label(root,text ='Ключ сообщения:', bg = "#f7f7f7" )
                digits_3_0.place(x = 200,y=265)

                Key_3_0 = Entry(root)
                Key_3_0.place(x = 310,y=268, width = 260)
                Key_3_0.bind('<Return>', partial(aesshifr, "cod"))
                Key_3_0.bind('<Double-Return>', partial(aesshifr, "decod"))

                word_3_1 = Label(root,text = 'Преобразованное сообщение:', bg = "#f7f7f7")
                word_3_1.place(x = 200, y =295)
                
                ans_3_0 = Text(root)
                ans_3_0.place(x = 200,y= 320,width = 550, height = 200 )
                ans_3_0.bind("<Button-3>", partial(openMenu, ans_3_0))

                btn_3_0 = Button(root, text = "Шифровать", command = partial(aesshifr,"cod",  None))
                btn_3_0.place(x = 580,y=265,height = 25)

                btn_3_1 = Button(root, text = "Дешифровать", command = partial(aesshifr,"decod", None))
                btn_3_1.place(x = 661,y = 265, height = 25)                    
                
        scet3=1
        
def aesshifr(mess, e):     #ФУНКЦИЯ ШИФРОВКИ ПО AES
        global ask_3_0, Key_3_0, ans_3_0, Key_3_1
        try:
            if __name__ == '__main__':

                import os
                import time
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

                def encrypt(input_bytes, key):
                #"""Функция шифрует input_bytes в соответствии с алгоритмом AES (128), используя ключ
                #    Параметр args:
                #    input_bytes -- список int менее 255, т. е. список байт. Длина input_bytes постоянно составляет 16
                #    ключ - строка обычного текста. Эта же строка используется и при расшифровке
                #    Возвращается:
                #    Список int
                #"""

                    # подготовим наши вводные данные: массив состояний (state) и KeySchedule
                    state = [[] for j in range(4)]
                    for r in range(4):
                        for c in range(nb):
                            state[r].append(input_bytes[r + 4 * c])

                    key_schedule = key_expansion(key)

                    state = add_round_key(state, key_schedule)

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


                def decrypt(cipher, key):
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

                    key_schedule = key_expansion(key)

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


                def key_expansion(key):
                    """Он составляет список круглых клавиш для функции AddRoundKey.
                    """

                    key_symbols = [ord(symbol) for symbol in key]

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


                #final=""
                #message = ask_3_0.get(1.0, END).upper()
                crypted_data = ""
                decrypted_data = ""
                message = ask_3_0.get(1.0, END).upper()
                key = str(Key_3_0.get().upper()).split("\n")
                #temp[:] = temp[0]
                #key *=((len(message))//len(key)+1)
                #key = []
                if mess == "cod":
                        crypted_data = bytes(crypted_data)
                        #bytes(crypted_data)
                        temp = []
                        for byte in message:
                            temp.append(byte)
                            if len(temp) == 16:
                                crypted_part = encrypt(temp, key)
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
                                crypted_part = encrypt(temp, key)
                                crypted_data.extend(crypted_part)

                        #out_path = os.path.join(os.path.dirname(input_path) , 'crypted_' + os.path.basename(input_path))


                if mess == "decod":
                        decrypted_data = []
                        temp = []
                        for byte in message:
                            temp.append(byte)
                            if len(temp) == 16:
                                decrypted_part = decrypt(temp, key)
                                decrypted_data.extend(decrypted_part)
                                del temp[:] 
                        else:
                            #padding v1
                            # decrypted_data.extend(temp)
            
                            # padding v2
                            if 0 < len(temp) < 16:
                                empty_spaces = 16 - len(temp)
                                for i in range(empty_spaces - 1):
                                    temp.append(0)
                                temp.append(1)
                                decrypted_part = encrypt(temp, key)
                                decrypted_data.extend(crypted_part) 

                        #out_path = os.path.join(os.path.dirname(input_path) , 'decrypted_' + os.path.basename(input_path))
    
                crypted_data = crypted_data [0:-1]
                decrypted_data = decrypted_data [0:-1]
                ans_3_0.delete(0.0, END)
                ans_3_0.insert(END, crypted_data)
                ans_3_0.insert(END, decrypted_data)
        except:
                ans_3_0.delete(0.0, END)
                ans_3_0.insert(END, "ОШИБКА!!!")
        
              


def vernamshifr(mess, e):      #ФУНКЦИЯ ШИФРОВКИ ПО ВЕРНАМУ     
        global txtForKey, ask_2_0, ans_2_0, keys
        try:
                message = ask_2_0.get(0.0, END)
                keys = []
                final=""
                if mess == "cod":
                        for symbol in message:
                                key = randint(0,25);
                                keys.append(str(key))
                                final += chr((ord(symbol) + key))

                        keys = keys[0:-1]
                        final = final [0:-1]
                if mess == "decod":
                        keys =txtForKey.get()
                        keys = keys.split(" ")
                        message= message[:-1]
                        for i, s in enumerate(message):
                                final += chr(ord(s) - int(keys[i]))
                txtForKey.delete(0, END)
                txtForKey.insert(END, keys)
                ans_2_0.delete(0.0, END)
                ans_2_0.insert(END, final)
        except:
                ans_2_0.delete(0.0, END)
                ans_2_0.insert(END, "Ошибка ключа!!!")


def unicoding(mess, e):           #ФУНКЦИЯ ШИФРОВКИ ПО ЦЕЗАРЮ
        global answer1,answer,word3 
        try:
                symvol = answer.get(0.0, END)
                digit = int(answer1.get())
                new = ''
                symvol = symvol[:-1]
                if mess == "cod":
                        for i in symvol:
                                new += chr(ord(i) + digit)
                if mess == "decod":
                        for i in symvol:
                                new += chr(ord(i) - int(digit))
                word3.delete(0.0, END)
                word3.insert(END,new)
        except:
                word3.delete(0.0, END)
                word3.insert(END,"ОШИБКА КЛЮЧА!!!")


def closewin1():        #ЗАКРЫТИЕ СТРАНИЦЫ ЦЕЗАРЯ
        global word2,answer,digits,answer1,fintxt, word3, btn_0,\
               btn_00, lab
        try:
                lab1.pack_forget()
                lab.pack_forget()
                word2.place_forget()
                answer.place_forget()
                digits.place_forget()
                answer1.place_forget()
                fintxt.place_forget()
                word3.place_forget()
                btn_0.place_forget()
                btn_00.place_forget()
        except:
                pass

def closewin2():        #ЗАКРЫТИЕ СТРАНИЦЫ ВЕРНАМА
        global label_2_0, word_2_0, ask_2_0, digits_2_0, txtForKey,word_2_1, ans_2_0,\
               btn_2_0, btn_2_1
        try:
                lab1.pack_forget()
                ans_2_0.place_forget()
                ask_2_0.place_forget()                
                btn_2_0.place_forget()
                btn_2_1.place_forget()
                txtForKey.place_forget()
                word_2_1.place_forget()
                word_2_0.place_forget()
                label_2_0.pack_forget()
                digits_2_0.place_forget()
        except:
                pass

def closewin3():        #ЗАКРЫТИЕ СТРАНИЦЫ AES
        global label_3_0, word_3_0, ask_3_0, digits_3_0,word_3_1, ans_3_0,\
               btn_3_0, Key_3_0, btn_3_1
        try:
                lab1.pack_forget()
                Key_3_0.place_forget()
                ask_3_0.place_forget()
                ans_3_0.place_forget()
                btn_3_0.place_forget()
                btn_3_1.place_forget()
                word_3_1.place_forget()
                word_3_0.place_forget()             
                label_3_0.pack_forget()
                digits_3_0.place_forget()
                
        except:
                pass
        
def close_win():        #ФУНКЦИЯ ЗАКРЫТИЯ ОКНА
        ask = askyesno("Вам понравилась программа?", "Если нет - пользуйтесь ею пока не понравится")
        if ask ==1:
                root.destroy()               
        
      

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

        def sendmess(widget):           #ОТПРАВКА СОДЕРЖАНИЯ ПОЛЯ
                def send(from_adr, e):
                        try:
                                
                                txt = widget.get(0.0 , END)[:-1]
                                print (txt) # +
                                fa = str(from_adr.get()) 
                                print (fa)# +

                                s = socket(AF_INET, SOCK_STREAM) # создаем сокет tcp
                                s.bind((fa, 65043)) # присваиваем порт
                                print (fa) # +
                                #server = smtplib.SMTP('smtp.gmail.com', 587)
                                s.listen(5) # пять запросов максимум
                                #txt = txt.as_string()
                                #while True: # пока выполняется условие (пока есть запросы на подключение от клиента)
                                client, addr = s.accept() # принимаем запрос на соединение
                                data = client.recv(1000000) # указываем максимальное количество данных, которое можно принять от клиента
                                print('message: ', data.decode('utf-8'), ', пришло от него: ', addr)
                                #txt = 'Симметричное шифрование'
                                print (txt)
                                client.send(txt.encode('utf-8')) # передаем данные, предварительно упаковав их в байты
                                z = raw_input()
                                client.close()
                                slave.destroy()
                                showinfo("УСПЕХ", "Сообщение было отправлено")
                        except:
                                showerror("ОШИБКА", "Оправка сообщения не была произведена")
                        
                #ОБЪЯВЛЕНИЕ ДОЧЕРНЕГО ОКНА
                
                slave = Toplevel(root)
                slave.title("Отправка сообщения")
                slave.geometry("270x150+600+450")
                slave.resizable(width = False, height = False)
                slave.bind("<Escape>", lambda e: slave.destroy())
                #ДОБАВЛЕНИЕ ПОЛЕЙ ВВОДА
                lab1 = Label(slave, text = "Введите адрес хоста:")
                lab1.place(x=10, y = 10)

                from_addr = Entry(slave, width = 40)
                from_addr.place(x = 10, y = 30)


                btnY = Button(slave, text = "Отправить",command = partial(send, from_addr, e))
                btnY.place(x = 130, y =110)

                btnN = Button(slave, text = "Отмена", command = lambda: slave.destroy())
                btnN.place(x = 200, y = 110)
                
                slave.grab_set()
                slave.focus_set()
                slave.wait_window()
        
        l1 = Menu(root, tearoff = 0)
        l1.add_command(label="Open File", command = partial(Open_file, widget))
        l1.add_command(label="Save as...", command = partial(save_as, widget))
        l1.add_command(label="Send to...", command = partial(sendmess, widget))
        l1.post(e.x_root, e.y_root)               

#ОБЪЯВЛЕНИЕ РОДИТЕЛЬСКОГО ОКНА                
root = Tk()
root.iconbitmap("shifr.ico")
root.geometry('800x600+300+250')
root.title("Shyfr++")
root.configure(bg = "#f7f7f7")
root.resizable(width = False, height = False)
root.bind("<Escape>", lambda e: root.destroy())

#ДЕЛЕНИЕ РОДИТЕЛЬСКОГО ОКНА НА ФРЭЙМЫ
frame1 = Frame(root, width = 150)
frame1.pack(side = "left", fill = X)
  
#СТАРТОВАЯ ИНФОРМАЦИЯ        
lab1 = Label(root, text = "\nДобро пожаловать\nв\n \
программу\n шифровки и дешифровки\n\n\nВыберите\n необходимый\
 тип\n шифра слева", bg = "#f7f7f7", fg = "red", font=("Courier",14))
lab1.pack()

lab2 = Label(root, text = "Created by\n Маковей Сергей,\n Маркелов \
Александр")
lab2.configure( bg = "#f7f7f7", fg = "red", font=("Courier",8))
lab2.place(x = 650, y = 525)

#ОБЪЯВЛЕНИЕ КНОПОК ВЫЗОВА ОКОН ШИФРОВОК
button1 = Button(frame1,text = "ШИФР ЦЕЗАРЯ", width = 20, height = 13, command = cezarbtn)
button1.pack()
button1.bind("<Enter>", partial(color_config, button1, "#f0f0fe"))
button1.bind("<Leave>", partial(color_config, button1, "#f0f0f0"))


button2 = Button(frame1,text = "ШИФР ВЕРНАМА", width = 20, height = 12,  command = vernambtn)
button2.pack()
button2.bind("<Enter>", partial(color_config, button2, "#f0f0fe"))
button2.bind("<Leave>", partial(color_config, button2, "#f0f0f0"))

button3 = Button(frame1,text = "ШИФР AES", width = 20, height = 13, command = aesbtn)
button3.pack()
button3.bind("<Enter>", partial(color_config, button3, "#f0f0fe"))
button3.bind("<Leave>", partial(color_config, button3, "#f0f0f0"))
    
root.protocol('WM_DELETE_WINDOW', close_win)
        
root.mainloop()













