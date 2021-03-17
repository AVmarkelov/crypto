#def atbash(s):
#    abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#    s = s.replace('.', 'тчк') # Если в сообщении попадется точка, она заменется на тчк
#    s = s.replace(',', 'зпт') # Если в сообщении попадется запятая, она заменется на зпт
#    s = s.replace('-', 'тире') # Если в сообщении попадется тире, символ заменется на тире
#    return s.translate(str.maketrans(
#      abc + abc.upper(), abc[::-1] + abc.upper()[::-1])) # функция шифрования

#def unatbash(a):
#    abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#    a = a.replace('тчк', '.') # Если в сообщении попадется точка, она заменется на тчк
#    a = a.replace('зпт', ',') # Если в сообщении попадется запятая, она заменется на зпт
#    a = a.replace('тире', '-') # Если в сообщении попадется тире, символ заменется на тире
#    return a
## Работа с текстом на 1000 символов
#a = print('Зашифрованный текст: ', atbash('Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь.'))
#decr = (unatbash('Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь.'))
#decr = unatbash(decr)
#print('\n')
#print('Расшифрованный текст: ', decr)
#print('\n')

## Работа с пословицей
#a = print('Зашифрованный текст: ', atbash('Кто хочет инжир из Лепе, пусть залезает на дерево.'))
#decr = (unatbash('Кто хочет инжир из Лепе, пусть залезает на дерево.'))
#decr = unatbash(decr)
#print('\n')
#print('Расшифрованный текст: ', decr)




# ЦЕЗАРЬ
#llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я', '.', ',', '-', '!', '?', ':'] # входной алфавит (прописные)
#blst = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я'] # входной алфавт (заглавные)
# # Можно проще, добавив upper
 
#def encryptCaesar(msg, shift=3): # Функция зашифрования, shift=3 - значение ключа
#    msg = msg.replace('.', 'тчк') # Если в сообщении попадется точка, она заменется на тчк
#    msg = msg.replace(',', 'зпт') # Если в сообщении попадется запятая, она заменется на зпт
#    msg = msg.replace('-', 'тире') # Если в сообщении попадется тире, символ заменется на тире
#    ret = ""
#    for x in msg:
#        if x in llst:
#            ind = llst.index(x)
#            ret += llst[ind+shift]
#        elif x in blst:
#            ind = blst.index(x)
#            ret += blst[ind+shift]
#        else:
#            ret += x
#    return ret
 
#def decryptCaesar(msg, shift=3): # Функция расшифрования
#    ret = ""
#    for x in msg:
#        if x in llst:
#            ind = llst.index(x)
#            ret += llst[ind-shift]
#        elif x in blst:
#            ind = blst.index(x)
#            ret += blst[ind-shift]
#        else:
#            ret += x
#    ret = ret.replace('тчк', '.') # Если в сообщении попадется точка, она заменется на тчк
#    ret = ret.replace('зпт', ',') # Если в сообщении попадется запятая, она заменется на зпт
#    ret = ret.replace('тире', '-') # Если в сообщении попадется тире, символ заменется на тире
#    return ret
# # Вывод результата
#print('Зашифрованный текст: ', encryptCaesar('Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь.'))
#print('\n')
#print('Расшифрованный текст: ', decryptCaesar(encryptCaesar('Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь.')))
#print('\n')
#print('Зашифрованный текст: ', encryptCaesar("Кто хочет инжир из Лепе, пусть залезает на дерево."))
#print('Расшифрованный текст: ', decryptCaesar(encryptCaesar("Кто хочет инжир из Лепе, пусть залезает на дерево.")))







# ПОЛИБИЙ
#text = 'Кто хочет инжир из Лепе, пусть залезает на дерево.'.lower()
##text = 'Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь.'.lower()
#keys = { # исходная таблица значений символов
#  'а':'11', 'б':'12', 'в':'13', 'г':'14', 'д':'15', 'е':'16',
#  'ж':'21', 'з':'22', 'и':'23', 'й':'24', 'к':'25', 'л':'26',
#  'м':'31', 'н':'32', 'о':'33', 'п':'34', 'р':'35', 'с':'36',
#  'т':'41', 'у':'42', 'ф':'43', 'х':'44', 'ц':'45', 'ч':'46',
#  'ш':'51', 'щ':'52', 'ъ':'53', 'ы':'54', 'ь':'55', 'э':'56',
#  'ю':'61', 'я':'62', '.':'63', ',':'64', '-':'65', ':':'66', ' ':'67'
#}
#crypt = "" # функция шифрования
#for i in text:

#  if i in keys:
#    crypt += keys[i] # каждый символ из сообщения заменяется порядковым номером из таблицы
#    crypt += " "
#print('Зашифрованный текст: ', crypt)
#print('\n')

#temp = ""
#decrypt = "" # функция расшифрования
#for i in crypt:
#  if i != " ":
#    temp += i # каждый символ записывается в переменную
#  else:
#    for j in keys:
#      if keys[j] == temp: # Сопоставление символов для обратной замены
#        decrypt += j
#    temp = ""
#print('Расшифрованный текст: ', decrypt)






# Тритемий
#abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
#print('Введите текст: ')
#stroka = input().lower()
#stroka = stroka.replace('.', 'тчк') # Если в сообщении попадется точка, она заменется на тчк
#stroka = stroka.replace(',', 'зпт') # Если в сообщении попадется запятая, она заменется на зпт
#stroka = stroka.replace('-', 'тире') # Если в сообщении попадется тире, символ заменется на тире
#stroka = stroka.replace(';', 'тчзп') # Если в сообщении попадется точка с запятой, символ заменется на тчзп
#sc = -1
#scl = 0
#otv = ''
#sh = 0
#for i in stroka:
#  sc = -1
#  for j in abc:
#    sc += 1
#    if j == i:
#      otv = otv + str(abc[(int(sc) + sh) % 32])
#      sh += 1
#print('Шифровка: ')
#print(otv)

#text = ''
#sc = -1
#scl = 0
#sh = 0
#for i in otv:
#  sc = -1
#  for j in abc:
#    sc += 1
#    if j == i:
#      text = text + str(abc[(int(sc) - sh) % 32])
#      sh += 1
#text = text.replace('тчк', '.') # Если в сообщении попадется точка, она заменется на тчк
#text = text.replace('зпт', ',') # Если в сообщении попадется запятая, она заменется на зпт
#text = text.replace('тире', '-') # Если в сообщении попадется тире, символ заменется на тире
#text = text.replace('тчзп', ';') # Если в сообщении попадется точка с запятой, символ заменется на тчзп
#print('Расшифровка: ')
#print(text)





# Виженер
#abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
#print('Введите текст: ')
#stroka = input().lower()
#print('Введите ключ: ')
#key = input()
#key1= key
#stroka = stroka.replace('.', 'тчк') # Если в сообщении попадется точка, она заменется на тчк
#stroka = stroka.replace(',', 'зпт') # Если в сообщении попадется запятая, она заменется на зпт
#stroka = stroka.replace('-', 'тире') # Если в сообщении попадется тире, символ заменется на тире
#stroka = stroka.replace('тчзп', ';') # Если в сообщении попадется точка с запятой, символ заменется на тчзп
#sc = -1
#otv = ''
#sh = 0
#scc = -1
#for i in stroka:
#  sc = -1
#  for a in abc:
#    sc += 1
#    if key == a:
#      sh = int(sc)
#  sc = -1
#  for j in abc:
#    sc += 1
#    if j == i:
#      otv = otv + str(abc[(int(sc) + sh) % 32])
#      key = str(abc[(int(sc) + sh) % 32])
#print('Шифровка: ')
#print(otv)

#text = ''
#sc = -1
#scl = 0
#sh = 0
#for i in otv:
#  sc = -1
#  for a in abc:
#    sc += 1
#    if key1 == a:
#      sh = int(sc)
#  sc = -1
#  for j in abc:
#    sc += 1
#    if j == i:
#      text = text + str(abc[(int(sc) - sh) % 32])
#      key1 = str(abc[int(sc)])
#text = text.replace('тчк', '.') # Если в сообщении попадется точка, она заменется на тчк
#text = text.replace('зпт', ',') # Если в сообщении попадется запятая, она заменется на зпт
#text = text.replace('тире', '-') # Если в сообщении попадется тире, символ заменется на тире
#text = text.replace('тчзп', ';') # Если в сообщении попадется точка с запятой, символ заменется на тчзп
#print('Расшифровка: ')
#print(text)





