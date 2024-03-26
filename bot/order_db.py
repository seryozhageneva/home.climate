import sqlite3

def create_orders_table():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        chat_id INTEGER,
                        full_name TEXT,
                        address TEXT,
                        phone_number TEXT,
                        article TEXT)''')
    conn.commit()
    conn.close()

def insert_order(chat_id, full_name, address, phone_number, article):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO orders (chat_id, full_name, address, phone_number, article) 
                      VALUES (?, ?, ?, ?, ?)''', (chat_id, full_name, address, phone_number, article))
    conn.commit()
    conn.close()
