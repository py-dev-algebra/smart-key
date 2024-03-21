import sqlite3

from constants.app_consts import DB_PATH


def db_init():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            pin TEXT,
                            is_active INTEGER
                        )
                    ''')
    
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if len(users) == 0:
        cursor.execute('''
                        INSERT INTO users (first_name, last_name, pin, is_active)
                        VALUES (?, ?, ?, ?)
                        ''',
                        ('Pero', 'Peric', '9876', 1))

    conn.commit()
    cursor.close()
    conn.close()


def check_users_pin(pin: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
   
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    for user in users:
        if user[3] == pin:
            cursor.close()
            conn.close()
            return user
    
    cursor.close()
    conn.close()
    return None


def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
   
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()    
    
    cursor.close()
    conn.close()
    return users


def get_user(id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
   
    cursor.execute('SELECT * FROM users WHERE id=?', (id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user


def delete_user(id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
   
    cursor.execute('DELETE FROM users WHERE id=?', (id,))
    
    conn.commit()
    cursor.close()
    conn.close()


def save_user(id: int, first_name: str, last_name: str, pin: str, is_active: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
     
    cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
    user = cursor.fetchone()

    if user:
        cursor.execute('''
                       UPDATE users
                       SET first_name = ?,
                            last_name = ?,
                            pin = ?,
                            is_active = ?)
                       WHERE id = ?
                        ''',
                        (first_name, last_name, pin, is_active, id))
    else:
        cursor.execute('''
                        INSERT INTO users (first_name, last_name, pin, is_active)
                        VALUES (?, ?, ?, ?)
                        ''',
                        (first_name, last_name, pin, is_active))

    conn.commit()
    cursor.close()
    conn.close()
