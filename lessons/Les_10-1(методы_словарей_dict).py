# Методы словарей: https://itproger.com/course/python/10
# Рассмотрим разные методы словарей :

# dict.clear() - # очищает словарь

# Связываем страны со столицами
asia = {
    'Azerbaijan': 'Baku',
    'Armenia': 'Yerevan',
    'Afghanistan': 'Kabul'
    }
# Связываем столицы с данными о населении
population = {
    'Baku': 2137000,
    'Yerevan': 1060000,
    'Kabul': 3000000
    }

print('=' * 5)
population.clear()
print(population) # {}

#__________________________________
#Новый метод:
# .copy - создание копии словаря
# dict.copy()

print('=' * 5)
countriesofasia = asia.copy()
print(asia) # {'Azerbaijan': 'Baku', 'Armenia': 'Yerevan', 'Afghanistan': 'Kabul'}
print(countriesofasia) # {'Azerbaijan': 'Baku', 'Armenia': 'Yerevan', 'Afghanistan': 'Kabul'}

#__________________________________
#Новый метод:
# .keys - извлечение только ключей из словаря
# dict.keys()
print('=' * 5)
print(asia.keys()) # dict_keys(['Azerbaijan', 'Armenia', 'Afghanistan'])

asiaclone = asia.keys()
print(asiaclone)   # dict_keys(['Azerbaijan', 'Armenia', 'Afghanistan'])

#___________________________________
#Новый метод:
# .values - извлечение только значений из словаря
# dict.values()
print('=' * 5)
print(asia.values()) # dict_values(['Baku', 'Yerevan', 'Kabul'])

asiavalues = asia.values()
print(asiavalues)  # dict_values(['Baku', 'Yerevan', 'Kabul'])

#____________________________________
#Новый метод:
# .get - извлечение пар ключ-знаение, возможность выполнения действий в случае, если пары ключ-значение отсутствуют

print('=' * 5)
countryone = asia.get('Azerbaijan') # Baku
print(countryone)

countryone = asia.get('Tokyo')
print(countryone)  # None

# Использование метода .get с оператором 'if'

print( '=' * 5)
country = asia.get('Armenia')

# Условие на случай, если такой страны в словаре нет:
if not country:
    print( "Sorry, no info about this country.")

if country:
    print(country) # Yerevan

#____________________________________

#Добавляем списки в качестве значений - такое решение не всегда идеально
# dict = {'key': [value, value, value], 'key2': [value, value, value]}
print('=' * 5)
citiesoffrance = {'city': ['Paris', 'Marseille', 'Lyon'], 'population': ['3M', '2M', '1M']}
print(citiesoffrance)

#или
print(citiesoffrance['city'][0])
print(citiesoffrance['population'][0])

#или
print('=' * 5)
print(citiesoffrance['city'][0], citiesoffrance['population'][0])

#____________________________________

# А вот почему включать списки в словари это не всегда хорошая мысль.
print( '=' * 5)
for city, population in citiesoffrance.items():
    print( "%s has the population of %s" % (city, population))  # Paris 3M



# Такое решение было бы куда лучше
citiesoffrance = {'Paris': '3M', 'Marseille': '2M', 'Lyon':'1M'}
for city, population in citiesoffrance.items():
    print( "%s has the population of %s" % (city, population))  # city has the population of ['Paris', 'Marseille', 'Lyon']
#population has the population of ['3M', '2M', '1M']
#Paris has the population of 3M
#Marseille has the population of 2M
#Lyon has the population of 1M



#____________________________________
