"""
02_03_02_C
Напишите программу, которая проверяет начинается ли
введенная фраза строкой mam вне зависимости от регистра букв

В качестве ответа необходимо вывести True, если введенная
строка начинается с mam, во всех остальных случаях нужно вывести False

Sample Input 1:
MaMba
Sample Output 1:
True
Sample Input 2:
Marka
Sample Output 2:
False
Sample Input 3:
mAma
Sample Output 3:
True
"""
S = input()
print(S.lower().startswith('mam'))

