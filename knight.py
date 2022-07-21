class Knight():

    def __init__(self, name):
        self.name = name
        self.maxhp = 10
        self.hp = self.maxhp
        self.gold = 0
        self.treasure = 0
        self.damage = 10
        self.frags = 0

    def take_damage(self, damage):
        self.hp -= damage

    def take_treasure(self, treasure):
        self.gold += treasure
        self.treasure += treasure
