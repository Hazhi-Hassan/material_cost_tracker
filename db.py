import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            date_added TEXT,
            price REAL,
            unit TEXT,
            description TEXT,
            seller_name TEXT,
            shop_location TEXT,
            phone TEXT
        )
        """)
        self.conn.commit()

    def get_all_items(self):
        return self.conn.execute("SELECT name, date_added, price, unit, description, seller_name, shop_location, phone FROM items").fetchall()

    def add_item(self, name, price, unit, description, seller_name, shop_location, phone):
        date_added = datetime.now().strftime("%Y-%m-%d")
        self.conn.execute("INSERT INTO items (name, date_added, price, unit, description, seller_name, shop_location, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (name, date_added, price, unit, description, seller_name, shop_location, phone))
        self.conn.commit()
