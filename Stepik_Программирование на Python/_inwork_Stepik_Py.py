"""
import webbrowser
webbrowser.open("https://stepik.org/course/67")

# ->*https://fooobar.com/questions/8105644/how-to-insert-links-in-python
"""
"""
> Визуализатор - http://pythontutor.com/visualize.html - позволяет пошагово показывать работу вашей программы, что крайне полезно
"""

#1. Операторы. Переменные. Типы данных. Условия

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
#import math
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

#*Подскажите,как создать полуинтервал в Python'е? Например, нужно вывести рандомные числа на промежутке [1,10),но при этом 10ти не включая???
#*->https://www.cyberforum.ru/python-beginners/thread2491262.html
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
#Площадь треугольника: S = √p(p - a)(p - b)(p - c), p = (a + b + c) / 2
#Площадь прямоугольника: S = a · b
#Площадь круга: S = π r2
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
#*На ввод могут подаваться и повторяющиеся числа.
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

#2  Циклы. Строки. Списки

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
##?Определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы:
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
a = 0
"""
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
# ?Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# ->https://stepik.org/lesson/3366/step/3?unit=949
a, b, c, d = input()
#n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()

##2.4 Строки и символы

##2.5 Списки

##2.6 ЗАДАЧИ по материалам недели

#3  Функции. Словари. Интерпретатор. Файлы. Модули.

## 3.1 Функции

##3.2 Словари

##3.3 Интерпретатор: установка, запуск скрипта

##3.4 Файловый ввод/вывод

##3.5 Модули, подключение модулей

##3.6 Установка дополнительных модулей

##3.7 ЗАДАЧИ по материалам недели

##3.8 Библиотеки для анализа данных. NumPy

##3.9 Библиотека Matplotlib

##3.10 Заключение
