"""
02_11_E
Программа получает на вход список из целых чисел. Ваша задача найти сумму списка
Примечание:

Чтобы прочитать из ввода целые числа и сохранить их в
виде списка в переменной list_numbers вам необходимо написать строчку

list_numbers = list(map(int, input().split()))
Sample Input:
8 11 17
Sample Output:
36
"""

my_list = list(map(int, input().split()))
print(sum(my_list))

