"""
02_01_E
Напишите программу, которая сначала считывает три фразы по очереди,
а потом воспроизводит их в обратной последовательности, каждую на отдельной строчке.

Sample Input:
Привет!
Артем
Как дела?
Sample Output:
Как дела?
Артем
Привет!
"""
phrase1 = input()
phrase2 = input()
phrase3 = input()
print(phrase3, phrase2, phrase1, sep='\n')
