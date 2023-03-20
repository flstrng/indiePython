"""
03_K
Счастливый билет

Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером
(иногда и с незначащими нулями), где сумма первых трех цифр равна
сумме последних трех. Т.е.
билеты с номерами 385916 и 2011 – счастливые, т.к. 3+8+5=9+1+6 и 0+0+2=0+1+1.
Вам требуется написать программу, которая проверяет «счастливость» билета.

Программа получает на вход одно целое число N (0 ≤ N < 10^6) и
должна вывести «YES», если билет с номером N счастливый и «NO» в противном случае.

Sample Input 1:
385916
Sample Output 1:
YES
Sample Input 3:
5203
Sample Output 3:
YES
"""
ticket_number = list(map(int, input()))
zero = [0]
if 6 - len(ticket_number) != 0:
    ticket_number = (zero * (6 - len(ticket_number))) + ticket_number
    if ticket_number[0] + ticket_number[1] + ticket_number[2] == ticket_number[3] + ticket_number[4] + ticket_number[5]:
        print('YES')
    else:
        print('NO')
else:
    if ticket_number[0] + ticket_number[1] + ticket_number[2] == ticket_number[3] + ticket_number[4] + ticket_number[5]:
        print('YES')
    else:
        print('NO')
