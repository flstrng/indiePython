"""
02_08_C
Напишите программу, которая считывает целое число, и затем
сообщает какие числа будут следующим и предыдущим в определенном формате.
Пробелы, знаки препинания, заглавные и строчные буквы важны!

Sample Input:
99
Sample Output:
Для числа 99 предыдущим будет число 98.
Для числа 99 следующим будет число 100.
"""
number = int(input())
number_next = number + 1
number_previous = number - 1
print('Для числа {number} предыдущим будет число {number_previous}.\n'
      'Для числа {number} следующим будет число {number_next}.'.format(number=number, number_previous=number_previous,
                                                                       number_next=number_next))
