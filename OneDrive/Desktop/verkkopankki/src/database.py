import sqlite3

def create_database():
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    # Luo käyttäjätaulu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        balance REAL DEFAULT 0
    )
    """)

    # Luo tapahtumataulu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        transaction_type TEXT NOT NULL,
        amount REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    connection.commit()
    connection.close()

def add_user(username, password):
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
    except sqlite3.IntegrityError:
        print("Käyttäjänimi on jo käytössä.")
    connection.close()

def get_user(username):
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.close()
    return user
