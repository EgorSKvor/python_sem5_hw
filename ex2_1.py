import random
first_player = input('Enter ur Name ')
who_first_num = random.randint(1, 2)  # жеребьевка
bot = 'bot'
who_first_name = None
who_second_name = None
if who_first_num == 1:
    print(f'Now is ur turn {first_player}')
    who_first_name = first_player
    who_second_name = bot
else:
    print(f'Now is ur turn {bot}')
    who_first_name = bot
    who_second_name = first_player

borders = 28
count = 201
count_fi = 0
count_b = 0
while count >= 1:
    if who_first_name == bot:
        fi = random.randint(1, 28)
        print(f'Bot takes {fi} candies')
        count_fi += fi
        count -= fi
        print(f'Now {count} of candies')
        if count <= 1:
            print(f'{bot} wins')
            break
        se = int(
            input(f'Enter amount of candies u want to steal, {who_second_name} '))
        if se > 28:
            while se > 28:
                se = int(input('Enter num under 28, u dirty player '))
        count_b += se
        count -= se
        if count <= 1:
            print(f'{bot} win u :(')
        print(f'Now {count} of candies')
    else:
        fi = int(
            input(f'Enter amount of candies u want to steal, {who_first_name} '))
        if fi > 28:
            while fi > 28:
                fi = int(
                    input(f'Enter amount of candies u want to steal, {who_first_name} '))
        count_fi += fi
        count -= fi
        print(f'Now {count} of candies')
        if count <= 1:
            print(f'{first_player} You win!!')
            break
        se = random.randint(1, 28)
        print(f'Bot takes {se} candies')
        count_b += se
        count -= se
        if count <= 1:
            print(f'{bot} win u :(')
        print(f'Now {count} of candies')

    # fi = int(
    #     input(f'Enter amount of candies u want to steal, {who_first_name} '))
    # if fi > 28:
    #     while fi > 28:
    #         fi = int(input('Enter num under 28, u dirty player '))
    # count_fi += fi
    # count -= fi
    # print(f'Now {count} of candies')
    # if count <= 1:
    #     print(f'{first_player} You win!!')
    #     break
    # se = int(
    #     input(f'Enter amount of candies u want to steal, {who_second_name} '))
    # if se > 28:
    #     while se > 28:
    #         se = int(input('Enter num under 28, u dirty player '))
    # count_b += se
    # count -= se
    # if count <= 1:
    #     print(f'{bot} win u :(')
    # print(f'Now {count} of candies')

print(f'{first_player} has {count_fi} candies and {bot} has {count_b} candies')
print("Thank's for playing soul-cost game :) ")
