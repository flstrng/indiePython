"""
02_03_02_G
Напишите программу, которая проверяет состоит
ли введенная строка целиком из заглавных букв

В качестве ответа необходимо вывести True, если
условие выполняется, во всех остальных случаях нужно вывести False

Sample Input 1:
ABRACADABRA
Sample Output 1:
True
Sample Input 2:
This Good
Sample Output 2:
False
"""

S = input()
print(S.isupper())
