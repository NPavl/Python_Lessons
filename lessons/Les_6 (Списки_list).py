# Списки - в питон это по сути массивы , толко своеобразные , в данные спики вы можете помстить много разных значений
# к примеру в переменной вы можете хранить какое то одно значение , в списках наоборт много разных значений
# приер списка:
l = [] # пустой списко здесь ничего нет

lis = [1, 56, 'x', 34, 2.45, ['s', 't', 'r', 'o', 'k', 'a']] # приер списка с разными
print (lis)

a = [a + b for a in 'list' if a != 's' for b in 'soap' if b != 'u']
print (a)
# из этого примеры мы видем что у нас есть список - а , a+b это строки которые мы будем совмещать a - list и b - soap
# мы берем 1 буквочку с одного слова и 1 букву со второго слова к пример ls , lo , la ...тд, все это проходим через цикл
# мы берем a  в строке list (мы берем каждую букву кроме буквы s) все остальные буквы мы соединяем ['ls', 'lo',
# 'la', 'lp', 'is', 'io', 'ia', 'ip', 'ts', 'to', 'ta', 'tp'] пербираем все кроме буквы u.
# Все это очень похоже на двумерный статич массив в С , тоест мы зходим в первый цикл list берем его первое значение
# и перебираем все цикле soap побуквенно . + имем какиетто дополнителные условия по списку - a
#__________________________________________________________________
# Примеры функций для списков: их существуют дастаточно много :
# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
# https://www.ibm.com/developerworks/ru/library/l-python_part_3/index.html

# некоторые примеры:

l = []
l.append (23) # к переменной l (список) мы добавляем функцию append (она добавляет элимент в конец этого списка)
l.append (34)
print (l) # [23, 34] добавил два новых значения

b = [24, 67]
l.extend (b) # здесь мы расширяем наш списко l списком b .
# extend - фунция которая позволяет нам расширить список, добавяляя в его конец все элимиенты списка
# (которые мы передаем в качестве аргументов) .
print (l) # [23, 34, 24, 67]

l.insert (3, 44) # функция которая позволяет вставить элимент по индексу (индекс это номер элимента в списке)
print (l) # [23, 34, 24, 44, 67] мы видим как в наш предыдущий список доавлено новое значение 44 . (3, 44)
# 3 - это номер индекса списка а 44 это новое значение под этим индексом

l.remove (34) # удаляем из списка значение 34; # эта функция удаляет имющее значение коорое мы передаем
# в качестве аргумента в данную функцию (если там ничего не находится (в аргументах) то компилятор нам выдаст error)
print (l) # как видим 34 пропала

l.pop (0) # данная функция удаляет последний элимент в списке если там нет ничего в качестве аргументов ,
# для того что бы удалить конкетны элиент из списка нужно указать его номер индекса, в данном примере мы удалили
# первый элимент из списка под индексом 0.
print (l) # результат [24, 44, 67] значение 23 отсут

print (l.index (24)) # данная функция возвращает индекс какого либо элимента в списке , к примеру мы хотим найти номер индекса
# какого то элимента к примеру индекс значения 24 / нам показываает 0 (номер индекса в списке)

print (l.count (24)) # функция которая возвращает количество элиментов в списке. нам показывает 1.
# данную функцию можно записать еще последовательно, вот так :
print(l.count(24), l.count(44), l.count('x'))
print (l) # 1 1 0  (так как x у нас нет выводится последняя цифра 0)
# доп пример : a = [66.25, 333, 333, 1, 1234.5]
# print (a.count(333), a.count (66.25), a.count('x')) 2 1 0 (так как значение 333 у нас 2 то и вывод соот-ный 2 1 0)
l.sort () # данная функция сортирует список по возрастанию
print (l) # на выводе данный функции мы видим что наш списко отсортирован по возрастанию [24, 44, 67]

l.reverse () # а эта функия наоборот перворачивает наш список, (не путай ! она не выстраивает элиенты по убыванию)
# а толко перворачивает его , пример вывода снизу:
print (l) # [67, 44, 24]

l.clear() # функция которая очищает весь список
print (l) # соот-но выводится пустой список []

#__________________________________________________________________

