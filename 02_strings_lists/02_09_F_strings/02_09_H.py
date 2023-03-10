"""
02_09_H
Программа запрашивает у пользователя курс доллара - вещественное число,
и также количество долларов(целое число), которое пользователь хочет приобрести.
В итоге программа должна вывести следующее сообщение:

Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
You must pay <стоимость>

Sample Input 1:
56.77
11
Sample Output 1:
Current dollar rate is 56.77. You want to buy 11 dollars
You must pay 624.47
"""
usd_rate = float(input())
usd_qnt = int(input())
payment = usd_rate * usd_qnt

print(f"""
Current dollar rate is {usd_rate}. You want to buy {usd_qnt} dollars
You must pay {payment}
""")
