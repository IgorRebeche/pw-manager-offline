from src.controller.secret_controller import SecretController
from src.services.backup_service import BackupService
from src.services.terminal_view_service import Item, TerminalViewService
from src.services.secret_service import SecretService
from src.services.authorization_service import AuthorizationService
from src.services.encryptor_service import EncryptorService

from src.repositories.secret_history_repository import SecretHistoryRepository
from src.repositories.secret_repository import SecretRepository
from src.repositories.encryptor_configuration_repository import EncryptorConfigurationRepository


class App:
    def __init__(self) -> None:
        self.__create_instances()
    
    def __create_instances(self):
        
        self.encryptor_configuration_repository = EncryptorConfigurationRepository()
        self.secret_history_repository = SecretHistoryRepository()
        self.secret_repository = SecretRepository()
        
        self.encryptor_service = EncryptorService()
        
        self.backup_service = BackupService()
        
        self.authorization_service = AuthorizationService(
            self.encryptor_service, self.encryptor_configuration_repository)
        
        self.secret_service = SecretService(
            self.secret_repository, self.secret_history_repository, self.encryptor_service, self.authorization_service)
        
        self.secret_use_case = SecretController(self.secret_service)
        
        self.view = TerminalViewService()