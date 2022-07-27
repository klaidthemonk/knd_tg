from random import randint


#  по каждому цвету - ключ из характеристик: ХП, урон, сокровища
colors = {
'красный':[40,10,20],
'оранжевый':[40, 20, 20],
'желтый':[40, 10, 40],
'зеленый':[80, 10, 20],
'голубой':[40, 20, 40],
'синий':[80, 10, 40],
'фиолетовый':[80, 20, 20],
'черный':[80, 20, 40]
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
