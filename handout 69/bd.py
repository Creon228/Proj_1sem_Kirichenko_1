import sqlite3 as sq

with sq.connect('Store.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sales (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    tovar TEXT NOT NULL,
    izm TEXT NOT NULL,
    amount INTEGER,
    cost INTEGER
    )""")
    cur.execute("""INSERT INTO sales (name, tovar, izm, amount, cost) VALUES ('Макаров Н.Г', 'кофеварка', 'шт', 1, 15000)""")
    cur.execute("""INSERT INTO sales (name, tovar, izm, amount, cost) VALUES ('Королёв А.Ф', 'холодильник', 'шт', 10, 30000)""")
    cur.execute("""INSERT INTO sales (name, tovar, izm, amount, cost) VALUES ('Кудряшова П.Э', 'пылесос', 'шт', 2, 13500)""")
    cur.execute("""INSERT INTO sales (name, tovar, izm, amount, cost) VALUES ('Гаврилова М.А', 'перфоратор', 'шт', 4, 3750)""")
    cur.execute("""INSERT INTO sales (name, tovar, izm, amount, cost) VALUES ('Молчанова М.Г', 'фен', 'шт', 5, 7850)""")

