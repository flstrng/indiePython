"""
01_06_E
Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров.
Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера.
Также известно, что стоимость карандаша составляет 3 рубля. Требуется определить общую стоимость покупки.

Sample Input 1:
1 1 1
Sample Output 1:
20
Sample Input 2:
23 8 76
Sample Output 2:
1021
Sample Input 3:
75 5 72
Sample Output 3:
1114

"""

X, Y, Z = map(int, input().split())
pencil_price = 3
total_pencil = pencil_price * X
total_pen = (pencil_price + 2) * Y
total_marker = (pencil_price + 9) * Z

print(total_pencil + total_pen + total_marker)
