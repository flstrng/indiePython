"""
01_11_C
Парты

В некоторой школе решили набрать три новых математических класса и оборудовать
кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
которое нужно приобрести для них.

Программа получает на вход три натуральных числа: количество учащихся
в каждом из трех классов (числа не превышают 1000).

Sample Input 1:
5
6
7
Sample Output 1:
10
Sample Input 2:
1
1
2
Sample Output 2:
3
"""
class1 = int(input())
class2 = int(input())
class3 = int(input())
TABLE_PUPIL = 2

class1_table = (class1 + TABLE_PUPIL - 1) // TABLE_PUPIL
class2_table = (class2 + TABLE_PUPIL - 1) // TABLE_PUPIL
class3_table = (class3 + TABLE_PUPIL - 1) // TABLE_PUPIL
print(class1_table + class2_table + class3_table)

