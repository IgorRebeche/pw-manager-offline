class AuthorizationState:
    def __init__(self, salt, password) -> None:
        self.salt = salt
        self.password = password
    
    