# Множества (set и frozenset)   https://itproger.com/course/python/11
# Множества также схожи с массивами, но есть несколько отличий.
# Во-первых, множества создаются в абсолютно случайном порядке каждый раз.
# Вы можете разместить элементы как вам будет угодно, но они все равно будут
# расположены впоследствии в случайном порядке. Во-вторых, множества не могут
# иметь повторяющихся элементов, поэтому все элементы, которые будут одинаковыми
# не будут выведены повторно.

# с множетвами монжно проделать очень много полезных функций и операций,
# к примеру мы можем проверить одно множетво на соот-вие другому какому то списку кортежу и т д
# как можно создать множество:

a = set () # в множестве нет повторябщихся элиментов
print (type(a)) # <class 'set'>
# print (a)


a = set ("hello") # создали множество
print (type(a)) # <class 'set'>
print (a) # {'h', 'l', 'o', 'e'} значения меняются на каждой компиляции {'o', 'l', 'h', 'e'} ....

a = {'23', 32} # дугой пример создания множества
print (type(a)) # <class 'set'>
print (a) # {32, '23'}

a = {i ** 2 for i in range (10)} # в этом множестве 10 элиментов в рандомной последоваелности
print (type(a)) # <class 'set'>
print (a) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# в множетвах есть функция frozenset () здесь примерно тоже само что и в кортежах мы не можем изменять  :

a = set ("hello")
frozenset ("qwerty")
a.add (1) # фунция коорая добавляет некий элимент в множество
print (a) # {1, 'h', 'o', 'l', 'e'} и так {1, 'o', 'e', 'h', 'l'} ......


a = ['r', 's', 'w', 'a', 's', 'w']
print (a) # ['r', 's', 'w', 'a', 's', 'w'] в певом случае это обчынй список
print (set (a)) # {'a', 's', 'w', 'r'} а во втором это уже множество

a = {32, 45, 43.12, 76}
x = 45
print (len (a)) # 4 , данная функция выводит количство элименов в нашем множестве
print (x in a) #  True,  данная функция показывает нам есть ли число x в множетве а (как видим true)



a = {32, 45, 43.12, 76}
x = {67, 12, 90}
print (a.isdisjoint(x)) # True. данная функция буде возвращать true если a и x не имеет общих
                        # элиментов, если есть соот-вие тогда false

a = {32, 45, 43.12, 76}
x = {67, 12, 90}
print (a == x) # здесь смысл такой тчо ели все элименты множества будут совпадать в a и x тогда true , наоборо false

a = {32, 45, 43.12, 76}
x = {45, 43.12, 76, 32}
print (a == x) # True  здесь уже true


a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 32, 334}
a.update (x) # данная функция обьединяет несколко множеств  (здесь наше в множесво а из множества x
             # добавяться значения которыx нет в а)
print (a) #  {32, 43.12, 76, 45, 334, 56} тд добавили  334, 56


a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 32, 334}
a.intersection_update (x) # это функция пересечение (дискретная математика) числа которые есть и в одном
                          # множетве и в другом множестве
print (a) # {32, 43.12, 45}


a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 23}
a.difference_update (x) # {32, 76} # это тоже пересечение множеств
print (a) # {32, 76} здесь те циры которые есть в а но нету в x


a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 23}
a.symmetric_difference_update (x) # это функция множеств из элиментов встречающихся в одном множестве но не
                                  # встречающихся в обоих
print (a) # {32, 76, 23, 56}  32 и 76 есть в а но нет в x , в x есть 23, 56 но таких числе нет в а.




a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 23}
a.remove (32) # функция которая удаляет некий элимент из множества
print (a) # {43.12, 76, 45} самое инетересное что значения после компиляции меняются местами

a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 23}
a.discard (32) # функция которая даляет элимент если он находиться в множестве , по ути почти тоже самое
               # что и функция remove (только remove выдаст ошибку ели такого элимента нет , discard же ничего не выдаст
               # если такого элимента не будет во множестве
print (a) #   {43.12, 76, 45}


a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 23}
a.pop (32) # эта функция опять таки удалет элимент но она удалет первый элиент из множества , благодаря тому что
           # то мы не знаем какой буде певый элиент (ак как они располагаються в случайном порядке)

print (a) #


a = {32, 45, 43.12, 76}
x = {45, 43.12, 56, 23}
a.clear () # функция которая очищает наше множетсво от всех элиентов
print (a)  #