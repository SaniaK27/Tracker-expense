class Expense:
    def __init__(self, name , category, money) -> None:
        self.name = name
        self.category = category
        self.money = money

    def __repr__(self) -> str:
        return f"<Expense>: {self.name}, {self.category}, ${self.money:.2f}"