"""
03_I
Требуется написать программу, определяющую, является ли
четырехзначное натуральное число N палиндромом, т.е. числом,
которое одинаково читается слева направо и справа налево.

Программа получает на вход целое положительное четырехзначное
число N и должна вывести YES, если число N является палиндромом, и NO - если не палиндром.

Sample Input 1:
4554
Sample Output 1:
YES
"""

number = list(map(int, input()))

if number == number[::-1]:
    print('YES')
else:
    print('NO')

