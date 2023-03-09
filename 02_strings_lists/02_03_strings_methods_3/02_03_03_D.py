"""
02_03_03_D
Входные данные

Программе поступают последовательно три числа: значения
оттенка красного, потом зеленого и затем синего цветов.
Данные числа варьируются от 0 до 255 включительно

Выходные данные
Ваша задача закодировать оттенки цветов согласно RGB модели.
Sample Input 1:
1
2
3
Sample Output 1:
#010203
Sample Input 2:
0
255
10
Sample Output 2:
#00FF0A
"""
red = int(input())
green = int(input())
blue = int(input())

red = hex(red).strip('0x').upper().zfill(2)
green = hex(green).strip('0x').upper().zfill(2)
blue = hex(blue).strip('0x').upper().zfill(2)
S = red + green + blue

print('#', S, sep='')
