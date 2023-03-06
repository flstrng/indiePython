"""
02_01_J
Программа принимает на вход три символа через пробел в одну строку.
Необходимо вывести код каждого символа при помощи функции ord в определенном формате.

Sample Input 1:
A , y
Sample Output 1:
Simvol code A is 65.
Simvol code , is 44.
Simvol code y is 121.
"""
symbol1, symbol2, symbol3 = map(str, input().split())
print('Simvol code', symbol1, 'is', ord(symbol1), end=".\n")
print('Simvol code', symbol2, 'is', ord(symbol2), end=".\n")
print('Simvol code', symbol3, 'is', ord(symbol3), end=".\n")


