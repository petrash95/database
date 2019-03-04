import sqlite3

conn = sqlite3.connect(':memory:')
#/Users/Petrash/PycharmProjects/database/userdata.db
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS users (
            id integer PRIMARY KEY,
           name text NOT NULL,
           surname text NOT NULL
           )""")


#c.execute("INSERT INTO users VALUES ('1', 'Ruben', 'Kopan')")

#c.execute("SELECT * FROM users WHERE name='Ruben'")
#print(c.fetchone())

c.execute(""" CREATE TABLE IF NOT EXISTS history (
           id integer PRIMARY KEY,
          conversation text NOT NULL
            )""")
conn.commit()
conn.close()