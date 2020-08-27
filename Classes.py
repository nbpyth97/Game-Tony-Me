class Guardian:
    def __init__(self):
        self.hp = 50
        self.at = 60
        self.de = 50

guardian = Guardian()

class Tank:
    def __init__(self, hp, at, de):
        self.hp = 60
        self.at = 30
        self.de = 70

tank = Tank()

class Magician:
    def __init__(self, hp, at, de):
        self.hp = 40
        self.at = 80
        self.de = 40

magician = Magician()
