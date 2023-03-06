"""
02_02_F
Программа получает на вход строку. Ваша задача вывести
все символы этой строки, которые имеют нечетные индексы

Sample Input:
Donald Trump
Sample Output:
oadTup
"""
phrase = input()
print(phrase[1::2])
