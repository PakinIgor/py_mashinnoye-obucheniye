"""
import webbrowser
webbrowser.open("https://stepik.org/course/67")

# ->*https://fooobar.com/questions/8105644/how-to-insert-links-in-python
"""
"""
> Визуализатор - http://pythontutor.com/visualize.html - позволяет пошагово показывать работу вашей программы, что крайне полезно
"""

# 1. Операторы. Переменные. Типы данных. Условия

##1.1 Общая информация о курсе

##1.2 Введение: программы и Python. Проверка заданий

##1.3 Интерактивный режим Python. IPython

##1.4 Установка Python на компьютер

##1.5 Операции с целыми числами

##1.6 Операции с вещественными числами

##1.7 Типы данных

##1.8 Переменные. Стандартный ввод/вывод

###Тимофей обычно спит ночью XX часов и устраивает себе днем тихий час на YY минут. Определите, сколько всего минут Тимофей спит в сутки.
"""
X = int(input())
Y = int(input())
print(X*60 + Y)
"""

###Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его сна составляет XX минут. Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через XX минут после полуночи, однако для этого необходимо указать время сигнала в формате часы, минуты. Помогите Коле определить, на какое время завести будильник.
"""
X = int (input())
print (X // 60)
print (X % 60)
"""

###Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.
"""
X = int(input())
H = int(input())
M = int(input())
print((X+M)//60 + H)
print((X+M)%60)
"""

##1.9 Логические операции, операции сравнения

###??? Вывод логического выражения
"""
x = 5
y = 10
y > x * x or y >= 2 * x and x < y
print (result)
"""

##1.10 Условия: if, else, elif. Блоки, отупы

###Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки, но пересыпать тоже вредно и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.
"""
A = int (input ())
B = int (input ())
H = int (input ())
if A <= H <= B:
    print ('Это нормально')
elif H < A:
    print ('Недосып')
else:
    print ('Пересып')
"""

###Требуется определить, является ли данный год високосным.
"""
E = int(input())
if E%4==0 and E%100!=0 or E%400==0:
    print ('Високосный')
else:
    print ('Обычный')
"""

##1.11 Строки

##1.12 ЗАДАЧИ по материалам недели

###В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника, так как казалась слишком сложной.
# import math
"""
a = float(input())
b = float(input())
c = float(input())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
#S = math.sqrt(p*(p-a)*(p-b)*(p-c))
#print (p)
print (S)
"""

###Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (-15, 12] \cup (14, 17) \cup [19, +\infty)(−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

# *Подскажите,как создать полуинтервал в Python'е? Например, нужно вывести рандомные числа на промежутке [1,10),но при этом 10ти не включая???
# *->https://www.cyberforum.ru/python-beginners/thread2491262.html
"""
import random
a = random.randint(1, 9)
print(a)
"""
"""
x = int (input())
if -15<x<=12 or 14<x<17 or 19<=x:
    print(True)
else:
    print(False)
"""

###Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
"""
c1 = float(input())
c2 = float(input())
F = str(input())
if (F=="/" or F == "mod" or F == "div") and c2 == 0:
    print ("Деление на 0!")
elif F=="/":
    print (c1/c2)
elif F=="mod":
    print (c1%c2)
elif F=="div":
    print (c1//c2)
elif F=="+":
    print(c1+c2)
elif F=="-":
    print(c1-c2)
elif F=="*":
    print(c1*c2)
elif F=="pow":
    print(c1**c2)
else:
    print ("Пока не знаю")
"""
# *Вариант 2:
"""
a = float(input())
b = float(input())
act = input()

if (act=="/" or act=="mod" or act=="div") and b==0:
    c = "Деление на 0!"
elif act=="+":    c = a + b
elif act=="-":    c = a - b
elif act=="/":    c = a / b
elif act=="*":    c = a * b
elif act=="mod":  c = a % b
elif act=="pow":  c = a ** b
elif act=="div":  c = a // b

print (c)
"""
###Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты. Для числа π в стране Малевии используют значение 3.14.
# Площадь треугольника: S = √p(p - a)(p - b)(p - c), p = (a + b + c) / 2
# Площадь прямоугольника: S = a · b
# Площадь круга: S = π r2
"""
T = str(input())
if T == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif T == "прямоугольник":
    a = float(input())
    b = float(input())
    S = a * b
elif T == "круг":
    r = float(input())
    S = 3.14*r**2
print (S)
"""
# *Вариант 2:
"""
t = input()
if t == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    res = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif t == 'прямоугольник':
    res = float(input()) * float(input())
elif t == 'круг':
    res = 3.14 * float(input()) ** 2
else:
    res = 'Вы не истинный Малевиец!'
print(res)
"""
###Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
# *На ввод могут подаваться и повторяющиеся числа.
# -> Python Tернарный оператор - https://yandex.ru/search/?text=Python+%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%80%D0%BD%D1%8B%D0%B9+%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80&lr=21641&clid=2270457&win=401
"""
a, b, c = int(input()), int(input()), int(input())
max = a if a>=b and a>=c else b if b>=a and b>=c else c #if c>a and c>b
min = a if a<=b and a<=c else b if b<=a and b<=c else c
#print((a+b+c)-(max+min))
print (max, min,(a+b+c)-(max+min), sep="\n")
"""
# *Вариант 2 - "сортировка пузырьком" - Комет:
"""
Ivan Trechyokas
Если уйти от наивного подхода сравнить всё со всем, можно упростить логику следующим образом.

Формально этот алгоритм сортировки называется "сортировка пузырьком".
1 сортируем первые два элемента,
2 сортируем вторые два элемента,
3 восстанавливаем сортировку первых двух элементов.

a, b = b, a
- операция обмена значениями, аналогичная вводу третьей перемененой
c = a
a = b
b = c

Если стало интересно, то рекомендую два курса:
1 Алгоритмы: теория и практика. Методы - https://stepik.org/course/217
2 Алгоритмы: теория и практика. Структуры данных - https://stepik.org/course/1547
"""
# *Вариант 2 - "сортировка пузырьком" - Код:
"""
a = int(input())
b = int(input())
c = int(input())

if a <= b:
    a, b = b, a
if b <= c:
    b, c = c, b
if a <= b:
    a, b = b, a

print(a, c, b, sep='\n')
"""

# *Вариант 3 - Кратко как мог)
"""
x = [int(input()) for i in range(3)]
print(max(x),"\n", min(x),"\n", sum(x) - max(x) - min(x))
"""
###В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".
# ->https://stepik.org/lesson/5047/step/6?unit=1086
"""
# h->http://pythonmin.blogspot.com/2016/12/112-9-11.html
P = int(input())
if (P%100>=11 and P%100<=19) or (P%10==0 or P%10>=5 and P%10<=9):
    print(P," программистов")
elif P%10==2 or P%10==3 or P%10==4:
    print(P," программиста")
else:
    print(P," программист")
"""
###Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# ->https://stepik.org/lesson/5047/step/7?unit=1086
"""
n = input()
if int(n[0])+int(n[1])+int(n[2]) == int(n[3])+int(n[4])+int(n[5]):
#if int(n[0] + n[1] + n[2] == n[3] + n[4] + n[5]):
#if n[0] + n[1] + n[2] == n[3] + n[4] + n[5]:
    print("Счастливый")
else:
    print("Обычный")
"""
# *Вариант 2:
"""
a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')
"""
# *Вариант 3 - Без дополнительных функций, не забегая вперед - Где-то появилось солнце, Значит, где-то появилась тень. Мы сидели и делили (%, //), Начинался новый день.:
"""
a=int(input())
a1=a%10
a2=(a%100)//10
a3=(a%1000)//100
a4=(a%10000)//1000
a5=(a%100000)//10000
a6=a//100000
if a1+a2+a3==a4+a5+a6:
    print('Счастливый')
else:
    print('Обычный')
"""
"""
n=int(input())
print("Счастливый" if n//100000+n//10000%10+n//1000%10==n//100%10+n//10%10+n%10 else "Обычный")
"""
# *Вариант 4 - Такие дела
"""
a,b,c,d,e,f=(int(n) for n in input())
print(('Обычный','Счастливый')[a+b+c == d+e+f])
"""

