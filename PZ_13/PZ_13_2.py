#Вариант 8
#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def uppercase_generator(spisok): #функция переводит каждую букву строки в верхний регистр
    for i in spisok:
        i = i.upper()
        yield i

fraza = input('Введите фразу ') #ввод данных
fraza = list(fraza.split()) #переводим строку в список из символов
result = []
generator = uppercase_generator(fraza)

for k in generator: #заносим результаты в список с результатом
    result.append(k)

print(result) #выводим результат
