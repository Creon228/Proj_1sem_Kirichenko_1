#Вариант 8
#В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.

def umnozenie(b):
    for i in range(0,len(matriza)): #перебираем элементы матрицы
        matriza[n-1][i] = matriza[n-1][i] * 3 #умножаем каждый элемент на 2
    return matriza

matriza = [[2,5,7], #задаем матрицу
           [4,7,9],
           [1,2,0]]

n = int(input("Введтие номер столбца ")) #ввод данных
print(umnozenie(n)) #вывод конечного результата
print('Не забывай выходить с GitHub. Файлы потерять можешь.')
