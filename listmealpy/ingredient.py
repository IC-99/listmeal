
class Ingredient:

    def __init__(self, name: str, amount: str) -> None:
        self.name = name
        self.amount = amount

    def edit(self, name: str, duration: int, price: float) -> None:
        self.name = name
        self.duration = duration
        self.price = price