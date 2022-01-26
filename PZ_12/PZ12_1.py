# Вариант 8

from tkinter import *
from tkinter import ttk

root = Tk() #создание главного окна
root.title("Sign Up") #создание заголовка окна
root.geometry('600x650')
root.configure(bg='#222536')
root.resizable(height="false", width="false")
# root.Label(root, text="Sign up")

lb1 = Label(root, text="Sign Up", bg="orange", fg="yellow", pady=10, width=100, font=('Arial', '12', 'bold'), #добавление виджета label
            anchor='w')
lb1.place(x=0, y=0) #упаковка виджета
lb2 = Label(root, text="First Name", fg="yellow", font=('Arial', '12'), bg='#222536')
lb2.place(x=80, y=50)
ent = Entry()
ent.place(x=200, y=50, width=375, height=25)

lb3 = Label(root, text="Last Name", fg="yellow", font=('Arial', '12'), bg='#222536')
lb3.place(x=80, y=100)
ent1 = Entry() #добавление виджета entry
ent1.place(x=200, y=100, width=375, height=25)

lb4 = Label(root, text="Screen Name", fg="yellow", font=('Arial', '12'), bg='#222536')
lb4.place(x=80, y=150)
ent2 = Entry()
ent2.place(x=200, y=150, width=375, height=25)

lb5 = Label(root, text="Date of Birth", fg="yellow", font=('Arial', '12'), bg='#222536')
lb5.place(x=80, y=200)
combo1 = ttk.Combobox() #добавлене виджета combobox
combo1.place(x=200, y=200, width=100, height=25)
combo2 = ttk.Combobox()
combo2.place(x=350, y=200, width=60, height=25)
combo2 = ttk.Combobox()
combo2.place(x=450, y=200, width=80, height=25)

lb6 = Label(root, text="Gender", fg="yellow", font=('Arial', '12'), bg='#222536')
lb6.place(x=80, y=250)
check1 = Radiobutton(root, text="Male", fg="yellow", font=('Arial', '10'), bg='#222536') #добавление виджета radiobutton
check1.place(x=200, y=250)
check1 = Radiobutton(root, text="Female", fg="yellow", font=('Arial', '10'), bg='#222536')
check1.place(x=270, y=250)

lb7 = Label(root, text="Country", fg="yellow", font=('Arial', '12'), bg='#222536')
lb7.place(x=80, y=300)
combo3 = ttk.Combobox()
combo3.place(x=200, y=300, width=375, height=25)

lb8 = Label(root, text="Email", fg="yellow", font=('Arial', '12'), bg='#222536')
lb8.place(x=80, y=350)
ent3 = Entry()
ent3.place(x=200, y=350, width=375, height=25)

lb9 = Label(root, text="Phone", fg="yellow", font=('Arial', '12'), bg='#222536')
lb9.place(x=80, y=400)
ent4 = Entry()
ent4.place(x=200, y=400, width=375, height=25)

lb10 = Label(root, text="Password", fg="yellow", font=('Arial', '12'), bg='#222536')
lb10.place(x=80, y=450)
ent5 = Entry()
ent5.place(x=200, y=450, width=375, height=25)

lb11 = Label(root, text="Confirm Password", fg="yellow", font=('Arial', '12'), bg='#222536')
lb11.place(x=20, y=500)
ent6 = Entry()
ent6.place(x=200, y=500, width=375, height=25)

check2 = Checkbutton(root, text="I agree to the Terms of Use", fg="yellow", font=('Arial', '10'), bg='#222536') #добавление виджета checkbutton
check2.place(x=200, y=540)

lb12 = Label(root, text="Sign Up", bg="orange", fg="orange", pady=10, width=150, height=50,
             font=('Arial', '12', 'bold'), anchor='w')
lb12.place(x=0, y=600)
butt1 = Button(root, text="submit", bg="lightgreen", fg="white", font=('Arial', '10', 'bold'))
butt1.place(x=450, y=615)
butt2 = Button(root, text="Cancel", bg="red", fg="white", font=('Arial', '10', 'bold'))
butt2.place(x=510, y=615)

root.mainloop()