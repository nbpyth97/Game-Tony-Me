class Guardian:
    def __init__(self):
        self.hp = 50
        self.at = 60
        self.de = 50

guardian = Guardian()

class Tank:
    def __init__(self, hp, at, de):
        self.hp = hp
        self.at = at
        self.de = de

tank = Tank(60, 30, 70)

class Magician:
    def __init__(self, hp, at, de):
        self.hp = hp
        self.at = at
        self.de = de

magician = Magician(40, 80, 40)
