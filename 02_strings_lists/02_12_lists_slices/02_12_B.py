"""
02_12_B
Программа получает на вход список целых чисел и ваша
задача вывести срез списка с третьего элемента по пятый включительно.

Sample Input:
7 8 9 10 11 12 13
Sample Output:
[9, 10, 11]
"""
my_list = list(map(int, input().split()))
print(my_list[2:5])