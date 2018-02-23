# примеры применение sizeof в питоне
# http://qaru.site/questions/2916/how-do-i-determine-the-size-of-an-object-in-python
# Как определить размер объекта в Python?



# используйте функцию sys.getsizeof, определенную в модуле sys.

# sys.getsizeof(object[, default]):

# Возвращает размер объекта в байтах. Объектом может быть любой тип объекта.
# Все встроенные объекты вернутся правильные результаты, но это не должны быть
# справедливыми для сторонних расширений, поскольку это реализация специфичны.

# Аргумент default позволяет определить значение, которое будет возвращено,
# если тип объекта не предоставляет средства для получить размер и вызвать TypeError.

# getsizeof вызывает объекты __sizeof__ и добавляет дополнительные служебные данные
# сборщика мусора если объект управляется сборщик мусора.

# Пример использования в python 3.0:

import sys  

x = 2
sys.getsizeof(x) # 14
print(sys.getsizeof(x)) # 28

sys.getsizeof(sys.getsizeof) # 32
print(sys.getsizeof(sys.getsizeof)) # 72

sys.getsizeof('this')  # 38
print(sys.getsizeof('this')) # 53

sys.getsizeof('this also') # 48
print(sys.getsizeof('this also')) # 58