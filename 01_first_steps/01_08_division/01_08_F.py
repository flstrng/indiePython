"""
01_08_F
Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа

Sample Input 1:
123
Sample Output 1:
6
Sample Input 2:
109
Sample Output 2:
10
"""
number = int(input())
first_digit = number // 100 % 10
second_digit = number // 10 % 10
third_digit = number % 10
total = first_digit + second_digit + third_digit
print(total)

