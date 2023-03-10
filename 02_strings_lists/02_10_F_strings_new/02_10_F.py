"""
02_10_F
Вам необходимо подправить код ниже так, чтобы он выравнивал

первый print по центру
второй print по правому краю
третий print по левому краю
Количество знаков для выравнивания 20 символов, знак разделителя - &

Sample Input 1:
hello
Sample Output 1:
|&&&&&&&hello&&&&&&&&|
|&&&&&&&&&&&&&&&hello|
|hello&&&&&&&&&&&&&&&|
"""

text = input()
print(f"|{text:&^20}|")
print(f"|{text:&>20}|")
print(f"|{text:&<20}|")
