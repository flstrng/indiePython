"""
01_10_E
На вход поступает целое положительное число.
Программа должна вывести True, если у введенного числа
последняя цифра 2, в противном случае - False.
Сделать задачу необходимо без использования условного оператора.
"""
n = int(input())
print(n % 10 == 2)