# ЫДЮЪЩЧЦДШТСИБЪЧРРПЦЩЯЧЪУВДММЛЛЦЩРКЭНСЦХХРВЯДЗП
# ВТЬЕКЛДЙИЕКВЭЪАКХНЩХРЧВКЧЪЫТЛСУЧВКВЕЬАТКВЕЫЩЯЧХОГАААФВВРЦНТННБШЦЛЛВТЬШЙЛДЙИШЙВЭЪАКХНЩХГЧВКЧЪЫУШВАВЮИЩЛЯЦММЪТУЧФБРМДЯХПЩГХТСАЦОХТЦКТАБТСЕЭЫУТВБШАЧЪЧТЗЛУГХКООУВХСКЗСЯШСЛЛСЬЭНОАГЙЪЦРБРЙХРЩВЦЙХПВИВЭШРНПЩГРЧРЛРЗЧФЭНЯЩРЗЬЮЧЪЧТЗНЦБАУПАЬЯШУПНЯХЮХЛСВЬРМЛЛЦЮГТРКЯХФЕМЫЬАШЪЪИВТВБТПГФХЙЗУЮЧУУМЫЬТЪТУГСДЗПЩНШТАУЬЗАДЭКПЕЬСЬНШЕЭНЫЦКЗАДРЗЪАБЪЪСЛХЦВБПЩЙЮЧЯУКВЬСЫЦКГЯЦРСУТИЬШМИЗСДЮИЩЗАДЗЧЩОЮЯШИПЕЮЧАЕМОГТЫНШИИЧУУШЕАЪБЕЦНСБАУПАЧЕЧФЭЕЭЕЯХУХЯЦШРЩСНШШЧЗНСБЮЙЛЯЮЪХНЪИГТВБЬЯГЧЬМЪТИДЮТРВВСЪЕКСЯУРПЛСЯХЫЕЬИЬТББМЫУЩПЧЗВАТБЧЗТИЬЗКЦОУЧЗКХСИЪВЕЦЗАДЗЧЩЭГАХИЩПБЧФТЛЗЮТЗКШИЦПБЕЧАРЭГЬГАРФЬНЫЕЫЯШИЛЗАДШУЭДСФРРНСЦХЮЦРБРЧЩЧВКЩЬЭНОАТВРРЛЕФАБКМЕТЧЧУЬТСДЪЕЭЧЫЧЬШШЕЖФРЧУЛЯГЮЗЬЕЭЙГЧЗЭИЕВБИОЮЯХШЬПЦЭЯУЬТСФШЧЗПЯГЫКПНПРВУВКДЯРЙУТИЬЪХЩВЯЪЧРУЯЮЪХЗЧОШХБЗЛЛЩЭЮЬРЛЯФХЬХАЩАЭШЪАЬУХМЬТЯЯРТЛСУЧЦКУСАЪБЕШНМЫЫНЬТГЙЪТЩВМЧЕУТЯЦФРМЪТУМХЪЛВЙЪХЗРГЯЬЮСШАГЕЧФЭСАТЫНЦИВДРХЮЮЭЧСКЦЬУЮХЦЭЕВЬЫУЪАЭЪШМЛМСВРТШЫЭЪЫНЬТЫТЬНМУЭТУНТПГДРПУНЦЕФУЬУЧЪТЭУСНБАУВЕВДМТЛКСВПЖЛНЮНХТЛНЩЗЪЕЫАЫЕЫНЭЧЫДРПЛЯОДЮЦЭРСЯЭЕКШГЕЪЕИЖЩЩЭБЭЧЫ


# Белаз
#cryptMode = input("[1]Зашифровать|[2]Расшифровать: ").upper()
#if cryptMode not in ['1','2']:
#    print("Ошибка: операция не найдена")
#    raise SystemExit
#startMessage = input("Введите текст: ").upper() # Ввести текст или пословицу
#startMessage = startMessage.replace('.', 'тчк').upper() # Если в сообщении попадется точка, она заменется на тчк
#startMessage = startMessage.replace(',', 'зпт').upper()
#startMessage = startMessage.replace(' ', '')
#print(startMessage) # вывести введенное сообщение
#oneKey = input("Ключ: ").upper() # создать ключ
#def encryptDecrypt(mode, message, key, final = ""): # функция зашифрования/расшифрования в зависимости от выбранного значения в начале
#    key *= len(message) // len(key) + 1 # Подстановка ключа к тексту
#    for index, symbol in enumerate(message):
#        if mode == '1': # если выбран '1'
#            if enumerate(message) != ' ':
#                temp = ord(symbol) + ord(key[index]) # подставляем символ текста с символом ключа и записываем полученный зашифрованный символ
#        else:
#            if symbol != ' ':
#                temp = ord(symbol) - ord(key[index]) # иначе делаем обратную замену символов для восстановления открытого текста
#        final += chr(temp % 32 + ord('А')) # К переменной final прибавить получившийся символ
#    return final
#a = (encryptDecrypt(cryptMode, startMessage, oneKey))
#a = a.replace('ТЧК', '.') # Если в сообщении попадется точка, она заменется на тчк
#a = a.replace('ЗПТ', ',') # Если в сообщении попадется запятая, она заменется на зпт
#a = a.replace('ТИРЕ', '-') # Если в сообщении попадется тире, символ заменется на тире
#print("Результат:", a)








#from re import findall

#alpha = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ 1234567890,.:;?!%()-")
#MatrixLength = 3; MatrixMod = len(alpha)
#MatrixSquare = MatrixLength * MatrixLength

## Проверка условий на ошибки
#def checkErrors(key):
#    if len(key) != MatrixSquare: return "Error: len(key) != %d"%MatrixSquare
#    elif not getDeter(sliceto(key)): return "Error: det(Key) = 0"
#    elif not getDeter(sliceto(key)) % MatrixMod: return "Error: det(Key) mod len(alpha) = 0"
#    else: return None

## Регулярное выражение - 3 символа сообщения
#def regular(text): 
#    template = r".{%d}"%MatrixLength
#    return findall(template, text)

## Кодирование символов в матрице
#def encode(matrix): 
#    for x in range(len(matrix)):
#        for y in range(MatrixLength):
#            matrix[x][y] = alpha.index(matrix[x][y])
#    return matrix

## Декодирование чисел в матрице + шифрование/расшифрование
#def decode(matrixM, matrixK, message = ""):
#    matrixF = []
#    for z in range(len(matrixM)):
#        temp = [0 for _ in range(MatrixLength)]
#        for x in range(MatrixLength):
#            for y in range(MatrixLength):
#                temp[x] += matrixK[x][y] * matrixM[z][y]
#            temp[x] = alpha[temp[x] % MatrixMod]
#        matrixF.append(temp)
#    for string in matrixF: 
#    	message += "".join(string)
#    return message

## Создаёт матрицу по три символа
#def sliceto(text): 
#    matrix = []
#    for three in regular(text): 
#    	matrix.append(list(three))
#    return encode(matrix)

## Нахождение обратного определителя матрицы
#def iDet(det):
#    for num in range(MatrixMod):
#        if num * det % MatrixMod == 1:
#            return num

## Алгебраические дополнения
#def algebratic(x, y, det): 
#    matrix = sliceto(mainKey)
#    matrix.remove(matrix[x])
#    for z in range(2):
#        matrix[z].remove(matrix[z][y])
#    det2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#    return (pow(-1, x + y) * det2x2 * iDet(det)) % MatrixMod

## Получение определителя матрицы
#def getDeter(matrix):
#    return \
#    (matrix[0][0] * matrix[1][1] * matrix[2][2]) + \
#    (matrix[0][1] * matrix[1][2] * matrix[2][0]) + \
#    (matrix[1][0] * matrix[2][1] * matrix[0][2]) - \
#    (matrix[0][2] * matrix[1][1] * matrix[2][0]) - \
#    (matrix[0][1] * matrix[1][0] * matrix[2][2]) - \
#    (matrix[1][2] * matrix[2][1] * matrix[0][0])

## Получение алгебраических дополнений
#def getAlgbr(det, index = 0):
#    algbrs = [0 for _ in range(MatrixSquare)]
#    for string in range(MatrixLength):
#        for column in range(MatrixLength):
#            algbrs[index] = algebratic(string, column, det)
#            index += 1
#    return algbrs

## Получение обратной матрицы
#def getIMatr(algbr):
#    return [
#        [algbr[0],algbr[3],algbr[6]],
#        [algbr[1],algbr[4],algbr[7]],
#        [algbr[2],algbr[5],algbr[8]]
#    ]

#print("Перед началом работы убедитесь, что файл в кодировке ANSI, чтобы программа смогла отобразить русские символы")
#cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
#if cryptMode not in ['E','D']:
#    print("Error: mode is not Found")
#    raise SystemExit

## Выбор, с чем будет работать программа - с пословицей или с текстом    
#filename = "my_text" #тест на 1000 символов
##filename = "my_proverb"
#handle = open(filename+".txt", "r")
#startMessage = handle.read().upper().replace("Ё","Е")
#filename = "key"
#handle = open(filename+".txt", "r")
#mainKey = handle.read().upper()
#handle.close()

## Проверка ошибок
#if checkErrors(mainKey): 
#    print(checkErrors(mainKey))
#    raise SystemExit

#for symbol in startMessage:

