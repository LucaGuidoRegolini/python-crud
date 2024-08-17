import datetime


class Contract:

    def __init__(self, user_id, fidelity, amount, description="",):
        self.user_id = user_id
        self.fidelity = fidelity
        self.amount = amount
        self.description = description
        self.created_at = datetime.datetime.now()

    def validate(self):
        if not self.user_id or not self.fidelity or not self.amount:
            return ValueError("User id, fidelity and amount are required")

        if self.fidelity < 0 or self.amount < 0:
            return ValueError("Invalid fidelity or amount")
