#Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
#этого элемента и его соседей.
#Вариант 8

from random import randint

n = int(input('Введите n: ')) #ввод исходных данных
my_list = [randint(-100, 100) for i in range(n)] #создание списка с случайными числами размером n
my_list_copy = my_list.copy() #клонирование списка
for i in range(len(my_list)):
    if i == 0:
        my_list_copy[i] = (my_list[i] + my_list[i + 1]) / 2
    elif i == len(my_list) - 1:
        my_list_copy[i] = (my_list[i-1] + my_list[i]) / 2        #нахождение среднего арифметического
    else:
        my_list_copy[i] = (my_list[i-1] + my_list[i] + my_list[i+1]) / 3
print(my_list) #вывод конечных данных
print(my_list_copy)
