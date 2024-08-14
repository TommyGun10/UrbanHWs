import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL, 
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                ("User", "example@gmail.com", "10", "1000"))
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))

cursor.execute('''
    UPDATE users
    SET balance = 500
    WHERE id IN (
        SELECT id FROM users WHERE id % 2 = 1
    )
''')

cursor.execute('DELETE FROM users WHERE id IN (SELECT id FROM users WHERE id % 3 = 1)')

cursor.execute('SELECT username, email, age, balance FROM users WHERE age != 60')

results = cursor.fetchall()

for row in results:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

connection.commit()
connection.close()
