#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Индекс последнего минимального элемента:
#Сумма элементов больших 10 во второй половине:



posledovatelnost = [1, 2, -3, 4, 5, -1, 6, 11, -10, -15] #создаем последовательность чисел



f = open('text.txt', 'w', encoding='UTF-8') # создаем и открываем файл для записи
f.writelines(f'Исходные данные:  {str(posledovatelnost)}\n') # записываем последовательность
f.writelines(f'Количество элеметов: {len(posledovatelnost)}\n') #записываем длинну последовательности
f.writelines(f'Индекс последнего минимального элемента: {min((x, -i) for i, x in enumerate(posledovatelnost))[1]}\n') #записываем индекс последнего минимального элемента последовательности
summa = 0
polovina = int(len(posledovatelnost) / 2) #считаем сумму элементов больше 10 во второй половине последовательности
for i in posledovatelnost[polovina:]:
    if i > 10:
        summa += i
f.writelines(f'Сумма элементов больших 10 во второй половине: {summa}\n')
f.close()