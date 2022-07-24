from random import randint


class Knight():

    def __init__(self, name):
        self.name = name
        self.maxhp = 10
        self.hp = self.maxhp
        self.gold = 0  # текущее количество монет в кошельке
        self.treasure = 0  # получено монет всего за игру
        self.damage = 10
        self.frags = 0  # количество убитых драконов
        self.rested = False
        self.shield = False
        self.spf = False

    def take_damage(self, damage):
        self.hp -= damage

    def take_treasure(self, treasure):
        self.gold += treasure
        self.treasure += treasure
        self.rested = False
        self.spf = False

    def rest(self):
        if self.hp >= self.maxhp:
            return 'healthy'
        elif self.rested == False:
            self.hp += randint(1, self.maxhp - self.hp)
            self.rested = True
            return 'rest'
        else:
            self.rested = True
            return 'rested'