import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aditya3401",
    database="mydb"
    )

c = mydb.cursor()


def register(username, password):
    # Check if the username already exists
    c.execute('SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)', (username,))
    if c.fetchone()[0]:  # If the username exists
        print('Username already exists.')
        return

    # If the username does not exist, insert it into the database
    c.execute('INSERT INTO users (username, pword) VALUES (%s, %s)', (username, password))
    mydb.commit()
    print('User registered successfully.')