# 2  Циклы. Строки. Списки

##2.1 Цикл while
# Цикл while
"""
a = 5
while a > 0:
    print(a, end=' ')
    a -= 1
"""
# Счетчик
"""
b = 10
a = 3
s = 0
i = a
while i<=b:
    s += i
    i += 1
print (s)
# ? Сломанный Счетчик
b = 10
s = 0
while s<=b:
    s += 1
print (s)
"""
###Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
"""
s = int(input())
i = s
while i != 0:
    i = int(input())
    s += i
print (s)
"""
# !? Переменную надо объявлять До цикла.. NameError: name 'a' is not defined:
"""
s = int(input())
i = s
while i != 0:
    i = int(input())
    a += i
print (a)
"""
# *Вариант 2:
""""
a = int(input())
s = 0
while a != 0 :
    s += a
    a = int(input())
print(s)
"""
"""
s, n =0, int(input())
while n:
    s, n = s + n, int(input())
print(s)
"""
# *Вариант 3 - Как пример того, что можно делать при использовании функций из sys.
"""
import sys
print(sum(int(x) for x in sys.stdin.readlines()))
"""
### В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов aa человек, а в команде информатиков — bb человек.
# ->https://stepik.org/lesson/3364/step/12?unit=947
"""
a = int(input())
b = int(input())
d = 1
while d%a!=0 or d%b!=0:
    d += 1
print (d)
"""
# *Вариант 2:
"""
a = int(input())
b = int(input())
d = a
while d%b:
    d += a
print(d)
"""
"""
a = int(input())
b = int(input())
d=a
while d%b!=0:
    d+=a
print(d)
"""
# *Вариант 3 - Решение в рамках пройденного материала и при этом без нерационального перебора с помощью +1.
# ->Находим большее из введенных чисел и прибавляем его к самому себе, пока это накопление не начнет делиться на меньшее.:
"""
a = int(input())
b = int(input())

if   a > b:
      p = a
      while p % b != 0: p += a

elif a < b:
      p = b
      while p % a != 0: p += b

else: p = a

print (p)
"""
##2.2 Операторы break, continue
"""
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break # досрочно завершаем цикл
    if (a == 0) or (b == 0):
        continue # переходим к следующей итерации
    print(a * b)
    i += 1
"""
##?Определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы:
"""
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
"""
## ? Определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы:
"""
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
"""
###Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# ->https://stepik.org/lesson/3365/step/4?unit=948
"""
i = int(input())
while i <= 100:
    if i>=10:
        print (i)
    i = int(input())
"""
# *Вариант 2:
"""
a = 0
while a <= 100:
    a = int(input())
    if 10 <= a <= 100:
        print(a)
"""
# *Вариант 3:
"""
while True:
    r = int(input())
    if r < 10: continue
    elif r > 100: break
    else: print(r)
"""
##2.3 Цикл for
# Вывести квадрат из звездочек
"""
n = int(input())
for i in range(n):
    print('*' * n)
"""
# 2 + end (?):
"""
n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
"""
# *Смотря на этот "квадратный" прямоугольник, перфекционист во мне негодует, если хотим всё таки квадрат, то лучше вот так
"""
n = int(input())
for i in range(n):
  print('* '*n)
"""
# **@Иван_Тихомиров
"""
n = int(input())
for i in range(n):
    print(' * ' * n)
"""
# ? Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# ->https://stepik.org/lesson/3366/step/3?unit=949
"""
#a, b, c, d = input() # <-здесь Ошибка
#a,b,c,d = (int(n) for n in input()) # <-здесь Ошибка

a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d+1):
    print('\t',i, end='')
print ()
for j in range (a, b+1):
    print (j, end='')
    for f in range (c, d+1):
        print('\t', j*f, end='')
    print()
"""
# *Вариант 2:
"""
# *?Как вставить '\t' перед циклом range?
# ->Ivan Trechyokas - Самый простой путь - сделать так:
print('\t', *range(c, d+1), sep='\t') # * - unpacking arguments list - https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists - _onenote:_документация Python_4.7.4. Unpacking Argument Lists
## --> чуть длиннее:
print('\t', end = '')
for i in range(c, d+1):
    print('\t', i, sep='', end='')
"""
# *Вариант 3 - Roman M - как-то так..):
"""
a, b, c, d = (int(input()) for x in range(4))
print('', *range(c,d+1), sep='\t')
for x in range(a, b+1):
    print(x, *[y*x for y in range(c, d+1)], sep='\t')
"""
# ->Ivan Trechyokas - Таблица умножение строится на сложении числа некоторого числа N раз, где N - номер столбца. /так правильнее:
"""
a=int(input())
b=int(input())
c=int(input())
d=int(input())

#print('\t', *range(c, d+1), sep='\t') #<-здесь Ошибка - '\t' = \t - лишняя
print('', *range(c, d+1), sep='\t') # * - unpacking arguments list - https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists - _onenote:_документация Python_4.7.4. Unpacking Argument Lists
for i in range(a,b+1):
    print(i, *range(i*c,(i*d)+1, i), sep='\t')
"""
# ? Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые делятся на 33.
# ->https://stepik.org/lesson/3366/step/7?unit=949
"""
a, b = (int(input()) for i in range(2))
s = 0
n = 0
for i in range (a, b+1):
    if i % 3 == 0:
        s += i
        n += 1
print(s/n)
"""
# *Вариант -
"""
a,b = int(input()), int(input())
a += -a%3
b -= b%3
print((a+b)/2)
"""
# *Вариант - как посмотрел на задачу и подумал, это все можно свести к красивой математической формулке. Что я собственно и сделал.
"""
print((((int(input())-1)//3)+1+int(input())//3)*1.5)
"""

