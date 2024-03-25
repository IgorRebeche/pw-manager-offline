from datetime import datetime
import os
import sqlite3
from typing import List

from src.domain.secret import Secret

class SecretRepository():
    def __init__(self) -> None:
        current_dir = os.path.dirname(__file__)
        self.db_path = os.path.join(current_dir, '..', '..', 'output', 'data.db')
        self.init_db()
        pass
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS secret 
                          (id INTEGER PRIMARY KEY, key TEXT, value TEXT, creation_date TEXT, update_date TEXT)''')
        conn.commit()
        conn.close()
    
    def get_secret_value_by_key(self, key) -> Secret:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM secret WHERE key = ?", (key,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def get_secret(self, key) -> Secret:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, key, value, creation_date, update_date FROM secret WHERE key = ?", (key,))
        row = cursor.fetchone()
        conn.close()
        
        return Secret(id=row[0], key=row[1], value=row[2], creation_date=row[3], update_date=row[4])
    
    def create_secret(self, key, value):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO secret (key, value, creation_date, update_date) VALUES (?, ?, ?, ?)", 
                       (key, value, current_time, current_time))
        conn.commit()
        conn.close()
    
    def delete_secret(self, key):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM secret WHERE key = ?", (key,))
        conn.commit()
        conn.close()
    
    def update_secret(self, key, new_value):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE secret SET value = ?, update_date = ? WHERE key = ?", 
                       (new_value, current_time, key))
        conn.commit()
        conn.close()
    
    def get_all_secrets(self) -> List[Secret]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, key, value, creation_date, update_date FROM secret")
        secrets_data = cursor.fetchall()
        conn.close()
        return [Secret(id=row[0], key=row[1], value=row[2], creation_date=row[3], update_date=row[4]) for row in secrets_data]

    
    