"""
01_07_E
В этой задаче мы сами будем решать, какое значение использовать в качестве разделителя в параметре sep

Программа принимает на вход строку - разделитель, вам необходимо распечатать числа от 1 до 5,
выводя между ними введенный разделитель

Sample Input 1:
!
Sample Output 1:
1!2!3!4!5
Sample Input 2:
$
Sample Output 2:
1$2$3$4$5
Sample Input 3:
BoB
Sample Output 3:
1BoB2BoB3BoB4BoB5
"""
separator = input()
print(1, 2, 3, 4, 5, sep=separator)
