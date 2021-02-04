# Card class
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.value}{self.color}'
