"""
01_10_J
На вход поступают три целых числа - стороны треугольника.
Необходимо вывести True, если данные стороны образуют
равнобедренный треугольник, в противном случае - False.
Сделать задачу необходимо без использования условного оператора.
"""
ab, bc, ac = map(int, input().split())
print(ab == bc or bc == ac or ab == ac)
