# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
# 72 x 28 = 2016 = > 5 последних забирает первый игроk

first_player = input('Enter first player ')
second_player = input('Enter second player ')
who_first_num = random.randint(1, 2)  # жеребьевка
who_first_name = None
who_second_name = None
if who_first_num == 1:
    print(f'Now is ur turn {first_player}')
    who_first_name = first_player
    who_second_name = second_player
else:
    print(f'Now is ur turn {second_player}')
    who_first_name = second_player
    who_second_name = first_player

borders = 28
count = 201
count_fi = 0
count_se = 0
while count >= 1:
    fi = int(
        input(f'Enter amount of candies u want to steal, {who_first_name} '))
    if fi > 28:
        while fi > 28:
            fi = int(input('Enter num under 28, u dirty player '))
    count_fi += fi
    count -= fi
    print(f'Now {count} of candies')
    if count <= 1:
        print(f'{first_player} You win!!')
        break
    se = int(
        input(f'Enter amount of candies u want to steal, {who_second_name} '))
    if se > 28:
        while se > 28:
            se = int(input('Enter num under 28, u dirty player '))
    count_se += se
    count -= se
    if count <= 1:
        print(f'{second_player} You win!!')
    print(f'Now {count} of candies')

print(f'{first_player} has {count_fi} candies and {second_player} has {count_se} candies')
print("Thank's for playing soul-cost game :) ")
