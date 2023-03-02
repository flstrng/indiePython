"""
01_08_G
Выиграть в лотерею

У Олега в банке есть n евро. Он хочет снять всю сумму наличными.
Номиналы евро купюр равны 1, 5, 10, 20, 100. Какое минимальное число
купюр должен получить Олег после того, как снимет все деньги?
На вход программе поступает одно положительные целое число n.

Sample Input 1:
125
Sample Output 1:
3
Sample Input 2:
43
Sample Output 2:
5
Sample Input 3:
10000000
Sample Output 3:
100000

"""
n = int(input())

hundreds = n // 100
twenties = n % 100 // 20
tens = n % 20 // 10
fives = n % 10 // 5
units = n % 5 // 1

banknotes = hundreds + twenties + tens + fives + units

print(banknotes)