#    if symbol not in alpha:
#        startMessage = startMessage.replace(symbol,'')
        
        
#while len(startMessage) % MatrixLength != 0: 
#	startMessage += startMessage[-1]

## Основная функция
#def encryptDecrypt(mode, message, key):
#    MatrixMessage, MatrixKey = sliceto(message), sliceto(key)
#    if mode == 'E':
#        final = decode(MatrixMessage, MatrixKey)
#    else:
#        algbr = getAlgbr(getDeter(MatrixKey))
#        final = decode(MatrixMessage, getIMatr(algbr))
#    return final

#encdata=encryptDecrypt(cryptMode, startMessage, mainKey)
#print("Текст= ",startMessage)
#print("Ключ= ",mainKey)
#print("Зашифрованный текст = ",encdata)

#cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
#decrypt = encryptDecrypt(cryptMode, encdata, mainKey)
#print("Расшифрованное сообщение= ", decrypt)








# Плейфер
#from itertools import chain, islice
 
#def main(): # Создаем таблицу с ключом
#    keytable = [
#            ['Ф', 'И', 'Л', 'Ь', 'М', 'А'],
#            ['Б', 'В', 'Г', 'Д', 'Е', 'Ж'],
#            ['З', 'К', 'Н', 'О', 'П', 'Р'],
#            ['С', 'Т', 'У', 'Х', 'Ц', 'Ч'],
#            ['Ш', 'Щ', 'Ы', 'Э', 'Ю', 'Я'] ]
#    for i in keytable:
#      print(*i)
#    print('')
#    # !! Выбор, с чем будет работать программа - с пословицей или с текстом
#    ct = 'КТО ХОЧЕТ ИНЖИР ИЗ ЛЕПЕ, ПУСТЬ ЗАЛЕЗАЕТ НА ДЕРЕВО.'
#    #ct = 'САМАЯ ЛУЧШАЯ В МИРЕ КНИГА. ЖИЛ НА СВЕТЕ ЧЕЛОВЕЧЕК, КОТОРЫИ ВСЮ ЖИЗНЬ ПИСАЛ САМУЮ ЛУЧШУЮ В МИРЕ КНИГУ. ЖИЛ ОН ВПРОГОЛОДЬ, ВЕДЬ ЕМУ НЕКОГДА БЫЛО ДАЖЕ ЗАРАБАТЫВАТЬ НА ЖИЗНЬ; ВСЕ ЕГО ВРЕМЯ ЗАНИМАЛА КНИГА. СЕБЯ ЧЕЛОВЕЧЕК ЧИСЛИЛ В ПИСАТЕЛЯХ, НО ЗА ВСЮ ЖИЗНЬ НЕ ПРОДАЛ НИ ОДНОГО РАССКАЗА; ЕМУ НЕКОГДА БЫЛО ИХ ПИСАТЬ, ВЕДЬ У НЕГО БЫЛА КНИГА. ОН ЗАРОС, НЕДЕЛЯМИ НЕ МЫЛСЯ, А В ПАРИКМАХЕРСКОИ НЕ ПОЯВЛЯЛСЯ ГОДАМИ. ИЗ-ЗА ТОГО, ЧТО ОН НИГДЕ НЕ РАБОТАЛ И НИЧЕГО НЕ ПИСАЛ НА ПРОДАЖУ, ЕМУ ПРИХОДИЛОСЬ ЖИТЬ НА ПОДАЯНИЕ И ПИТАТЬСЯ ТЕМ, ЧТО НЕ ВСЯКАЯ СОБАКА СОГЛАСИЛАСЬ БЫ ВЗЯТЬ В ПАСТЬ. ЧЕЛОВЕЧЕК СЧИТАЛ, ЧТО ЭТО ЕГО ПРЕДНАЗНАЧЕНИЕ - САМАЯ ЛУЧШАЯ В МИРЕ КНИГА, И ОТДАВАЛ ВСЕГО СЕБЯ ЕИ. И КНИГА БРАЛА ЕГО СЕБЕ БЕЗ ОСТАТКА. ЕМУ НЕ ХВАТИЛО СОВСЕМ ЧУТЬ-ЧУТЬ - ОН НЕ УСПЕЛ ПОСТАВИТЬ ПОСЛЕДНЮЮ ТОЧКУ НАД И. КРОВОИЗЛИЯНИЕ В МОЗГ СВАЛИЛО ЧЕЛОВЕЧКА И ОН УПАЛ БЕЗ СТОНА НА СВЕЖЕИСПИСАННЫИ ЛИСТ. НОВЫЕ ХОЗЯЕВА, ВЬЕХАВШИЕ В ЕГО КОМНАТУ, СПАЛИЛИ СТАРУЮ МЕБЕЛЬ ВМЕСТЕ С КЛОПАМИ И ЗАМАРАННЫМИ ЛИСТКАМИ БУМАГИ, ТАК И НЕ УДОСУЖИВШИСЬ ПРОЧЕСТЬ НАКАРЯБАННЫЕ НА НИХ КАРАКУЛИ. ТАКАЯ ЭТО СТРАННАЯ ШТУКА - ЖИЗНЬ.'
#    print('Исходный текст: ',ct)
#    # Замена символов
#    ct = ct.replace(' ', '')
#    ct = ct.replace('.', 'ТЧК')
#    ct = ct.replace(',', 'ЗПТ')
#    ct = ct.replace('-', 'ТИРЕ')
#    ct = ct.replace(':', 'ДВТЧ')
#    ct = ct.replace(';', 'ТЧЗП')
 
#    # Выводим результаты зашифрования/расшифрования
#    pt = playfair_decode(ct, keytable)
#    print('Зашифрованный текст: ', pt)
#    et = playfair_encode(pt, keytable)
#    print('Расшифровка: ', et)
 
#    # функция расшифрования
#def playfair_decode(ct, keytable):
#    rows = len(keytable)
#    cols = len(keytable[0])
#    table = list(chain(*keytable))
#    pt = []
#    for pair in zip(islice(ct, 0, None, 2), islice(ct, 1, None, 2)):
#        pt.append(playfair_decode_pair(pair, table, rows, cols))
#    return "".join(chain(*pt))

# # нахождение соответствующей пары
#def playfair_decode_pair(pair, table, rows, cols):
#    x1, y1 = find_in_table(pair[0], table, rows, cols)
#    x2, y2 = find_in_table(pair[1], table, rows, cols)
#    x1, y1, x2, y2 = playfair_decode_transform(x1, y1, x2, y2, rows, cols)
#    return table[y1*cols + x1], table[y2*cols + x2]
 
#def find_in_table(c, table, rows, cols):
#    idx = table.index(c)
#    return idx % cols, idx // cols
 
#def playfair_decode_transform(x1, y1, x2, y2, rows, cols):
#    if x1 == x2:
#        y1 = (y1 + 1) % rows
#        y2 = (y2 + 1) % rows
#    elif y1 == y2:
#        x1 = (x1 + 1) % cols
#        x2 = (x2 + 1) % cols
#    else:
#        x1, x2 = x2, x1
#    return x1, y1, x2, y2

## функция зашифрования
#def playfair_encode(pt, keytable):
#  rows = len(keytable)
#  cols = len(keytable[0])
#  table = list(chain(*keytable))
#  et = []
#  for pair in zip(islice(pt, 0, None, 2), islice(pt, 1, None, 2)):
#    et.append(playfair_encode_pair(pair, table, rows, cols))
#  return "".join(chain(*et))


## нахождение пары для шифровки
#def playfair_encode_pair(pair, table, rows, cols):
#    x1, y1 = find_in_table(pair[0], table, rows, cols)
#    x2, y2 = find_in_table(pair[1], table, rows, cols)
#    x1, y1, x2, y2 = playfair_encode_transform(x1, y1, x2, y2, rows, cols)
#    return table[y1*cols + x1], table[y2*cols + x2]
 
 
#def playfair_encode_transform(x1, y1, x2, y2, rows, cols):
#    if x1 == x2:
#        y1 = (y1 - 1) % rows
#        y2 = (y2 - 1) % rows
#    elif y1 == y2:
#        x1 = (x1 - 1) % cols
#        x2 = (x2 - 1) % cols
#    else:
#        x1, x2 = x2, x1
#    return x1, y1, x2, y2

 
#if __name__ == "__main__":
#    main()






# Вертикальная перестановка
# !! Выбор, с чем будет работать программа - с пословицей или с текстом
#text = 'Кто хочет инжир из Лепе, пусть залезает на дерево.'.lower()
##text = 'Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь.'.lower()

#print('Исходный текст: ', text)
## Функция шифрования
#def encrypt(text, key):
#    text = text.replace('.', ' тчк') # Если в сообщении попадется точка, она заменется на тчк
#    text = text.replace(',', ' зпт') # Если в сообщении попадется запятая, она заменется на зпт
#    text = text.replace('-', 'тире') # Если в сообщении попадется - (тире), оно заменется на тире
#    text = text.replace(' ', '') # Если в сообщении попадется - (тире), оно заменется на тире
#    n = len(text) #
#    m = len(key)
#    d = n % m
#    if d != 0:
#        for i in range(m - d):
#            text += "_"
#        n = len(text)
#    p = ''
#    q = 0
#    while q < n:
#        p += ''.join(text[q+x] for x in key)
#        q += m
#    return p

