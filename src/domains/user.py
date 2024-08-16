class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def validate(self):
        if not self.name or not self.email:
            raise ValueError("Name and email are required")
        # Add other domain logic if needed
