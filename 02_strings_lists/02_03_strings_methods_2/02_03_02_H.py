"""
02_03_02_H
Напишите программу, которая проверяет состоит ли
введенная строка целиком из строчных букв

В качестве ответа необходимо вывести True, если условие
выполняется, во всех остальных случаях нужно вывести False

Sample Input 1:
opportunity
Sample Output 1:
True
Sample Input 2:
Salary
Sample Output 2:
False
"""
S = input()
print(S.islower())
