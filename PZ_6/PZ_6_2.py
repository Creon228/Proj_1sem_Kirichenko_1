#Дан список размера N. Найти количество участков, на которых его элементы
#монотонно возрастают.
#Вариант 8

from random import randint

n = int(input('Введите n: ')) #ввод исходных данных
my_list = [randint(-100, 100) for i in range(n)] #создание списка случаных числе с размером n
print(my_list)
buff = ''
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]: #сравнение числе в списке
        buff += '+'
    elif my_list[i] < my_list[i-1]:
        buff += '-'
k = 0
for el in buff.split('-'): #нахождение монотонно возрастающих участков
    if '+' in el:
        k += 1
print(k)
