"""
03_02_B
На вход вашей программе поступает два неравных
друг другу целых числа в отдельных строках

Ваша задача сохранить наименьшее из этих чисел
в переменную  minimum, а наибольшее - в maximum

Использовать нужно, конечно же, тернарный оператор

В качестве ответа выведите через
пробел сперва minimum , а потом maximum

Sample Input 1:
8
11
Sample Output 1:
8 11
Sample Input 2:
900
800
Sample Output 2:
800 900
"""
num1 = int(input())
num2 = int(input())
minimum = num1 if num1 < num2 else num2
maximum = num1 if num1 > num2 else num2
print(f'{minimum} {maximum}')