# *Вариант - Это максимум  на базе изученного материала.
"""
a,b = (int(input()) for i in (1, 2))
print(((a+(3-a%3)%3)+b-(b%3))/2)
"""

# *Вариант - Как-то так...
"""
a, b = (int(input()) for _ in range(2))
print(((a+(3-a%3)%3)+b-(b%3))/2)
"""

##2.4 Строки и символы
# *Подсчет числа символов C в строке:
"""
genome = input()
cnt = 0
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print(cnt)
"""

# ? GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
# ->https://stepik.org/lesson/3367/step/3?unit=950
"""
genome = input()

s = len(genome)
a = genome.upper().count('G') + genome.upper().count('C')
p = a/s*100
print(p)
"""
# *Вариант 2:
"""
s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)
"""
# *Вариант - Это настоящая генетическая программа ) Она учитывает, что геном состоит только из 4-х оснований: a, g, c, t.
"""
gen = input().lower()
cg = gen.replace('a', '').replace('t', '')
print(100 * len(cg) / len(gen))
"""
# ? В поле ответа через пробел запишите строки (без кавычек), полученные в результате следующих операций:
"""
s = 'abcdefghijk'
#s[3:6]
#s[:6]
#s[3:]
#s[::-1]
#s[-3:]
#s[:-6]
print(s[-1:-10:-2])
"""

# ? Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
# ->https://stepik.org/lesson/3367/step/7?unit=950
"""
s = input()
i = 0
j = len(s)-1
while i<=j:
    k=i+1
    n = 1
    if k <= j:
        while s[i] == s[k]:
            k+=1
            n+=1
            if k > j:
                break
    print(s[i],n,sep='',end='')
#    print(s[i] + str(n), end='')
    i=k
"""
# *Вариант - Ivan Trechyokas - То действие, которые является особым, т.е. прекращается последовательность - можно обрабатывать в условии. А накручивать счётчик при прохождении символов - это "нормальное" поведение программы, поэтому его можно выполнять без дополнительных условных блоков.
"""
genome = input()+' '
s = 0
n=genome[0]
for i in genome:
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1
"""
# *Вариант - x
"""
dna = input()                    # считываем строку
print(dna[0],end='')             # выводим первый символ
cnt = 1                          # счетчик символов на единице
for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов кроме предпоследнего
    if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
        cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
    else :
        print(cnt,end='')        # если разные, то выводим значение счетчика
        print(dna[i+1],end='')   # выводим следующий символ
        cnt = 1                  # счетчик текущего символа на единице
print(cnt)                       # в конце распечатываем значение счетчика последнего символа
"""
##2.5 Списки

# ? Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
# *Используйте метод split строки.
"""
Li = [int(i) for i in input().split()]
sum = 0
for i in Li:
    sum+=i
print (sum)
"""
# *Вариант - С использованием generator expression.
"""
print(sum(int(i) for i in input().split()))
"""
# *Option - без sum. - @Дмитрий_Калинин, тот же sum(), только в "развернутом" виде -
# -> И смысл того, что ты изучал Списки, если не использовал их?:D Удивляют такие :)
"""
s = 0
for i in input().split():
    s += int(i)
print(s)
"""
# ? Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# ->https://stepik.org/lesson/3368/step/10?unit=951
"""
L = [int(i) for i in input().split()]
if len(L) == 1:
    print(L[0])
else:
    for i in range(len(L)):
        if i == len(L)-1:
            print(L[0]+L[len(L)-2], end='')
        else:
            print(L[i-1]+L[i+1],'', end='')
"""
# *Option - Как не обособлять случай последнего числа
# -> IGOR PAKIN - @Сергей_Долгих, красивое решение! ..если все правильно, для условия задачи, чтоб взлетело.., не хватает:
# , end=''
"""
a=[int(i) for i in input().split()]
if len(a)>1:
    for i in range(len(a)):
        print(a[i-1]+a[i+1-len(a)])
else:
    print(a[0])
"""
# *Option - для красивого лаконичного решения придётся вникать в list comprehension
"""
src = [int(i) for i in input().split()]
if len(src) == 1:
    print(src[0])
else:
    [print( src[i-1] + src[(i+1) % len(src)] ,end=' ') for i in range(len(src))]
    # выражение src[(i+1) % len(src)] на выходе для src = [1, 3, 5, 6, 10] даст [3, 5, 6, 10, 1]
    # потому, что (i+1) % len(src) даёт 1 2 3 4 0
    # т.е. таким образом 0й элемент оказывается в конце списка (как будто повернули циферблат)
    # таким образом если при обращении к i+1 случится выход за границу диапазона для последнего элемента
    # то при обращении к (i+1) % len(src) элементу выхода не произойдет
    # поэтому складывая -1й элемент с [(i+1) % len(src)]-тым элементом
    # мы выполним условие найти сумму предыдущего и следующего элементов
    # [print( src[(i+1) % len(src)]) for i in range(len(src))]
"""
# ? Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
# - Мой вариант - без создания второго списка:
"""
L = [int(i) for i in input().split()]
L.sort()
L.append('')
for i in range(len(L)):
    if L.count(L[i]) > 1:
        if L[i] != L[i+1]:
            print(L[i],'', end='')
        else:
            continue
"""
# *Option - Помещаю в новый список текущее число, если его там ещё нет И если в исходном списке таких чисел несколько
"""
a, b = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")
"""
# *Option - все просто )) - !+ set()
"""
ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')
"""
# *Option - мне кажется красивое решение и не должно быть очень ресурсоемким = +.sort
"""
a,b=[int(i) for i in input().split()],''
a.sort()
for i in range(len(a)-1):
    if a[i]==a[i+1] and a[i]!=b:
        print(a[i], end=' ')
        b=a[i]
"""
# *Option - Ivan Trechyokas - Немного уличной магии. +.splot
"""
str = [int(i) for i in input().split()]
ans = []
[ans.append(x) for x in str if x not in ans and str.count(x) > 1]
print(*ans)
"""
##2.6 ЗАДАЧИ по материалам недели
# ? Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# -> https://stepik.org/lesson/3369/step/7?unit=952
"""
C = int(input())
S = C
ans = []
ans.append(C)
while S != 0:
    C = int(input())
    ans.append(C)
    S+=C
for i in ans:
    S += i*i
print(S)
"""
# *Option - Генераторы списка - правильная вещь +! sam()
"""
s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))
"""
"""
c=[int(input())]
while sum(c) != 0:
    c.append(int(input()))
print(sum(i**2 for i in c))
"""
# *Option - и снова !!? list comprehension позволил сократить код
"""
lst = [int(input())]
while sum(lst) != 0:
    lst.append(int(input()))
print(sum( el * el for el in lst))
"""
# *Option - !!! Без Списка - C помощью цикла while суммируем квадраты введенных значений и накапливаем его. Первое значение суммы, задал до цикла вводом первого значения.
"""
s = int(input())
ss = s ** 2
while s != 0:
    a = int(input())
    s += a
    ss += a ** 2
print(ss)
"""
# ? Напишите программу, которая выводит часть последовательности
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
# На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# -> https://stepik.org/lesson/3369/step/8?unit=952

