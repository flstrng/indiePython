"""01_06_B
Найти лучшую оценку.
Напишите программу, которая находит наилучшую оценку ученика за решение пяти контрольных работ.
Оценки всех пяти работ вводятся в одну строку, могут быть только целые числа от 1 до 100

Sample Input 1:
45 80 98 47 81
Sample Output 1:
98
Sample Input 2:
1 86 63 98 20
Sample Output 2:
98"""

work1, work2, work3, work4, work5 = map(int, input().split())
print(max(work1, work2, work3, work4, work5))
