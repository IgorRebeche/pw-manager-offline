import os
import sqlite3
from typing import List

from src.domain.encryptor_configuration import EncryptorConfiguration

class EncryptorConfigurationRepository:
    def __init__(self) -> None:
        current_dir = os.path.dirname(__file__)
        self.db_path = os.path.join(current_dir, '..', '..', 'output', 'data.db')
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS encryptor_configuration 
                          (id INTEGER PRIMARY KEY, key TEXT, value TEXT, creation_date TEXT, update_date TEXT)''')
        conn.commit()
        conn.close()
    
    def get_master_password_hash(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM encryptor_configuration WHERE key = 'master_password_hash'")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def create_master_password_hash(self, hash):
        self.create_encryption_configuration(EncryptorConfiguration.create('master_password_hash', hash))
    
    def save_password_hash(self, password_hash):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO encryptor_configuration (key, value) VALUES ('master_password_hash', ?)", (password_hash,))
        conn.commit()
        conn.close()
    
    def get_encryption_configurations(self) -> List[EncryptorConfiguration]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM encryptor_configuration")
        configurations = [EncryptorConfiguration(*row) for row in cursor.fetchall()]
        conn.close()
        return configurations
    
    def get_encryption_configuration_by_key(self, key):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT value FROM encryptor_configuration WHERE key = '{key}'")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    
    def create_encryption_configurations(self, configurations: List[EncryptorConfiguration]):
        for config in configurations:
            self.create_encryption_configuration(config)
    
    def create_encryption_configuration(self, configuration: EncryptorConfiguration):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO encryptor_configuration (key, value, creation_date, update_date) VALUES (?, ?, ?, ?)", 
                       (configuration.key, configuration.value, configuration.creation_date, configuration.update_date))
        conn.commit()
        conn.close()
    
    def update_encryption_configuration(self, configuration: EncryptorConfiguration):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE encryptor_configuration SET key = ?, value = ?, creation_date = ?, update_date = ? WHERE id = ?", 
                       (configuration.key, configuration.value, configuration.creation_date, configuration.update_date, configuration.id))
        conn.commit()
        conn.close()
