

import os
import sqlite3
from typing import Callable, List
from src.domain.secret_history import SecretHistory
from src.domain.secret import Secret


class SecretHistoryRepository:
    def __init__(self) -> None:
        current_dir = os.path.dirname(__file__)
        self.db_path = os.path.join(current_dir, '..', '..', 'output', 'data.db')
        pass
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS secret_history 
                          (id INTEGER PRIMARY KEY, secret_id INTEGER, key TEXT, value TEXT, creation_date TEXT)''')
        conn.commit()
        conn.close()
    
    def create_secret_history(self, secret: Secret):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO secret_history (secret_id, key, value, creation_date) VALUES (?, ?, ?, ?)", 
                       (secret.id, secret.key, secret.value, secret.update_date))
        conn.commit()
        conn.close()
        
    def delete_all_secret_history_by_key(self, key):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM secret_history WHERE key = ?", (key,))
        conn.commit()
        conn.close()
    
    def get_all_history_by_key(self, key, decryption_func: Callable = None) -> List[SecretHistory]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, secret_id, key, value, creation_date FROM secret_history WHERE key = ?", (key,))
        history = [SecretHistory(id=row[0], secret_id=row[1], key=row[2], value=row[3], creation_date=row[4], decryption_func=decryption_func) for row in cursor.fetchall()]
        conn.close()
        return history