a = int(input())  # считываем 3 целых числа
b = int(input())
c = int(input())

variant1 = a + b + c  # все возможные варианты вычислений
variant2 = a + b * c
variant3 = a * b + c
variant4 = (a + b) * c
variant5 = a * (b + c)
variant6 = a * b * c

print(max(variant1, variant2, variant3, variant4, variant5, variant6))
