from src.services.secret_service import SecretService
from texttable import Texttable

class SecretController:
    def __init__(self, secret_service: SecretService) -> None:
        self.secret_service = secret_service
        
    def create_secret(self, key, value):
        self.secret_service.create_secret(key, value)
        print(f'Secret with key {key} created!')
        
    def get_secret_by_key(self, key):
        value = self.secret_service.get_secret_by_key(key)
        print(f'Key: {key} returned secret: {value}')
        
    def delete_secret_by_key(self, key):
        self.secret_service.delete_secret(key)
        print(f"Key {key} deleted")
    
    def update_secret_by_key(self, key, value):
        self.secret_service.update_secret(key, value)
        print(f"Key {key} updated!")
    
    def list_secrets(self):
        t = Texttable()
        secrets = self.secret_service.get_all_secrets()
        rows = [['Id', 'Key', 'Created Date', 'Updated Date' ]]
        for secret in secrets:
            rows.append([secret.id, secret.key, secret.creation_date, secret.update_date])
            
        t.add_rows(rows)
        print(t.draw())
        
    def list_secret_history(self, key):
        t = Texttable()
        secret_histories = self.secret_service.get_all_secret_history_by_key(key)
        rows = [['Id', 'Key', 'Created Date', 'Value' ]]
        for secret_history in secret_histories:
            rows.append([secret_history.id, secret_history.key, secret_history.creation_date, secret_history.get_value()])
            
        t.add_rows(rows)
        print(t.draw())
        