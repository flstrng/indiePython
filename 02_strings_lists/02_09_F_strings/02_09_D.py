"""
02_09_D
Напишите программу для перевода натурального
значения секунд в значение минут определенного формата.

Sample Input 1:
99
Sample Output 1:
99 сек - это 1 мин. 39 сек.
"""
seconds = int(input())
SECONDS_IN_MINUTES = 60

print(f'{seconds} сек - это {seconds // SECONDS_IN_MINUTES} мин. {seconds % SECONDS_IN_MINUTES} сек.')
