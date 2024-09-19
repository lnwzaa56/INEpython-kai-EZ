import sqlite3

conn = sqlite3.connect("mydatabase.db")

cur = conn.cursor()

cur.execute('''
            create table if not exists users(
            id interger primary key autoincrement,
            name text not full, age integer not null, city text not null)''')


cur.execute("insert into user(name, age, city) values ("Alice",25,"New York")")
cur.execute("insert into user(name, age, city) values ("Bob",30,"Los Angeles")")
cur.execute("insert into user(name, age, city) values ("Charlie",35,"chicago")")

conn.commit()

cur.execute("select * from user where age > 28")
rows = cur.fetchall()

print("User plder than 28:")
for row in row:
    print(f"ID: {row[0]}, name:{row[1]}, Age:{row[2]}, city: {row[3]}")

conn.close()