#def decrypt(text, key): # функция расшифрования
#    # СТРЕЛА
#    key = [4, 5, 3, 1, 2, 0] # Ключ
#    dec_key=[]
#    for i in range(0,len(key)):
#        dec_key.append(key.index(i)) #переворачиваем ключ
#    dec_str = encrypt(text,dec_key) #используем функцию шифрования
#    dec_str = dec_str.replace('тчк', '.') # Если в сообщении попадется точка, она заменется на тчк
#    dec_str = dec_str.replace('зпт', ',') # Если в сообщении попадется запятая, она заменется на зпт
#    dec_str = dec_str.replace('тире', '-') # Если в сообщении попадется - (тире), оно заменется на тире
#    dec_str = dec_str.replace('_', '') # Если в сообщении попадется - (тире), оно заменется на тире
#    return dec_str


## в этот файл нужно записать исходный текст
#key = [4, 5, 3, 1, 2, 0]

## в этот файл записывается зашифрованный текст
#sh = encrypt(text, key)

## в этот файл записывается расшифрованный текст
#rassh = decrypt(sh, key)

#t = print('Зашифрованный текст: ', encrypt(text, [4, 5, 3, 1, 2, 0]))

#print('Расшифрованный текст: ', decrypt(encrypt(text,key), [4, 5, 3, 1, 2, 0]))








# Решетка Кордано
#import copy
#grid = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#	[1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
#	[0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
#	[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]

#text = "ктохочетинжиризлепезптпустьзалезаетнадеревотчкзаданиемносфюх"
#rows = 6
#cols = 10

#grid_step1 = copy.deepcopy(grid)
#tmp_grid = copy.deepcopy(grid)
#for i in range(len(tmp_grid)):
#	# print(tmp_grid[i])
#	tmp_grid[i].reverse() # переворот объекта (в данном случае grid, то есть таблицу)
#	# print(tmp_grid[i])
#	# print(grid[i])
#	# print()
	

#grid_step2 = copy.deepcopy(tmp_grid) # полное копирование перевёрнутого объекта

#grid_step3 = copy.deepcopy(grid_step2) # полное копирование объекта
#grid_step3.reverse() # переворот объекта

#grid_step4 = copy.deepcopy(grid_step1)
#grid_step4.reverse()

## Формирование таблицы для решетки (сетки)
#my_list = []
#for i in range(rows):
#	my_list.append([])
#	for j in range(cols):
#		my_list[i].append(0)
	

#char_count = 0
## вставка букв по исходному состоянию решётки
#for i in range(rows):
#	for j in range(cols):
#		if grid_step1[i][j]==1:
#			my_list[i][j] = text[char_count]
#			char_count += 1

## вставка букв по повороту решётки на 180 сверху
#for i in range(rows):
#	for j in range(cols):
#		if grid_step2[i][j]==1:
#			my_list[i][j] = text[char_count]
#			char_count += 1

## вставка букв по повороту решётки на 90 
#for i in range(rows):
#	for j in range(cols):
#		if grid_step3[i][j]==1:
#			my_list[i][j] = text[char_count]
#			char_count += 1
#print(len(text))
## вставка букв по повороту решётки на 180 снизу
#for i in range(rows):
#	for j in range(cols):
#		if grid_step4[i][j]==1:
#			my_list[i][j] = text[char_count]
#			char_count += 1
#for i in my_list:
#	print(i)

## Расшифровка
## вывод по исходному состоянию
#print ('\n 0:')
#for i in range(rows):
#  for j in range(cols):
#    if grid[i][j] == 1:
#      print (my_list[i][j], end = '')

## вывод после поворота на 180 градусов 
#print('\n')
#print('180 сверху:')
#for i in range(rows):
#  for j in range(cols):
#    if grid[i][cols - j - 1] == 1:
#      print (my_list[i][j], end = '')

## вывод после поворота на 90 градусов      
#print('\n')
#print('90:')
#for i in range(rows):
#  for j in range(cols):
#    if grid[rows-i-1][cols-j-1] == 1:
#      print (my_list[i][j], end = '')

## вывод после поворота на 180 градусов     
#print('\n')
#print('180 снизу:')
#for i in range(rows):
#  for j in range(cols):
#    if grid[rows-i-1][j] == 1:
#      print (my_list[i][j], end = '')
#print('\n')








 #Блокнот Шеннона
#def compress(key, val):         # аналогично itertools.compress - сжать строку на основе ASCII
#  key = list(''.join(key))    # сделать все в одном списке ['........']
#  val = list(''.join(val))
#  return ''.join(v for v, k in zip(val, key) if k=='X') 

#from collections import Counter

## Создание таблицы значений
#def divide_table(table):
#    optimal_difference = sum(table.values())
#    optimal_index = 0

#    for i in range(len(table)):
#        current_difference = abs(sum(list(table.values())[:i]) - sum(list(table.values())[i:]))

#        if current_difference < optimal_difference:
#            optimal_difference = current_difference
#            optimal_index = i
#    return dict({item for i, item in enumerate(table.items()) if i < optimal_index}), \
#           dict({item for i, item in enumerate(table.items()) if i >= optimal_index})

## Преобразование 
#def shenon_get_codes(table, value='', codes={}):
#    if len(table) != 1:
#        a, b = divide_table(table)
#        shenon_get_codes(a, value + '0', codes)
#        shenon_get_codes(b, value + '1', codes)
#    else:
#        codes[table.popitem()[0]] = value
#    return codes

## Функция расшифровки символов
#def decode_symbol(table, code, index=0):
#    if len(table) != 1:
#        a, b = divide_table(table)
#        if code[index] == '0':
#            return decode_symbol(a, code, index + 1)
#        else:
#            return decode_symbol(b, code, index + 1)
#    else:
#        return table.popitem()[0]

#data = input('Шифруемый текст: ')
#counter = Counter(data)

## Символы первичного алфавита по убыванию вероятностей.
#sorted_freq = sorted(set(data), key=lambda letter: counter[letter], reverse=True)
#sorted_freq_dict = {letter: counter[letter] for letter in sorted_freq}

#code_table = shenon_get_codes(sorted_freq_dict)  # таблица символов со значениями частоты

#print(sorted_freq_dict)
#for symbol, key in sorted(code_table.items(), key=lambda item: len(item[1])):
#    print(symbol, key, sep=': ')

#    # Шифрование 
#encoded = [code_table[letter] for letter in data] # перебираем каждый символ
#encoded_bits = ''.join(encoded) # шифруем по битам
#encoded_str = [chr(int(encoded_bits[i:i + 8], 2)) for i in range(0, len(encoded_bits), 8)]

## Вывод результатов
#print('исходный текст ({} bits): '.format(len(data) * 8), data)
#print('сжатый текст ({} bits): '.format(len(encoded_str) * 8), ''.join(encoded_str))
#print('Зашифрованные данные: {}'.format(encoded_bits))

#index = 0
#decoded_str = ''

#while index < len(encoded_bits):
#    current = decode_symbol(sorted_freq_dict, encoded_bits, index)  # расшифровать очередной символ
#    decoded_str += current             # добавить его в результат
#    index += len(code_table[current])  # перейти на следующий

#print('расшифрованный текст: ', decoded_str)











# A5/1
#import re
#import copy
#import sys 
## Регистры
#reg_x_length = 19
#reg_y_length = 22
#reg_z_length = 23

#key_one = ""
#reg_x = []
#reg_y = []
#reg_z = []

#def loading_registers(key): #загружает регистры, используя в качестве параметра 64-разрядный ключ
#	i = 0
#	while(i < reg_x_length): 
#		reg_x.insert(i, int(key[i])) #берет первые 19 элементов из ключа
#		i = i + 1
#	j = 0
#	p = reg_x_length
#	while(j < reg_y_length): 
#		reg_y.insert(j,int(key[p])) #берет следующие 22 элемента из ключа
#		p = p + 1
#		j = j + 1
#	k = reg_y_length + reg_x_length
#	r = 0
#	while(r < reg_z_length): 
#		reg_z.insert(r,int(key[k])) #берет следующие 23 элемента из ключа
#		k = k + 1
#		r = r + 1

#def set_key(key): #устанавливает ключ и загружает регистры если он содержит 0 и 1 и если это ровно 64 бита  
#	if(len(key) == 64 and re.match("^([01])+", key)):
#		key_one=key
#		loading_registers(key)
#		return True
#	return False

#def to_binary(plain): #преобразование открытого текста в двоичный формат
#	binary = list(map(lambda x: "{0:b}".format(ord(x)).zfill(11), plain))
#	return binary


