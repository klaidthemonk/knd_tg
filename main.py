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


def whats_next(knight):
    action = input('Что дальше? ')

    # /help command to show actions
    if action == 'help':
        print('''help - получить список команд
fight - сразиться с драконом
heal - вылечить раны
cemetary - отправиться на кладбище''')

    # /heal to heal hp to max
    elif action == 'heal':
        if knight.hp < knight.maxhp:
            knight.hp = knight.maxhp
            print(f'{knight.name} залечил свои раны!')
        else:
            print(f'{knight.name} уже здоров!')

    # fight with dragon to death
    elif action == 'fight':
        dragon = Dragon()
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
                if damage == 0:
                    print(f'Ух! {knight.name} уклоняется от дыхания дракона!')
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

    else:
        print('Такого действия нет. Напишите help чтобы получить список действий.')


game()
