#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
#мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
#1. в каких магазинах нельзя приобрести сыр.
#2. в каких магазинах можно приобрести одновременно молоко и сахар.
#3. в каких магазинах можно приобрести соль.
#Вариант 8



magnit = {"молоко", "соль" , "сахар"} #создание множеств
pyaterochka = {"мясо", "молоко", "сыр"}
perecrestok = {"молоко", "творого" , "сыр", "сахар"}
sir = set()
moloko = set()
sol = set()

#1

if "сыр" not in magnit: #проверка наличия товара
    sir.add("Магнит")
else :
    pass

if "сыр" not in pyaterochka:
    sir.add("Пятерочка")
else:
    pass

if "сыр" not in perecrestok:
    sir.add("Перекресток")
else:
    pass

print(sir)

#2

if "молоко" and "сахар" not in magnit: #проверка наличия товара
    pass
else:
    moloko.add("Магнит")

if "молоко" and "сахар" not in pyaterochka:
    pass
else:
    moloko.add("Пятерочка")

if "молоко" and "сахар" not in perecrestok:
    pass
else:
    moloko.add("Перекресток")

print(moloko)

#3

if "соль" not in magnit:     #проверка наличия товара
    pass
else:
    sol.add("Магнит")

if "соль" not in pyaterochka:
    pass
else:
    sol.add("Пятерочка")

if "соль" not in perecrestok:
    pass
else:
    sol.add("Перекресток")

print(sol)