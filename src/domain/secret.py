class Secret:
    def __init__(self, id, creation_date, update_date, key, value) -> None:
        self.id = id
        self.creation_date = creation_date
        self.update_date = update_date
        self.key = key
        self.value = value