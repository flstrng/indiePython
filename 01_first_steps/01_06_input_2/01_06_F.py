"""
Два бандита

Бандиты Гарри и Ларри отдыхали на природе. Решив пострелять, они выставили на бревно несколько
банок из-под кока-колы (не больше 10). Гарри начал простреливать банки по порядку, начиная
с самой левой, Ларри — с самой правой. В какой-то момент получилось так, что они одновременно
прострелили одну и ту же последнюю банку.

Гарри возмутился и сказал, что Ларри должен ему кучу денег за то, что тот лишил
его удовольствия прострелить несколько банок. В ответ Ларри сказал, что Гарри
должен ему еще больше денег по тем же причинам. Они стали спорить кто кому сколько
должен, но никто из них не помнил сколько банок было в начале, а искать простреленные
банки по всей округе было неохота. Каждый из них помнил только, сколько банок прострелил он сам.

Определите по этим данным, сколько банок не прострелил Гарри и сколько банок не прострелил Ларри.
Sample Input 1:
4 7
Sample Output 1:
6 3
Sample Input 2:
5 3
Sample Output 2:
2 4
Sample Input 3:
2 7
Sample Output 3:
6 1
"""

harry_cans_shot, larry_cans_shot = map(int, input().split())
shot_middle = (harry_cans_shot + larry_cans_shot) - 1
hary_missed = shot_middle - harry_cans_shot
larry_missed = shot_middle - larry_cans_shot
print(hary_missed, larry_missed)


