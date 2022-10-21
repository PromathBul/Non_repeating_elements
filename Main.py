from Methods import enter
from Methods import сreate_list_random_num as create
from Methods import list_unrepeat_num as unrepeat
import os

os.system('cls')

length = enter('Введите количество чисел в изначальной последовательности: ')
min = enter('Введите минимальное значение элементов: ')
max = enter('Введите максимальное значение элементов: ')

my_list = create(length, min, max)
print(f'Изначальная последовательность:\n{my_list}')

print(f'\nСписок неповторяющихся элементов изначальной последовательности:')
unrepeat_list = unrepeat(my_list)
print(unrepeat_list)