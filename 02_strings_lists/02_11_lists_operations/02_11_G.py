"""
02_11_G
Программа получает на вход список из целых чисел.
Ваша задача найти среднее арифметическое введенного списка чисел

Sample Input 1:
8 10
Sample Output 1:
9.0
"""

numbers = list(map(int, input().split()))
print(sum(numbers) / len(numbers))

