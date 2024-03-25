import ctypes
from src.domain.encryptor_configuration import EncryptorConfiguration
from src.domain.authorization_state import AuthorizationState
from src.repositories.encryptor_configuration_repository import EncryptorConfigurationRepository
from src.services.encryptor_service import EncryptorService


class AuthorizationService:
    def __init__(self, encryptor_service: EncryptorService, encryptor_configuration_repository: EncryptorConfigurationRepository) -> None:
        self.encryptor_service = encryptor_service
        self.encryptor_configuration_repository = encryptor_configuration_repository
    
    def create_if_not_exist(self):
        if self.encryptor_configuration_repository.get_master_password_hash() is None:
            self._create()
            
        
    def _create(self):
        print("Welcome to password manager! Let start creating a strong password!")
        
        password = input("Type a strong password: ")
        password_hash = self.encryptor_service.create_256_bit_hash(password)
        salt = self.encryptor_service.generate_salt()
        
        self.encryptor_configuration_repository.create_encryption_configurations([
            EncryptorConfiguration.create("salt", salt)
        ])
        
        self.encryptor_configuration_repository.create_master_password_hash(password_hash)
        
        
    def authorize(self):
        password = input("Please enter your password to authorize:")
        if self.__validate_master_password(password):
            print("Authorized!")
            salt = self.encryptor_configuration_repository.get_encryption_configuration_by_key('salt')
            
            self.authorization_state = AuthorizationState(salt, password)
            return True
        
        return False
        
    def clean_memory(self):
        self.secure_delete_object(self.authorization_state)
      
    def secure_delete_object(self, obj):
        """
        Securely delete the contents of an object from memory by overwriting its attributes.
        """
        # Iterate over object attributes
        for attr_name in dir(obj):
            # Check if attribute is not a method or special attribute
            if not attr_name.startswith('__') and not callable(getattr(obj, attr_name)):
                # Overwrite attribute with None
                setattr(obj, attr_name, None)
        # Delete the object
        del obj 
        
    def __validate_master_password(self, password):
        encrypted_password = self.encryptor_service.create_256_bit_hash(password)
        encrypted_password_from_bb = self.encryptor_configuration_repository.get_master_password_hash()
        return encrypted_password == encrypted_password_from_bb
    
    