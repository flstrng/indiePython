"""
02_03_02_L
На вход программе поступает натуральное число, которое не превосходит значение 109

Ваша задача вывести данное число так, чтобы вывод занимал 10 разрядов.
Если у числа не хватает разрядов, необходимо добавлять вперед незначащие нули.

Sample Input 1:
99
Sample Output 1:
0000000099
"""
num = input()
print(num.zfill(10))
