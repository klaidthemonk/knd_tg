from random import randint


class Dragon():

	def __init__(self, color):
		self.color = color
		self.maxhp = 40
		self.hp = self.maxhp
		self.treasuremax = 10
		self.treasure = randint(1, self.treasuremax)
		self.damage = 10

	def take_damage(self, damage):
		self.hp -= damage