# - Мой - со списком, по теме раздела + ! не забываем ставить break, чтоб цикл не молотил лишнего в пустую
"""
n = int(input())
L = []
for i in range(1, n+1):
    while len(L) < n and L.count(i) < i: L.append(i)
    if len(L) == n : break
for x in L : print (x, str(''), end='')
"""
# *Option - Хочу поделиться интересным решением задачи вывода элементов ﻿списка через любой символ (см. последнюю строчку моего ﻿кода). По умолчанию выводится через пробел, но можно использовать параметр sep.
# Примечательно, что это решение работает из коробки  как для строковых, так и для числовых списков (в отличии от метода .join)
# -> Решение было найдено здесь: http://stackoverflow.com/questions/22556449/print-a-list-of-space-separated-elements-in-python-3
"""
n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])
"""
# *Option - ээ.. без списка
"""
a = int(input())
c = 0
for i in range(a+1):
    for j in range(i):
        c += 1
        if c<a+1:
            print(i, end=' ')
"""
# Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
"""
lst = [int(i) for i in input().split()]
x = int(input())
if lst.count(x) == 0 : print('Отсутствует')
else:
    a = []
    for n in range(len(lst)):
        if lst[n] == x:
            a.append(n)
    a.sort()
#    print(*a[:n])
    for m in a: print(m, str(''), end='')
"""
# *Option - Как же мне нравится писать на питон, просто музыка.
# @Виктор, индексы уже по порядку идут. Их сортировать не нужно.
# @Sergey_Nikiforov, однако даже если значения x не будет в списке l, программа все равно зачем-то сделает прогон по списку. Стоила ли того сэкономленная строка кода?
# так лучшее будет:
"""
l = [int(i) for i in input().split()]
x = int(input())
if not x in l: print('Отсутствует')
else:
    for i in range(len(l)):
        if l[i]==x: print(i, end = ' ')
"""
# ? НЕ ЗАЧАРЖЕНА! Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
# ->https://stepik.org/lesson/3369/step/10?unit=952
"""
a = [[], [], [], []]
#   Видео - Видео: 29 Вложенные списки Python - https://www.youtube.com/watch?v=0qtLrRm36J0&t=6s
"""

# 3  Функции. Словари. Интерпретатор. Файлы. Модули.

