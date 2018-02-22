# Кортежи_tuples / кортежи это по сути теже списки только картежи в отличии от списков нельзя изменять после сзодания
# Защита от дурака. То есть кортеж защищен от изменений, как намеренных (что плохо), так и случайных (что хорошо).

# Создаем пустой кортеж:

a = () # пустой кортеж

a = tuple() # С помощью встроенной функции tuple()
print (a) # ()

# простой пример: Создаем кортеж из одного элемента:
a = ('s')
print (a) # s

# Как же нам кортеж получить?
a = ('s', ) # a = 's' можно напиать и так , тоесть запятая решает будет ли s в составе кортежа
print (a) # a = ('s', )

#
a = tuple('hello, world!') # С помощью встроенной функции tuple() делим строку на каждый отдельный символ
print (a) # ('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')

#
a = ("Hello world", "sdf", 345)
print (a)
print (a.count (345)) # совмещение функции для срок count . нам показывает что в этом кореже толко 1 элимент = 345


a = (23, 'rt', 34, 56.67, 0)
b = [23, 'rt', 34, 56.67, 0]

a = [455]

print (a.__sizeof__()) # показывает рамзер кортежа в байтах здесь 64 байта (Кортеж весит меньше)
print (b.__sizeof__()) # показывает рамзер списка в байтах здесь 80 байт


# Например, гордость программистов на python - поменять местами значения двух переменных:

a, b = b, a
print (a,b)



#________________________________________________________________
# Возможность использовать кортежи в качестве ключей словаря:



#________________________________________________________________


#________________________________________________________________