#def get_majority(x,y,z): #получает большинство, суммируя значения x,y и z, и если оно больше 1 (например, два 1 и один 0), он возвращает большинство (1). В противном случае , если это два 0 и один 1, большинство возвращается как 0.
#	return (x&y | x&z | y&z)

#def get_keystream(length): #вычисление ключевого потока с помощью XOR соответствующих индексов
#	reg_x_temp = copy.deepcopy(reg_x)
#	reg_y_temp = copy.deepcopy(reg_y)
#	reg_z_temp = copy.deepcopy(reg_z)
#	keystream = []
#	i = 0
#	while i < length:
#		majority = get_majority(reg_x_temp[7], reg_y_temp[9], reg_z_temp[9])
#		if reg_x_temp[7] == majority: 
#			new = reg_x_temp[0] ^ reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18]
#			reg_x_temp_two = copy.deepcopy(reg_x_temp)
#			j = 1
#			while(j < len(reg_x_temp)):
#				reg_x_temp[j] = reg_x_temp_two[j-1]
#				j = j + 1
#			reg_x_temp[0] = new

#		if reg_y_temp[9] == majority:
#			new_one = reg_x_temp[0] ^ reg_y_temp[20] ^ reg_y_temp[21]
#			reg_y_temp_two = copy.deepcopy(reg_y_temp)
#			k = 1
#			while(k < len(reg_y_temp)):
#				reg_y_temp[k] = reg_y_temp_two[k-1]
#				k = k + 1
#			reg_y_temp[0] = new_one

#		if reg_z_temp[9] == majority:
#			new_two = reg_x_temp[0] ^ reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22]
#			reg_z_temp_two = copy.deepcopy(reg_z_temp)
#			m = 1
#			while(m < len(reg_z_temp)):
#				reg_z_temp[m] = reg_z_temp_two[m-1]
#				m = m + 1
#			reg_z_temp[0] = new_two

#		keystream.insert(i, reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
#		i = i + 1
#	return keystream


#def convert_binary_to_str(binary): #преобразует двоичный код в строку
#	s = "".join(map(lambda x: chr(int(x,2)), binary))
#	return str(s)

#def encrypt_decrypt(plain): #принимает открытый текст, преобразует его в двоичный код, получает ключевой поток после ввода длины двоичного файла и добавляет значения XOR ключевого потока и двоичного файла в строку
#	s = []
#	nov_kod=""
#	binary = to_binary(plain)
#	col_simv=len(binary * 11)
#	keystream = get_keystream(col_simv)
#	i = 0
#	for kod_simv in binary:
#		for ind_simv in range(len(kod_simv)):
#			nov_kod += str(int(kod_simv[ind_simv]) ^ keystream[i])
#			i += 1
#		s.append(nov_kod)
#		nov_kod=""
#	shifr=convert_binary_to_str(s)
#	return shifr

#def user_input_key(): #ввести ключ
#	tha_key = str(input('Введите 64-битный ключ: '))
#	if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
#		return tha_key
#	else:
#		while(len(tha_key) != 64 and not re.match("^([01])+", tha_key)):
#			if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
#				return tha_key
#			tha_key = str(input('Введите 64-битный ключ: '))
#	return tha_key

#def user_input_choice(): #выбрать операцию
#	someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\nНажмите 0, 1, или 2: '))
#	if (someIn == '0' or someIn == '1' or someIn == '2'):
#		return someIn
#	else:
#		while(someIn != '0' or someIn != '1' or someIn != '2'):
#			if (someIn == '0' or someIn == '1' or someIn == '2'):
#				return someIn
#			someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\nНажмите 0, 1, или 2: '))
#	return someIn

#def user_input_text(): #ввести открытый текст
#	#filename = "my_text"
#	#handle = open(filename+".txt", "r")
#	#someIn = handle.read().upper()
#	#handle.close()
#	try:
#		someIn = str(input('Введите открытый текст: ')) # Введите текст или пословицу
#		someIn = someIn.replace('.', ' тчк') # Если в сообщении попадется точка, она заменется на тчк
#		someIn = someIn.replace(',', ' зпт') # Если в сообщении попадется запятая, она заменется на зпт
#		someIn = someIn.replace('-', 'тире') # Если в сообщении попадется - (тире), оно заменется на тире
#		#someIn = someIn.replace(' ', '') # Если в сообщении попадется - (тире), оно заменется на тире
#		someIn = someIn.replace(';', 'тчзп')
#	except:
#		someIn = str(input('Попробуйте снова: '))
#	return someIn


#def the_main(): #основная функция, которая обрабатывает входные данные пользователя 
#	while(1):
#		key = str(user_input_key())
#		set_key(key)
#		first_choice = user_input_choice()
#		if(first_choice == '0'):
#			print('Хорошего дня!!!')
#			sys.exit(0)
#		elif(first_choice == '1'):
#			plaintext = str(user_input_text())
#			print("Исходный текст = ",plaintext,end="\n")
#			print("Зашифрованный текст = ",encrypt_decrypt(plaintext),end="\n\n\n")
#		elif(first_choice == '2'):
#			ciphertext = str(user_input_text())
#			print("Зашифрованный текст = ",ciphertext,end="\n")
#			decr = encrypt_decrypt(ciphertext)
#			decr = decr.replace('тчк', '.')
#			decr = decr.replace('зпт', ',')
#			decr = decr.replace('тире', '-')
#			decr = decr.replace('двтч', ':')
#			decr = decr.replace('тчзп', ';')
#			print("Расшифрованный текст = ", decr, end="\n\n\n")			

#the_main()

##Пример 64-битного ключа: 0101001000011010110001110001100100101001000000110111111010110111








#from Crypto.PublicKey import RSA
#from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
#from Crypto.Hash import SHA256
#import binascii
#import random
#import hashlib

#p = 15640288098315529097 # Большое простое число
#q = 11858041638789695267 # Большое простое число
#n = p * q # Произведение P и Q
#m = (p-1)*(q-1) # Функция Эйлера
#def RandomPrime(): # Генерация D, взаимно простого с m
#  prime = False
#  while prime == False:
#    d = random.randint(100000, 1000000)
#    if d % m != 1:
#        prime = True
#        break
#    else:
#        primt = False


#  return d

#def RandomE(): # Генерация E, секретного ключа
#  sec = False
#  while sec == False:
#    e = random.randint(100000, 1000000)
#    if e* RandomPrime() % m != 1:
#        sec = True
#        break
#    else:
#        secr = False


#  return e

#print('P: ', p)
#print('Q: ', q)
#print('Произведение простых чисел P и Q (открытый ключ): ', n)
#print('Функция Эйлера: ', m)
#print('Открытый ключ D, взаимно простой с M: ', RandomPrime())
#print('Вычисление секретного ключа: ED = 1 mod M ')
#print('E: ', RandomE())

## Создание 1024-битной RSA пары ключей (приватный + публичный ключ)
#keyPair = RSA.generate(bits=1024)
#pubKey = keyPair.publickey()

## Подпись сообщения
## !! Выберите, с каким текстом будет проведена работа: RSA.txt - пословица; RSA_text.txt - текст 1000+ символов.
##mess = open("RSA.txt", 'r', encoding='utf-8').read()
#mess = open("RSA_text.txt", 'r', encoding='utf-8').read()
#print('Исходное сообщение: ', mess)
#msg = mess.encode('utf-8')
#hash = SHA256.new(msg)
#signer = PKCS115_SigScheme(keyPair)
#signature = signer.sign(hash)
#print("Подпись: ", signature)
#hash_object = hashlib.sha256(msg)


## Проверка подписи
## !! Выберите, с каким текстом будет проведена работа: RSA.txt - пословица; RSA_text.txt - текст 1000+ символов.
##mess = open("RSA.txt", 'r', encoding='utf-8').read()
#mess = open("RSA_text.txt", 'r', encoding='utf-8').read()
##print(mess)
#msg = mess.encode('utf-8')
#hash = SHA256.new(msg)
#hex_dig = hash.hexdigest()
#verifier = PKCS115_SigScheme(pubKey)
#print('\nПроверка')
#print('h: ', hex_dig)
#print('H: ', hash_object.hexdigest())

#try:
#    verifier.verify(hash, signature)
#    print("Подпись верна.")
#except:
#    print("Подпись не верна.")










