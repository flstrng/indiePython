"""
02_12_D
Программа получает на вход список целых чисел и ваша задача
вывести каждый третий элемент этого списка, начиная со второго по счету значения.

Sample Input:
8 32 5 87 2 43 53 23 5
Sample Output:
[32, 2, 23]
"""
my_list = list(map(int, input().split()))
print(my_list[1::3])