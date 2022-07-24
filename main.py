import codecs
from random import randint
from dragon import Dragon
from knight import Knight


def game():
    gameover = False
    while gameover is False:
        name = input('Введите имя рыцаря: ')
        if name == '':
            continue
        knight = Knight(name)
        while knight.hp > 0:
            whats_next(knight)
        print(f'{knight.name} мёртв!')
        print(f'{knight.name} в своих приключениях убил {knight.frags} драконов и заработал {knight.treasure} монет.')
        print(f'{knight.name} навсегда останется лежать на кладбище.')
        mourning(knight)
        print('Введите что угодно чтобы начать заново')
        again = input('Q чтобы закончить игру ')
        if again == 'Q':
            gameover = True


def mourning(knight):
    cemetary_file = codecs.open('cemetary.txt', 'a', 'utf-8')
    headstone = f'{knight.name}, {knight.treasure}\n'
    cemetary_file.writelines(headstone)
    cemetary_file.close()


def cemetary(knight):
    cemetary_file = codecs.open('cemetary.txt', 'r', 'utf-8')
    dead_knights = cemetary_file.readlines()

    if len(dead_knights) == 0:
        print(f'На кладбище солнечно и пусто. {knight.name} может оказаться здесь первым.')

    else:
        print(f'На кладбище так холодно...')
        print(f'Здесь могилы погибших рыцарей')

        if len(dead_knights) % 10 == 1:
            ending = 'могила'
        elif len(dead_knights) % 10 in [2, 3, 4]:
            ending = 'могилы'
        else:
            ending = 'могил'
        print(f'Всего {len(dead_knights)} {ending}')

        count = int(input('Сколько могил осмотреть? '))
        if count > len(dead_knights):
            print ('На кладбище нет столько могил.')
        else:
            headstones = []
            for dead_knight in dead_knights:
                name = dead_knight.split(sep=',')[0]
                money = int(dead_knight.split(sep=',')[1])
                headstones.append((name, money))
            headstones.sort(key=lambda x: -x[1])
            for headstone in headstones[:count]:
                print(f'{headstone[0]}, {headstone[1]}')
            cemetary_file.close()

def shopping(knight):
    print('Добро пожаловать в магазин!')
    item = ''
    while item != 'Q':
        item = input('Что бы вы хотели купить? ')
        if item == 'help':
            print('''Помощь бесплатна!
heal - полностью вылечиться (1 монета за 1 очко здоровья)
sword - заточить меч и увеличить атаку на 1 (10 монет)
health - зелье повышения максимального здоровья на 1 (10 монет)
shield - купить щит, который спасёт в фатальной ситуации (10 монет)
spf - солнцезащитный крем 1000 SPF, спасающий от ожогов (10 монет)
status - заглянуть в кошелёк
Q чтобы уйти из магазина''')

        elif item == 'heal':
            if knight.hp == knight.maxhp:  # если рыцарь здоров
                print(f'{knight.name} уже здоров!')
            elif knight.gold < knight.maxhp - knight.hp:  # если рыцарю не хватит денег на полное лечение
                knight.hp += knight.gold
                knight.gold = 0
                print(f'Это всё, на что хватит денег. {knight.name} теперь имеет {knight.hp} очков здоровья.')
            else:
                knight.gold -= knight.maxhp - knight.hp
                knight.hp = knight.maxhp
                print(f'{knight.name} лечится полностью и у него остаётся {knight.gold} монет!')

        elif item == 'sword':
            if knight.gold < 10:  # 10 - цена заточки меча
                print(f'{knight.name} имеет всего {knight.gold} монет. Заточка меча стоит 10.')
            else:
                knight.gold -= 10
                knight.damage += 1
                print(f'{knight.name} заточил свой меч и теперь наносит до {knight.damage} урона!')

        elif item == 'health':
            if knight.gold < 10:  # 10 - цена зелья здоровья
                print(f'{knight.name} имеет всего {knight.gold} монет. Зелье здоровья стоит 10.')
            else:
                knight.gold -= 10
                knight.maxhp += 1
                knight.hp += 1
                print(f'{knight.name} выпил зелье и теперь его максимальное здоровье -  {knight.maxhp}!')

        elif item == 'shield':
            if knight.shield == True:
                print(f'{knight.name} уже носит щит! Второй ему ни к чему.')
            elif knight.gold < 10:  # 10 - цена щита
                print(f'{knight.name} имеет всего {knight.gold} монет. Щит стоит 10.')
            else:
                knight.gold -= 10
                knight.shield = True
                print(f'{knight.name} купил щит!')

        elif item == 'spf':
            if knight.spf == True:
                print(f'{knight.name} уже нанёс крем от ожогов.')
            elif knight.gold < 10:  # 10 - цена солнцезащитного крема
                print(f'{knight.name} имеет всего {knight.gold} монет. Солнцезащитный крем стоит 10.')
            else:
                knight.gold -= 10
                knight.spf = True
                print(f'{knight.name} купил крем от ожогов!')

        elif item == 'status':
            print(f'{knight.name} смотрит в кошелёк. Монет в нём - {knight.gold}.')

        elif item == 'Q':
            break

        else:
            print('Такого в продаже нет. Напишите help чтобы узнать, что продаётся.')


def get_dragon(knight):
    dragon_rainbow = ['красный']
    color = dragon_rainbow[randint(0,len(dragon_rainbow))]
    return color


def whats_next(knight):
    action = input('Что дальше? ')

    # /help command to show actions
    if action == 'help':
        print('''help - получить список команд
fight - сразиться с драконом
rest - вылечить раны
shop - отправиться в магазин
cemetary - отправиться на кладбище''')

    # /rest to heal hp a bit
    elif action == 'rest':
        rest = knight.rest()
        if rest == 'healthy':
            print(f'{knight.name} здоров!')
        elif rest == 'rest':
            print(f'{knight.name} отдыхает и теперь у него {knight.hp} очков здоровья!')
        elif rest == 'rested':
            print(f'{knight.name} уже отдыхал сегодня! Пора в бой!')

    # fight with dragon to death
    elif action == 'fight':
        color = get_dragon(knight)
        dragon = Dragon(color)
        print('Дракон нападает!')
        counter = 1
        while dragon.hp > 0:

            # knight attacks
            if counter % 5 != 0:  # 5 - это скорость атаки рыцаря (4) плюс 1 атака дракона
                damage = randint(0, knight.damage)
                if damage == 0:
                    print(f'Упс! {knight.name} промахивается!')
                else:
                    dragon.take_damage(damage)
                    print(f'{knight.name} наносит {damage} урона дракону!')

            # dragon attacks
            else:
                damage = randint(0, dragon.damage)
                if knight.spf == True:
                    damage -= 1
                if damage <= 0:
                    print(f'Ух! {knight.name} уклоняется от дыхания дракона!')
                elif damage >= knight.hp and knight.shield == True:
                    knight.shield = False
                    print(f'Ух! {knight.name} спасается от дыхания дракона за щитом! Щит разваливается на куски.')
                else:
                    knight.take_damage(damage)
                    if knight.hp > 0:
                        print(f'Ай! {knight.name} получает {damage} урона!')
                    else:
                        print('Ой...')
                        break
            counter += 1

        if dragon.hp <= 0:
            knight.take_treasure(dragon.treasure)
            knight.frags += 1
            print(f'{knight.name} убивает дракона и получает {dragon.treasure} монет!')

    elif action == 'cemetary':
        cemetary(knight)

    elif action == 'shop':
        shopping(knight)

    else:
        print('Такого действия нет. Напишите help чтобы получить список действий.')


game()
