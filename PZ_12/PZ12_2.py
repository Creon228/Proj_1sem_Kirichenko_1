#Вариант8

from tkinter import *
from tkinter import messagebox
from random import randint


def button_clicked(event):
    s = ent1.get()
    s = int(s)
    my_list = [randint(-100, 100) for i in range(s)]  # создание списка случаных числе с размером s
    buff = ''
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i - 1]:  # сравнение числе в списке
            buff += '+'
        elif my_list[i] < my_list[i - 1]:
            buff += '-'
    k = 0
    for el in buff.split('-'):  # нахождение монотонно возрастающих участков
        if '+' in el:
            k += 1
    messagebox.showinfo("result", f"Ответ: {k}") #вывод результата в messagebox



root = Tk() #создание главного окна
root.title("PZ6_2")
root.geometry('400x300')
root.configure(bg='#74BDCB')
root.resizable(height="false", width="false")

lb1 = Label(root, text="Введите N", fg="white", bg="#74BDCB", pady=10, width=100, font=('Arial', '16', 'bold'), #добавление виджетов
            anchor='w')
lb1.place(x=50, y=50)
ent1 = Entry()
ent1.place(x=200, y=50, width=150, height=45)



butt = Button(root, text="Отправить", fg="white", bg="#284b63")
butt.bind('<Button-1>', button_clicked) #отправка значений из entry по нажатию кнопки
butt.place(x=283, y=100)

root.mainloop()
