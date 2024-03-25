from src.repositories.secret_history_repository import SecretHistoryRepository
from src.services.authorization_service import AuthorizationService
from src.services.encryptor_service import EncryptorService
from src.repositories.secret_repository import SecretRepository


class SecretService:
    def __init__(self, secret_repository: SecretRepository, secret_history_repository: SecretHistoryRepository, encryptor_service: EncryptorService, authorization_service: AuthorizationService) -> None:
        self.secret_repository = secret_repository
        self.secret_history_repository = secret_history_repository
        self.encryptor_service = encryptor_service
        self.authorization_service = authorization_service
    
    def get_secret_by_key(self, key):
        encrypted_data = self.secret_repository.get_secret_value_by_key(key)
        return self.decrypt_data(encrypted_data)
    
    def get_all_secrets(self):
        return self.secret_repository.get_all_secrets()
    
    def get_all_secret_history_by_key(self, key):
        secret_histories = self.secret_history_repository.get_all_history_by_key(key, decryption_func=self.decrypt_data)
        return secret_histories
    
    def create_secret(self, key, value):
        if self.secret_repository.get_secret_value_by_key(key) is not None:
            print('Secret with this key aready exist!')
            return
        
        self.secret_repository.create_secret(key, self.encrypt_data(value))
        self.secret_history_repository.create_secret_history(self.secret_repository.get_secret(key))
    
    def delete_secret(self, key):
        self.secret_repository.delete_secret(key)
        self.secret_history_repository.delete_all_secret_history_by_key(key)

    def update_secret(self, key, value):
        self.secret_repository.update_secret(key,  self.encrypt_data(value))
        self.secret_history_repository.create_secret_history(self.secret_repository.get_secret(key))
    
    def encrypt_data(self, data):
        authorization_state = self.authorization_service.authorization_state
        return self.encryptor_service.encrypt(
            authorization_state.salt,
            authorization_state.password,
            data
        )
        
    def decrypt_data(self, data):
        authorization_state = self.authorization_service.authorization_state
        return self.encryptor_service.decrypt(
            authorization_state.salt,
            authorization_state.password, 
            data
        )