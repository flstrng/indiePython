"""03_G
На вход вашей программе поступает фраза, если в ней присутствует
слово walrus выводим текст Нашли моржа, иначе выводим Никаких моржей тут нет.

И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет

Следующие задачи можете решать без моржового оператора

Sample Input 1:
The walrus (Odobenus rosmarus) is a large flippered marine mammal with a discontinuous distribution
Sample Output 1:
Нашли моржа
Sample Input 2:
Не потерять бы в серебре еёёёёё однууууууу заветнуууююююю
Sample Output 2:
Никаких моржей тут нет
"""

if (phrase := input().find('walrus')) > 0:
    print('Нашли моржа')
else:
    print('Никаких моржей тут нет')