## Обмен ключами по ДИФФИ-ХЕЛЛМАНУ
#class DH_Endpoint(object):
#    def __init__(self, public_key1, public_key2, private_key):
#        self.public_key1 = public_key1
#        self.public_key2 = public_key2
#        self.private_key = private_key
#        self.full_key = None
#    # Генерация открытого ключа
#    def generate_partial_key(self):
#        partial_key = self.public_key1**self.private_key
#        partial_key = partial_key % self.public_key2
#        return partial_key
#    # Вычисление секретного ключа
#    def generate_full_key(self, partial_key_r):
#        full_key = partial_key_r**self.private_key
#        full_key = full_key % self.public_key2
#        self.full_key = full_key
#        return full_key
    # Функция шифрования
    #def encrypt_message(self, message):
    #    message = message.replace('.', ' тчк') # Если в сообщении попадется точка, она заменется на тчк
    #    message = message.replace(',', ' зпт') # Если в сообщении попадется запятая, она заменется на зпт
    #    message = message.replace('-', 'тире') # Если в сообщении попадется - (тире), оно заменется на тире
    #    #message = message.replace(' ', '') # Если в сообщении попадется - (тире), оно заменется на тире
    #    encrypted_message = ""
    #    key = self.full_key
    #    for c in message:
    #        encrypted_message += chr(ord(c)+key)
    #    return encrypted_message
    ## Функция расшифрования
    #def decrypt_message(self, encrypted_message):
    #    decrypted_message = ""
    #    key = self.full_key
    #    for c in encrypted_message:
    #        decrypted_message += chr(ord(c)-key)
    #    decrypted_message = decrypted_message.replace('тчк', '.') # Если в сообщении попадется точка, она заменется на тчк
    #    decrypted_message = decrypted_message.replace('зпт', ',') # Если в сообщении попадется запятая, она заменется на зпт
    #    decrypted_message = decrypted_message.replace('тире', '-') # Если в сообщении попадется - (тире), оно заменется на тире
    #   # decrypted_message = decrypted_message.replace('', ' ') # Если в сообщении попадется - (тире), оно заменется на тире
    #    return decrypted_message


# Определение секретного сообщения, которое Боб планирует отправить Алисе, 
# а также их закрытые и открытые ключи, заданные в наших конечных точках.

# !! Выберите, с каким текстом будет проведена работа
#message="Кто хочет инжир из Лепе, пусть залезает на дерево."
#message ="Самая лучшая в мире книга. Жил на свете человечек, который всю жизнь писал Самую Лучшую В Мире Книгу. Жил он впроголодь, ведь ему некогда было даже зарабатывать на жизнь; все его время занимала Книга. Себя человечек числил в писателях, но за всю жизнь не продал ни одного рассказа; ему некогда было их писать, ведь у него была Книга. Он зарос, неделями не мылся, а в парикмахерской не появлялся годами. Из-за того, что он нигде не работал и ничего не писал на продажу, ему приходилось жить на подаяние и питаться тем, что не всякая собака согласилась бы взять в пасть. Человечек считал, что это его предназначение - Самая Лучшая В Мире Книга, и отдавал всего себя Ей. И Книга брала его себе без остатка. Ему не хватило совсем чуть-чуть - он не успел поставить последнюю точку над И. Кровоизлияние в мозг свалило человечка и он упал без стона на свежеисписанный лист. Новые хозяева, въехавшие в его комнату, спалили старую мебель вместе с клопами и замаранными листками бумаги, так и не удосужившись прочесть накарябанные на них каракули. Такая это странная штука - жизнь."
#g=197 # g
#a=151 # a
#p=199 # p
#b=157 # b
#Alice = DH_Endpoint(g, p, a)
#Bob = DH_Endpoint(g, p, b)
##print("Открытый текст: ", message)
#print("Параметры:")
#print("g= ", g)
#print("a= ", a)
#print("p= ", p)
#print("b= ", b)

## Алиса генерирует этот частичный ключ и отправим его Бобу по сети
#A=Alice.generate_partial_key()
#print("Открытый ключ Алисы: A = g**a mod p = 197 ^151 mod 199 =", A) 

## Таким же образом Бобь посылает мне свои частичные ключи и передает их Алисе через сеть.
#B=Bob.generate_partial_key()
#print("Открытый ключ Боба: B = g**b mod p = 197 ^157 mod 199 =", B)


##Сравнение двух расчетов частичных ключей

## Это код получения секретного ключа s Алисы
#a_full=Alice.generate_full_key(B)
#print("Алиса вычисляет секретный ключ s: ", a_full) 

##А вот код Боба, полученный с использованием открытого ключа Алисы:
#b_full=Bob.generate_full_key(A)
#print("Боб подсчитывает: ", b_full) 

## Шифрование
#b_encrypted=Bob.encrypt_message(message)
#print("Зашифрованный текст: ",b_encrypted) 

## Расшифровка
#dec_message = Alice.decrypt_message(b_encrypted)
#print("Расшифрованный текст: ", dec_message)




#def sendmess(widget):           #ОТПРАВКА СОДЕРЖАНИЯ ПОЛЯ НА ПОЧТУ
#                def send(from_adr, e):
#                        try:
                                
#                                txt = widget.get(0.0 , END)[:-1]
#                                print (txt) # +
#                                fa = str(from_adr.get()) 
#                                print (fa)# +
#                                #msg = MIMEMultipart()
#                                #msg['Subject'] = "Зашифрованное сообщение"
#                                #msg.attach(MIMEText(txt, 'plain'))

#                                s = socket(AF_INET, SOCK_STREAM) # создаем сокет tcp
#                                s.bind((fa, 65043)) # присваиваем порт
#                                print (fa) # +
#                                #server = smtplib.SMTP('smtp.gmail.com', 587)
#                                s.listen(5) # пять запросов максимум
#                                #txt = txt.as_string()
#                                #while True: # пока выполняется условие (пока есть запросы на подключение от клиента)
#                                client, addr = s.accept() # принимаем запрос на соединение
#                                data = client.recv(1000000) # указываем максимальное количество данных, которое можно принять от клиента
#                                print('message: ', data.decode('utf-8'), ', пришло от него: ', addr)
#                                #txt = 'Симметричное шифрование'
#                                print (txt)
#                                client.send(txt.encode('utf-8')) # передаем данные, предварительно упаковав их в байты
#                                z = raw_input()
#                                client.close()
#                                #server.starttls()
#                                #server.login(fa,pas)
#                                #txt = msg.as_string()
#                                #server.sendmail(fa, txt)
#                                slave.destroy()
#                                showinfo("УСПЕХ", "Сообщение было отправлено")
#                        except:
#                                showerror("ОШИБКА", "Оправка сообщения не была произведена")
                        
#                #ОБЪЯВЛЕНИЕ ДОЧЕРНЕГО ОКНА
                
#                slave = Toplevel(root)
#                slave.title("Отправка сообщения")
#                slave.geometry("270x150+600+450")
#                slave.resizable(width = False, height = False)
#                slave.bind("<Escape>", lambda e: slave.destroy())
#                #ДОБАВЛЕНИЕ ПОЛЕЙ ВВОДА
#                lab1 = Label(slave, text = "Введите адрес хоста:")
#                lab1.place(x=10, y = 10)

#                from_addr = Entry(slave, width = 40)
#                from_addr.place(x = 10, y = 30)


#                btnY = Button(slave, text = "Отправить",command = partial(send, from_addr, e))
#                btnY.place(x = 130, y =110)

#                btnN = Button(slave, text = "Отмена", command = lambda: slave.destroy())
#                btnN.place(x = 200, y = 110)
                
#                slave.grab_set()
#                slave.focus_set()
#                slave.wait_window()





#def vijenershifr(mess, e):     #ФУНКЦИЯ ШИФРОВКИ ПО ВИЖЕНЕРУ
#        global ask_1_0, Key_1_0, ans_1_0, Key_1_1
#        try:
#                final=""
#                message = ask_1_0.get(1.0, END).upper()
#                message = message.replace('.', 'тчк').upper() # Если в сообщении попадется точка, она заменется на тчк
#                message = message.replace(',', 'зпт').upper()
#                message = message.replace('-', 'тире').upper()
#                message = message.replace(';', 'тире').upper()
#                message = message.replace(' ', '')
#                key = str(Key_1_0.get().upper()).split("\n")
#                key[:] = key[0]
#                key *=((len(message))//len(key)+1)
#                for index, symbol in enumerate(message):
#                    if mess == 'cod': # если выбран 'cod'
#                        if enumerate(message) != ' ':
#                            temp = ord(symbol) + ord(key[index]) # подставляем символ текста с символом ключа и записываем полученный зашифрованный символ
#                    if mess == "decod":
#                        if symbol != ' ':
#                            temp = ord(symbol) - ord(key[index]) # иначе делаем обратную замену символов для восстановления открытого текста
#                    final += chr(temp % 32 + ord('А')) # К переменной final прибавить получившийся символ
#                final = final.replace('ТЧК', '.') # Если в сообщении попадется точка, она заменется на тчк
#                final = final.replace('ЗПТ', ',') # Если в сообщении попадется запятая, она заменется на зпт
#                final = final.replace('ТИРЕ', '-') # Если в сообщении попадется тире, символ заменется на тире
#                final = final.replace('ТЧЗП', ';') # Если в сообщении попадется знак, символ заменется на тчзп
#                final = final [0:-1]
#                ans_1_0.delete(0.0, END)
#                ans_1_0.insert(END, final)
#        except:
#                ans_1_0.delete(0.0, END)
#                ans_1_0.insert(END, "ОШИБКА КЛЮЧА!!!")





