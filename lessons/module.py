# в самом модуле прописывам некоторые функции , которые ы сможемдльше иползовать в нашей программе:

# интересно то что мы можем даже просто написать: print "Hello World" и при вызове данного модуля в программе
# нам будет выведена строка "Hello World" , данная строка
# будет выведена в самом начале при вызове нашего моделя , поэтому если есть готовый код для модуля
# нужно изначально делать проверку:
                            # По этому если в наше файл ст каой то код и вы не хотите чтобы он сразу
                            # срабатывал при импортировании в другом файле то нужно прописвать проверки:

                             # данная строка предназначена для проверки  того где в первую очередь должен срабоать
                             # код модуля  если мы в командной строке вызовем наш файл module то нам выдас
                             # строку "Hello World"

def hi (): # первая функция
    print ("Hello")

def add (x, y): # вторая функция
    return x + y

if __name__ == "__main__":
    print ("Hello World")
                             # данная строка предназначена для проверки  того где в первую очередь должен срабоать
                             # код модуля  если мы в командной строке вызовем наш файл module то нам выдаст
                             # строку "Hello World"