"""
03_D
Программа получает на вход три натуральных числа A, B и C через пробел.

Вам необходимо вывести YES в том случае, если A + B = C и вывести NO в противном случае.

Sample Input 1:
4 5 9
Sample Output 1:
YES
"""

A, B, C = map(int, input().split())
if A + B == C:
    print('YES')
else:
    print('NO')

