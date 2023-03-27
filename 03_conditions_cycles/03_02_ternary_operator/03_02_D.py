"""
03_02_D
Если расположить рядом два магнита, они начинают
взаимодействовать друг с другом. При этом одинаковые
магнитные полюса (север/север или юг/юг) отталкиваются
друг от друга, в то время как разные магнитные полюса (север/юг) притягиваются друг к другу.

Ваша программа получает два значения в разных строках - полярности
магнитов, которые могут иметь значения либо N ( север) либо S (юг)

Ваша задача сохранить в переменную experiment строку Притягиваются,
если магниты имеют разную полярность,
в противном случае сохраните строку Отталкиваются

В качестве ответа необходимо вывести переменную experiment

Sample Input:
N
N
Sample Output:
Отталкиваются
"""
pole1 = input()
pole2 = input()
experiment = 'Притягиваются' if pole1 != pole2 else 'Отталкиваются'
print(experiment)
