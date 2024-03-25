from datetime import datetime


class EncryptorConfiguration:
    def __init__(self, id, key, value, creation_date, update_date) -> None:
        self.id = id
        self.key = key
        self.value = value
        self.creation_date = creation_date
        self.update_date = update_date
        
    @staticmethod
    def create(key, value):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return EncryptorConfiguration(None, key, value, now, now)