## 3.1 Функции

# ? Есть функция f, которая определена следующим образом:
# Введите её в интерпретаторе и посчитайте, чему равно значение следующего выражения: f(f(f(10)))
"""
def f(n):
    return n * 10 + 5
print(f(f(f(10))))
"""
# ?Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
"""
def f(x):
    if x <= -2:
        y = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        y = -(x / 2)
    elif 2 < x:
        y = (x - 2) ** 2 + 1
    return y
print(f(float(input())))
# x = f(-4.5)
# print(x)
"""
# * Option - :)
"""
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif x <= 2:
        return -x / 2
    else:
        return (x - 2) ** 2 + 1
"""
# Option - Такого варианта ещё не было.
"""
def f(x):
    if x <= -2:
        return 1 - (x+2)**2
    if x <= 2:
        return -x/2
    return (x-2)**2 + 1
"""

# НЕ ЗАЧАРЖЕНО! ? Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
# -> https://stepik.org/lesson/3372/step/9?unit=955

# 1
"""
def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] = l[i] / 2
        else:
            l.pop(i)
    return l
print(modify_list([float(i) for i in input().split()]))
"""
# 2
"""
def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 != 0:
            l.pop(i)
        else:
            l[i] = l[i] / 2
    return l
print(modify_list([float(i) for i in input().split()]))
"""

##3.2 Словари

# ? Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

"""
#    for key in d: #пример перебора по ключу без использования специальной функции.. это возможно только для ключа, перебор по значению или паре ключь-значение возможен только по специальным функциям
#    for key in d.keys(): #перебор по ключу через функцию
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    else:
        if 2*key in d:
            d[2*key] += [value]
        else:
            d[2*key] = [value]
"""
# *Option - True -> 1 | False -> 0
"""
def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]
"""
# *Option - Чётко по инструкции
"""
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif 2*key in d.keys():
        d[2*key].append(value)
    else:
        d[2*key]=[value]
"""
# *Optoin - Просто и читаемо
"""
def update_dictionary(d, key, value):
    if key not in d:
        key = 2 * key
    if key not in d:
        d[key] = list()
    d[key].append(value)
"""
# **Option - заменил ветку if на битовый сдвиг
"""
def update_dictionary(d, key, value):
    key <<= key not in d
    d.setdefault(key,[]).append(value)
"""

# ? Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# -> https://stepik.org/lesson/3373/step/6?unit=956
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
"""
lst = [i for i in input().lower().split()]
dct = {}
for x in lst:
    if x in dct:
        dct[x] += 1
    else:
        dct[x] = 1
for key, value in dct.items():
    print(key, value)
"""
# *Option - @Ирина_Пронина Решение компактнее, чем через словарь, но если посмотреть на время выполнения, то уже на данных от 20-25 слов суммарно получается медленее выполнение. Из-за того, что вот так count считать всё время по большому массиву - очень невыгодно. http://take.ms/YeHE3﻿ - тут пример.
# -> Хотя может не всё так однозначно, есть значения для которых сет быстрее
"""
lst = input().lower().split()
#print(set(s))
for i in set(s):
    print(i, lst.count(i))
"""
# **Option - @Ирина_Автомонова,   красиво у вас получилось. Предлагаю вот так записать.
"""
s = input().lower().split()
[print(i, s.count(i)) for i in set(s)]
"""
# ?
# - T3 - СКИПАНУЛ здесь хакнул комент - Oleh Biletskyi 7 months ago Link ->
# -> https://stepik.org/lesson/3373/step/7?unit=956
"""
dc={}
n=int(input())
for i in range(n):
    x=int(input())
    if x in dc:
        print(dc[x])
    else:
        dc[x]=f(x)
        print(dc[x])
"""
# + Для проверки времени исполнения кода:
## Блин, это гениальное задание. Заставило задуматься о том, что более длинный код может выполняться быстрее, чем короткий. Т.е. нас подводят к оптимизации кода.
"""
import time
start_time = time.clock()

# Ваш код...

print ("{:g} s".format(time.clock() - start_time))
"""