#if __name__ == '__main__':
#    nb = 4  # число колонок состояния (для AES = 4)
#    nr = 10  # количество раундов цикла cipher (если nb = 4 nr = 10)
#    nk = 4  # длина ключа (в 32-битных словах)

#    # Этот словарь будет использоваться в SubBytes(). 
#    hex_symbols_to_int = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

#    sbox = [
#        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
#        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
#        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
#        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
#        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
#        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
#        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
#        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
#        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
#        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
#        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
#        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
#        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
#        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
#        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
#        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
#    ]

#    # Обратный S-box для процедуры InvSubBytes
#    inv_sbox = [
#        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
#        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
#        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
#        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
#        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
#        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
#        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
#        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
#        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
#        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
#        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
#        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
#        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
#        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
#        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
#        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
#    ]

#    # массив, который состоит из битов 32-разрядного слова и является постоянным для данного раунда.
#    rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
#            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
#            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
#            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
#    ]

#    def encrypt(input_bytes, key):
#    #"""Функция шифрует input_bytes в соответствии с алгоритмом AES (128), используя ключ
#    #    Параметр args:
#    #    input_bytes -- список int менее 255, т. е. список байт. Длина input_bytes постоянно составляет 16
#    #    ключ - строка обычного текста. Эта же строка используется и при расшифровке
#    #    Возвращается:
#    #    Список int
#    #"""

#        # подготовим наши вводные данные: массив состояний (state) и KeySchedule
#        state = [[] for j in range(4)]
#        for r in range(4):
#            for c in range(nb):
#                state[r].append(input_bytes[r + 4 * c])

#        key_schedule = key_expansion(key)

#        state = add_round_key(state, key_schedule)

#        for rnd in range(1, nr):
#            state = sub_bytes(state)
#            state = shift_rows(state)
#            state = mix_columns(state)
#            state = add_round_key(state, key_schedule, rnd)

#        state = sub_bytes(state)
#        state = shift_rows(state)
#        state = add_round_key(state, key_schedule, rnd + 1)

#        output = [None for i in range(4 * nb)]
#        for r in range(4):
#            for c in range(nb):
#                output[r + 4 * c] = state[r][c]

#        return output


#    def decrypt(cipher, key):
#        """Функция расшифровывает шифр по алгоритму AES (128) с использованием ключа
#            Параметр args:
#            шифр -- список int менее 255, т.е. список байтов
#            ключ - строка обычного текста. Эта же строка используется и при расшифровке
#            Возвращается: Список int
#        """

#        # Подготовим алгоритм ввода данных: массив состояний и KeySchedule
#        state = [[] for i in range(nb)]
#        for r in range(4):
#            for c in range(nb):
#                state[r].append(cipher[r + 4 * c])

#        key_schedule = key_expansion(key)

#        state = add_round_key(state, key_schedule, nr)

#        rnd = nr - 1
#        while rnd >= 1:
#            state = shift_rows(state, inv=True)
#            state = sub_bytes(state, inv=True)
#            state = add_round_key(state, key_schedule, rnd)
#            state = mix_columns(state, inv=True)

#            rnd -= 1

#        state = shift_rows(state, inv=True)
#        state = sub_bytes(state, inv=True)
#        state = add_round_key(state, key_schedule, rnd)

#        output = [None for i in range(4 * nb)]
#        for r in range(4):
#            for c in range(nb):
#                output[r + 4 * c] = state[r][c]

#        return output


#    def sub_bytes(state, inv=False):
#        """Эта трансформация заменяет каждый элемент массива на элемент из информации sbox
#            согласно алгоритму: в шестнадцатеричной системе счисления элемент из состояния
#            состоят из двух значений: 0x<val1><val2>. Необходимо забрать элемент с переправы
#            val1-строка и val2-столбец в Sbox и поместитть его вместо элемента в состояние.
#            Если расшифровка-преобразование включено (inv = = True), он использует InvSbox вместо Sbox.
#            Параметр args:
#            inv -- If value = = False означает, что функция является шифрованием-преобразованием.
#            Истина-расшифровка-трансформация
#        """

#        if inv == False:  # Шифрование
#            box = sbox
#        else:  # Расшифрование
#            box = inv_sbox

#        for i in range(len(state)):
#            for j in range(len(state[i])):
#                row = state[i][j] // 0x10
#                col = state[i][j] % 0x10

#                # Наш Sbox-это плоский массив, а не таблица. Находим элементы:
#                # Не менять список sbox!
#                box_elem = box[16 * row + col]
#                state[i][j] = box_elem

#        return state


#    def shift_rows(state, inv=False):
#        """Это преобразование сдвигает строки состояния: вторые вращаются более чем на 1 байт,
#            третий вращается на 2 байта, четвертый-на 3 байта. А трансформация-не
#            прикасается к первому ряду. При шифровании преобразования используется сдвиг влево, при расшифровке-сдвиг вправо
#            Параметр args:
#            inv: если значение = = False означает, что функция находится в режиме шифрования. Режим истинной расшифровки
#        """

#        count = 1

#        if inv == False:  # Зашифрование
#            for i in range(1, nb):
#                state[i] = left_shift(state[i], count)
#                count += 1
#        else:  # Расшифрование
#            for i in range(1, nb):
#                state[i] = right_shift(state[i], count)
#                count += 1

#        return state


#    def mix_columns(state, inv=False):
#        """При шифровании преобразование умножает каждый столбец состояния на
#            фиксированный полиномиал a (x) = {03}x**3 + {01}x**2 + {01}x + {02} в поле Галуа.
#            При расшифровке умножается на a'(x) = {0b}x* * 3 + {0d}x* * 2 + {09}x + {0e}
#            Параметр args:
#            inv: если значение = = False означает, что функция находится в режиме шифрования. Режим истинной расшифровки
#        """

#        for i in range(nb):

#            if inv == False:  # Зашифрование
#                s0 = mul_by_02(state[0][i]) ^ mul_by_03(state[1][i]) ^ state[2][i] ^ state[3][i]
#                s1 = state[0][i] ^ mul_by_02(state[1][i]) ^ mul_by_03(state[2][i]) ^ state[3][i]
#                s2 = state[0][i] ^ state[1][i] ^ mul_by_02(state[2][i]) ^ mul_by_03(state[3][i])
#                s3 = mul_by_03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ mul_by_02(state[3][i])
#            else:  # Расшифрование
#                s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(state[2][i]) ^ mul_by_09(state[3][i])
#                s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(state[2][i]) ^ mul_by_0d(state[3][i])
#                s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(state[2][i]) ^ mul_by_0b(state[3][i])
#                s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(state[2][i]) ^ mul_by_0e(state[3][i])

#            state[0][i] = s0
#            state[1][i] = s1
#            state[2][i] = s2
#            state[3][i] = s3

#        return state


#    def key_expansion(key):
#        """Он составляет список круглых клавиш для функции AddRoundKey.
#        """

#        key_symbols = [ord(symbol) for symbol in key]

#        # ChipherKey должен содержать 16 символов, чтобы заполнить 4*4 блок. Если это меньше, нужно дополнить ключ с помощью "0x01"
#        if len(key_symbols) < 4 * nk:
#            for i in range(4 * nk - len(key_symbols)):
#                key_symbols.append(0x01)

#        # сделать ChipherKey (который является основой KeySchedule)
#        key_schedule = [[] for i in range(4)]
#        for r in range(4):
#            for c in range(nk):
#                key_schedule[r].append(key_symbols[r + 4 * c])

#        # Продолжайте заполнять таблицу ключей (KeySchedule)
#        for col in range(nk, nb * (nr + 1)):  # col - номер колонки
#            if col % nk == 0:
#                # возьмем сдвинутую (col - 1) - ю колонку...
#                tmp = [key_schedule[row][col - 1] for row in range(1, 4)]
#                tmp.append(key_schedule[0][col - 1])

#                # измененить его элементы, используя информацию sbox-таблицу, как в SubBytes...
#                for j in range(len(tmp)):
#                    sbox_row = tmp[j] // 0x10
#                    sbox_col = tmp[j] % 0x10
#                    sbox_elem = sbox[16 * sbox_row + sbox_col]
#                    tmp[j] = sbox_elem

#                # и наконец XOR из 3 столбцов
#                for row in range(4):
#                    s = (key_schedule[row][col - 4]) ^ (tmp[row]) ^ (rcon[row][int(col / nk - 1)])
#                    key_schedule[row].append(s)

#            else:
#                # сделать XOR из 2 столбцов
#                for row in range(4):
#                    s = key_schedule[row][col - 4] ^ key_schedule[row][col - 1]
#                    key_schedule[row].append(s)

#        return key_schedule


