# Player class
class Player:
    def __init__(self, name, total_cash):
        self.total_cash = total_cash
        self.name = name

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'{self.name} ${self.total_cash}'