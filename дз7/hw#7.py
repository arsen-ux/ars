import sqlite3 as sql3


conn = sql3.connect('users.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        salary REAL NOT NULL
    )
''')


employees = [
    ('Arsen', 50000),
    ('Kuba', 55000),
    ('Bekbolot', 60000),
    ('Manas', 65000),
    ('Semetey', 70000),
    ('Cristiano', 75000),
    ('Messi', 80000),
    ('Jordan', 85000),
    ('Muhammad', 90000),
    ('Kobe', 95000)
]

cursor.executemany('''
    INSERT INTO employees (name, salary)
    VALUES (?, ?)
''', employees)


conn.commit()


cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()


for row in rows:
    print(row)

conn.close()
