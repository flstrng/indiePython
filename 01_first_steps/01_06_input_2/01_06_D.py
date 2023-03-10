"""
01_06_D
Журавлики

Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Входные данные.
Поступает одно натуральное число S – общее количество сделанных журавликов.

Выходные данные.
В единственную строку нужно вывести три числа, разделенных пробелами –
количество журавликов, которые сделал каждый ребенок (Петя, Катя и Сережа).

Sample Input 1:
6
Sample Output 1:
1 4 1
Sample Input 2:
24
Sample Output 2:
4 16 4
Sample Input 3:
60
Sample Output 3:
10 40 10
"""
S = int(input())  # общее количество сделанных журавликов
"""
# Петя + Сережа + 2(Петя + Сережа) = общее количество сделанных журавликов
--> 6 * Петя = общее количество. а так как Петя и Сережа сделали одинаково
"""
petya = int(S / 6)
serezha = int(S / 6)
katya = S - petya - serezha
print(petya, katya, serezha)
