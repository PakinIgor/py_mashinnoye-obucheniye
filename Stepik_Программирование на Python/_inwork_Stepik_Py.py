"""
*https://fooobar.com/questions/8105644/how-to-insert-links-in-python

Одно из предложений заключается в использовании модуля python webbrowser для открытия ссылок:

import webbrowser
webbrowser.open("http://www.example.com")
который откроет вам ссылку в новом окне.

Вы также можете вывести текст в файл HTML и открыть файл HTML в веб-браузере для ссылки:

open("link.html", "w").write('<a href="http://www.example.com"> Link </a>')
"""
"""
import webbrowser
webbrowser.open("https://stepik.org/course/67")
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

# ##В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника, так как казалась слишком сложной.
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
c1 = float(input())
c2 = float(input())
F = str(input())
if F=="/" or F == "mod" or F == "div" and c2 == 0:
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
"""
else:
    print ("Пока не знаю")
"""


#2  Циклы. Строки. Списки

##2.1 Цикл while

##2.2 Операторы break, continue

##2.3 Цикл for

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
