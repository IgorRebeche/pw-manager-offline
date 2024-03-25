from typing import Any, Callable
from src.domain.secret import Secret


class SecretHistory:
    def __init__(self, id, secret_id, creation_date, key, value,  decryption_func: Callable[..., Any] = None) -> None:
        self.id = id
        self.secret_id = secret_id
        self.creation_date = creation_date
        self.key = key
        self.value = value
        self.decryption_func = decryption_func
    
    @staticmethod
    def create_by_secret(self, id, secret: Secret):
        return SecretHistory(id=id, secret_id=secret.id, creation_date=secret.update_date, value=secret.value)
        
    def get_value(self):
        return self.decryption_func(self.value) if self.decryption_func else self.value 