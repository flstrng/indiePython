"""
02_03_02_F
Напишите программу, которая проверяет состоит
ли введенная строка целиком из десятичных цифр

В качестве ответа необходимо вывести True,
если условие выполняется, во всех остальных случаях нужно вывести False

Sample Input 1:
12345
Sample Output 1:
True
Sample Input 2:
K9
Sample Output 2:
False
"""
S = input()
print(S.isdigit())