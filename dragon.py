from random import randint


#  по каждому цвету - ключ из характеристик: ХП, урон, сокровища
colors = {
'красный':[40,10,10],
'оранжевый':[40, 20, 10],
'желтый':[40, 10, 20],
'зеленый':[80, 10, 10],
'голубой':[40, 20, 20],
'синий':[80, 10, 20],
'фиолетовый':[80, 20, 10],
'черный':[80, 20, 20]
}


class Dragon():

	def __init__(self, color):
		self.color = color
		self.maxhp = colors[color][0]
		self.hp = self.maxhp
		self.treasuremax = colors[color][2]
		self.treasure = randint(1, self.treasuremax)
		self.damage = colors[color][1]

	def take_damage(self, damage):
		self.hp -= damage
