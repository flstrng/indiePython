"""
02_03_H
На вход программе поступает строка, ваша задача
вывести на экран индекс первой найденной латинской буквы a

Если такого символа в введенной строке нет, выведите -1

Sample Input 1:
banana
Sample Output 1:
1
Sample Input 2:
dog
Sample Output 2:
-1
"""

S = input()
print(S.find('a'))
