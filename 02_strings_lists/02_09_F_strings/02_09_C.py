"""
02_09_C
77 лет

Напишите программу, которая запрашивает имя пользователя
и его год рождения. Программа должна вывести на экран сообщение
"<Имя пользователя>, вам исполнится 77 лет в <год>"

Sample Input 1:
Геннадий
1990
Sample Output 1:
Геннадий, вам исполнится 77 лет в 2067
Sample Input 2:
Rich
2010
Sample Output 2:
Rich, вам исполнится 77 лет в 2087
"""
name = input()
birth_year = int(input())

print(f'{name}, вам исполнится 77 лет в {birth_year + 77}')