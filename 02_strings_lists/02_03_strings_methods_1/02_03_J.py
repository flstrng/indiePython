"""
02_03_J
Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
Ваша задача заменить все пробелы запятыми и вывести полученную строку.

Sample Input 1:
Smells Like Teen Spirit
Sample Output 1:
Smells,Like,Teen,Spirit
"""

phrase = input()
print(phrase.replace(' ', ','))
