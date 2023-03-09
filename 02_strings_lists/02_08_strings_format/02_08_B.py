"""
02_08_B
Программа запрашивает у пользователя имя и фамилию,
после чего выводит приветственное сообщение в следующем формате «Здравствуйте, <фамилия> <имя>!»

Sample Input 1:
Петя
Иванов
Sample Output 1:
Здравствуйте, Иванов Петя!
"""

name = input()
family_name = input()
print('Здравствуйте, {family_name} {name}!'.format(name=name, family_name=family_name))
