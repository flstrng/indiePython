"""
02_09_F
Виды деления

Давайте при помощи F-строк выведем информацию о трех видах деления,
которые мы с вами изучили ранее: обычное деление, целочисленное и деление по остатку.

Входные данные
На вход программе поступают два целых числа, при этом гарантируется, что второе число не равно 0.
Выходные данные
Необходимо вывести результат трех видов деления первого
числа на второе в определенном формате (см. примеры ниже)

Sample Input 1:
11
5
Sample Output 1:
11 / 5 = 2.2
11 // 5 = 2
11 % 5 = 1
"""
num_1 = int(input())
num_2 = int(input())
usual_division = num_1 / num_2
integer_division = num_1 // num_2
reminder_division = num_1 % num_2

print(f"""
{num_1} / {num_2} = {usual_division}
{num_1} // {num_2} = {integer_division}
{num_1} % {num_2} = {reminder_division}
""")