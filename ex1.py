# Напишите программу, удаляющую из текста все слова, содержащие 'абв'
my_str = 'Я люблю Джавуабв абви Питон'

lst = my_str.split(' ')

filtered_list = list(filter(lambda x: 'абв' not in x, lst))
print(*filtered_list)
