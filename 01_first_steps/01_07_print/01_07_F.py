"""
01_07_F
«Сказала она!»

Давайте и мы напишем такую программу. Она принимает на вход предложение и
затем печатает его с фразой «Сказала она!» в конце определенным образом (см. примеры).
Пользуйтесь аргументом end и следите за символами, которые печатаются.

Sample Input 1:
hello
Sample Output 1:
hello - Сказала она!
Sample Input 2:
easy peasy
Sample Output 2:
easy peasy - Сказала она!
"""
sentence = input()
print(sentence, end=' - Сказала она!')