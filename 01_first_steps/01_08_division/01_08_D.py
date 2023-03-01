"""
01_08_D
Программе поступает на вход одно целое положительное число, ваша задача вывести его последнюю цифру
Sample Input 1:
123
Sample Output 1:
3
Sample Input 2:
87632
Sample Output 2:
2
"""
number = int(input())
last_digit = number % 10
print(last_digit)
