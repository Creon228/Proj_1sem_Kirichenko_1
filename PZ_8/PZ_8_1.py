#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти среднее значение продаж по
#каждому виду продукции, результаты вывести на экран.
#Вариант 8


def average(key, summa=0):   #функция подсчета среднего арифметического
    for number in dictionary.get(key):
        summa += int(number)
    return summa / 5


stroka = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 16" #исходные данные
pravka = list(stroka.split()) #преобразование строки в словарь
dictionary = {}

keys_list = []
index_keys = []
for i in pravka: #создание ключей словаря
    if i.isalpha():
        keys_list.append(i)
        index_keys.append(pravka.index(i))


for i in index_keys: #добавление значений в словарь
    if int(i) >= len(index_keys):
        dictionary.update({keys_list[index_keys.index(i)]: pravka[i+1:]})
    else:
        dictionary.update({keys_list[i] : pravka[int(i)+1:index_keys[index_keys.index(i)+1]]})




print(f"Яблоки - {average('яблоки')}, апельсины - {average('апельсины')}") #вывод конечных результатов

