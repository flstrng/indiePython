"""
Даны три целых числа, каждое записано в отдельной строке.

Нужно вывести значение наибольшего из данных чисел

Примечание: используйте только условный оператор, функцией max пользоваться нельзя

Sample Input 1:
5
7
21
Sample Output 1:
21
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2:
    if num1 > num3:
        print(num1)
if num2 > num1:
    if num2 > num3:
        print(num2)
if num3 > num1:
    if num3 > num2:
        print(num3)

