"""
02_03_K
На вход программе поступает строка, ваша задача удалить из нее все символы w и z.
Учитываем только маленькие буквы

Sample Input:
what's up?
Sample Output:
hat's up?
"""
S = input()
print(S.replace('w', '').replace('z', ''))