##3.3 Интерпретатор: установка, запуск скрипта

##3.4 Файловый ввод/вывод

# ? На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
# -> https://stepik.org/lesson/3363/step/2?unit=1135

# 1: Читаем строку из файла, с относительным путем без зависимости от OS
"""
import os
with open(os.path.join('.', 'week_3_dataset', 'Т_3.4_1', 'dataset_3363_2 (2).txt')) as inf:
    s1 = inf.readline()

# 2: Декодируем строку
number='0123456789'
n = ''
souf = ''
for i in range(len(s1)-1, -1, -1):
    if s1[i] in number:
        n = s1[i]+n
    else:
        souf = s1[i]*int(n) + souf
        n = ''
"""
# ? Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
# -> https://stepik.org/lesson/3363/step/3?unit=1135

# 1: Читаем строку из файла, с относительным путем без зависимости от OS
"""
import os
with open(os.path.join('.', 'week_3_dataset', 'T_3.4_2', 'dataset_3363_3 (2).txt')) as text:
    s = sorted(text.read().replace('\n', ' ').lower().split())
#    print (s)

c1 = 0
c = 0
w = ''
for v in s:
    c = s.count(v)
    if c > c1:
        c1 = c
        w = v
print (w, c1)
"""
# ? Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# -> https://stepik.org/lesson/3363/step/4?unit=1135
# Можно сделать более универсальным — количество оценок может быть любое:
# ->
"""
import os
with open(os.path.join('.', 'week_3_dataset', 'T_3.4_3', 'dataset_3363_4 (2).txt')) as dat:
    for data in dat:
        data = data.strip()
#        print(line)

data = """

"""

students = list()

for line in data.split('\n'):
    line = line.strip()
    if not line:
        continue

    parts = line.split(';')
    name = parts[0]
    rating = list(map(int, parts[1:]))
    mean = sum(rating) / len(rating)

    students.append(
        (name, rating, mean)
    )

for st in students:
    print('{}: {:.2f}'.format(st[0], st[-1]))

print()

# Количество оценок определяем по количеству оценок последнего студента
for i in range(len(rating)):
    p = [s[1][i] for s in students]
    print(sum(p) / len(p))
"""
# * 1: без оптимизанции
data = """

"""
"""
students = list()

for line in data.split('\n'):
    line = line.strip()
    if not line:
        continue

    parts = line.split(';')
    name = parts[0]

    # Получаем список от второго элемента до последнего,
    # и приводим каждый элемент к числу
    rating = list(map(int, parts[1:]))
    mean = sum(rating) / len(rating)

    info = list()
    info.append(name)
    info.extend(rating)
    info.append(mean)

    students.append(info)

# Выводим имя студента и его среднюю оценку по предметам (последний элемент)
for st in students:
#    print('{}: {:.2f}'.format(st[0], st[-1]))
    print(st[-1])

print()
# По списку студентов составляет списки с оценками по каждому предмету
p1 = [st[1] for st in students]
p2 = [st[2] for st in students]
p3 = [st[3] for st in students]

print(sum(p1) / len(p1))
print(sum(p2) / len(p2))
print(sum(p3) / len(p3))
"""
##3.5 Модули, подключение модулей
# ? Напишите программу, которая подключает модуль math и, используя значение числа \piπ из этого модуля, находит для переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.
"""
import math
from math import pi
r = float(input())
print(2*pi*r)
"""
# ? Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
"""
import sys
l = len(sys.argv)
for i in range(1, l):
    print(sys.argv[i])
"""
# Option - 2
"""
import sys
print(*sys.argv[1:])
"""
##3.6 Установка дополнительных модулей

##3.7 ЗАДАЧИ по материалам недели

##3.8 Библиотеки для анализа данных. NumPy

##3.9 Библиотека Matplotlib

##3.10 Заключение
