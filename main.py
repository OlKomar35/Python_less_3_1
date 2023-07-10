# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

print(array_n := [random.randint(0, 15) for _ in range(int(input('n= ')))])
print(array_m := [random.randint(0, 5) for _ in range(int(input('m= ')))])

set_n = set(array_n)
set_m = set(array_m)

print(result_set := set_n.intersection(set_m))

print(sorted(list(result_set)))