#    def add_round_key(state, key_schedule, round=0):
#        """Это преобразование объединяет состояние и KeySchedule вместе. Xor состояния и RoundSchedule (часть KeySchedule).
#        """

#        for col in range(nk):
#            # nb * round-это сдвиг, который указывает на начало части ключевого графика
#            s0 = state[0][col] ^ key_schedule[0][nb * round + col]
#            s1 = state[1][col] ^ key_schedule[1][nb * round + col]
#            s2 = state[2][col] ^ key_schedule[2][nb * round + col]
#            s3 = state[3][col] ^ key_schedule[3][nb * round + col]

#            state[0][col] = s0
#            state[1][col] = s1
#            state[2][col] = s2
#            state[3][col] = s3

#        return state


#    # Небольшой блок полезных функций

#    def left_shift(array, count):
#        """Повернуть массив в течение подсчета раз влево"""

#        res = array[:]
#        for i in range(count):
#            temp = res[1:]
#            temp.append(res[0])
#            res[:] = temp[:]

#        return res


#    def right_shift(array, count):
#        """Повернуть массив в течение подсчета раз вправо"""

#        res = array[:]
#        for i in range(count):
#            tmp = res[:-1]
#            tmp.insert(0, res[-1])
#            res[:] = tmp[:]

#        return res


#    def mul_by_02(num):
#        """Функция умножается на 2 в пространстве Галуа"""

#        if num < 0x80:
#            res = (num << 1)
#        else:
#            res = (num << 1) ^ 0x1b

#        return res % 0x100


#    def mul_by_03(num):
#        """Функция умножается на 3 в пространстве Галуа
#        пример: 0x03*num = (0x02 + 0x01)num = num*0x02 + num
#        Дополнение в поле Галуа-это операция XOR
#        """
#        return (mul_by_02(num) ^ num)


#    def mul_by_09(num):
#        return mul_by_02(mul_by_02(mul_by_02(num))) ^ num


#    def mul_by_0b(num):
#        return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num


#    def mul_by_0d(num):
#        return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num


#    def mul_by_0e(num):
#        return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)


#def aesshifr(mess, e):     #ФУНКЦИЯ ШИФРОВКИ ПО AES 1q2w3e4r5t6y7u8i
#        global ask_3_0, Key_3_0, ans_3_0
#        #try:


#        #final=""
#        #message = ask_3_0.get(1.0, END).upper() 1q2w3e4r5t6y7u8i
#        crypted_data = []
#        #decrypted_data = bytes(crypted_data)
#        message = ask_3_0.get(1.0, END).upper()
#        key = (Key_3_0.get().split())

#        print (key)
#        #temp[:] = temp[0]
#        #key *=((len(message))//len(key)+1)
#        #key = []
#        #temp = []
#        if mess == "cod":
#                #crypted_data = []
#                #bytes(crypted_data)
#                temp = []
#                for byte in message:
#                    temp.append(byte)
#                    if len(temp) == 16:
#                        crypted_part = encrypt(temp, key)
#                        crypted_data.extend(crypted_part)
#                        del temp[:]
 
#                    #print (temp)
#                else:
#                    if 0 < len(temp) < 16:
#                        empty_spaces = 16 - len(temp)
#                        for i in range(empty_spaces - 1):
#                            temp.append(0)
#                        temp.append(1)
#                        crypted_part = encrypt(temp, key)
#                        crypted_data.extend(crypted_part)
#                #crypted_data = crypted_data[0:-1]


#        if mess == "decod":
#                decrypted_data = bytes(crypted_data)
#                temp = []
#                for byte in message:
#                    temp.append(byte)
#                    if len(temp) == 16:
#                        decrypted_part = decrypt(temp, key)
#                        decrypted_data.extend(decrypted_part)
#                        del temp[:] 

#                else:
#                    #padding v1
#                    # decrypted_data.extend(temp)
            
#                    # padding v2
#                    if 0 < len(temp) < 16:
#                        empty_spaces = 16 - len(temp)
#                        for i in range(empty_spaces - 1):
#                            temp.append(0)
#                        temp.append(1)
#                        decrypted_part = encrypt(temp, key)
#                        decrypted_data.extend(crypted_part) 

    
#        #crypted_data = crypted_data [0:-1]
#        #decrypted_data = decrypted_data [0:-1]
#        ans_3_0.delete(0.0, END)
#        ans_3_0.insert(END, crypted_data)
#        ans_3_0.insert(END, decrypted_data)
#        #except:
#        #        ans_3_0.delete(0.0, END)
#        #        print (ans_3_0.delete)
#        #        ans_3_0.insert(END, "ОШИБКА!!!")
        
              


#def vernamshifr(mess, e):      #ФУНКЦИЯ ШИФРОВКИ ПО ВЕРНАМУ     
#        global txtForKey, ask_2_0, ans_2_0, keys
#        try:
#                message = ask_2_0.get(0.0, END)
#                keys = []
#                final=""
#                if mess == "cod":
#                        for symbol in message:
#                                key = randint(0,25);
#                                keys.append(str(key))
#                                final += chr((ord(symbol) + key))

#                        keys = keys[0:-1]
#                        final = final [0:-1]
#                if mess == "decod":
#                        keys =txtForKey.get()
#                        keys = keys.split(" ")
#                        message= message[:-1]
#                        for i, s in enumerate(message):
#                                final += chr(ord(s) - int(keys[i]))
#                txtForKey.delete(0, END)
#                txtForKey.insert(END, keys)
#                ans_2_0.delete(0.0, END)
#                ans_2_0.insert(END, final)
#        except:
#                ans_2_0.delete(0.0, END)
#                ans_2_0.insert(END, "Ошибка ключа!!!")






#import crypto

import os
from tkinter import *
from functools import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from random import randint
from re import findall
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
from math import floor
import numpy as np 
from itertools import chain, islice
import re
import copy
import sys 
from socket import *
import time
import json

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




#def aes(mess, e):  # Заглушка
#        pass


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

        def sendmess(widget):           #ОТПРАВКА СООБЩЕНИЯ
                def send(from_adr, e):
                        #try:
                                
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
                                #pol = data.decode('utf-8')
                                #txt = 'Симметричное шифрование'
                                #print (txt)
                                client.send(txt.encode('utf-8')) # передаем данные, предварительно упаковав их в байты
                                #z = raw_input() # блокировка клавиатуры
                                client.close()
                                #server.starttls()
                                #server.login(fa,pas)
                                #txt = msg.as_string()
                                #server.sendmail(fa, txt)
                                #answw.delete(0.0, END)
                                answw.insert(END, data)
                                #ans.insert(END, pol)
                                #slave.destroy()
                                showinfo("УСПЕХ", "Сообщение было отправлено")
                        #except:
                                #showerror("ОШИБКА", "Оправка сообщения не была произведена")
                        #answw.delete(0.0, END)
                        #answw.insert(END, pol)  
                        
                #ОБЪЯВЛЕНИЕ ДОЧЕРНЕГО ОКНА
                
                slave = Toplevel(root)
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
        
        l1 = Menu(root, tearoff = 0)
        l1.add_command(label="Open File", command = partial(Open_file, widget))
        l1.add_command(label="Save as...", command = partial(save_as, widget))
        l1.add_command(label="Send to...", command = partial(sendmess, widget))
        l1.post(e.x_root, e.y_root)               

#ОБЪЯВЛЕНИЕ РОДИТЕЛЬСКОГО ОКНА                
root = Tk()
#root.iconbitmap("Shifr++.ico")
root.geometry('820x650+300+250')
root.title("Shifr++")
root.configure(bg = "#f7f7f7")
root.resizable(width = False, height = False)
root.bind("<Escape>", lambda e: root.destroy())

#ДЕЛЕНИЕ РОДИТЕЛЬСКОГО ОКНА НА ФРЭЙМЫ
frame1 = Frame(root, width = 150)
frame1.pack(side = "left", fill = X)


#СТАРТОВАЯ ИНФОРМАЦИЯ        
lab1 = Label(root, text = "ШИФР ВЕРНАМА", bg = "#f7f7f7", fg = "red", font=("Courier",15))
lab1.pack()

word1 = Label(root,text = 'Исходное сообщение:' , bg = "#f7f7f7")
ask = Text(root)
word2 = Label(root,text = 'Ключ сообщения:', bg = "#f7f7f7" )
key = Entry(root)
word3 = Label(root,text = 'Преобразованное сообщение:', bg = "#f7f7f7")
ans = Text(root)

btn0 = Button(root,text = 'Шифровать')
btn0.place(x = 625,y = 310,height = 25)

btn1 = Button(root,text = 'Расшифровать')
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

lab2 = Label(root, text = "Created by \n Маковей Сергей 171-341")
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

root.protocol('WM_DELETE_WINDOW', close_win)
        
root.mainloop()





# запись в файл исходных данных
# обработка файла (шифровка/дешифровка)
# вывод содержимого в поле (final)
# при расшифровке вывод содержимого исходного текста