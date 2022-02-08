class PlayerCharacter:
    # classs object attribute
    membership = True
    def __init__(self, name , gun):
        self.name = name
        self.gun = gun

    def run(self):
        print("Hello")
        return "done"

player1 = PlayerCharacter("lukshark" , 12)
player1.attack = 198
print(player1.name)
print(player1.attack)
