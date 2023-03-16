"""
03_F
Таможня

На момент написания текста из РФ можно было вывозить не более 10000$
или эквивалент в другой валюте. При превышении этой суммы необходимо составлять декларацию.

Давайте представим, что сумму выше 10000 долларов таможня забирает себе и вам останется только 10000$.

Давайте напишем такую программу, которая будет принимать целое положительное число -
сумма в долларах. Если она не превышает 10000$, то выводим текст Сумма <значение> не превышает лимит, проходите

Если сумма превышает 10000$ выводим текст Ого! <значение>! Куда вам столько? Мы заберем <разница>

И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет

Sample Input 1:
500
Sample Output 1:
Сумма 500 не превышает лимит, проходите
Sample Input 2:
12000
Sample Output 2:
Ого! 12000! Куда вам столько? Мы заберем 2000
"""

if (money := int(input())) <= 10000:
    print(f'Сумма {money} не превышает лимит, проходите')
else:
    print(f'Ого! {money}! Куда вам столько? Мы заберем {money - 10000}')
