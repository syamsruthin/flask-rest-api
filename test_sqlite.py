import sqlite3

conn = sqlite3.connect("./Section6/data.db")
cursor = conn.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "user1", "pass1")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, "user2", "pass2"),
    (3, "user3", "pass3")
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

conn.commit()
conn.close()