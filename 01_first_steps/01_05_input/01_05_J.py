hours1 = int(input())
min1 = int(input())
sec1 = int(input())
hours2 = int(input())
min2 = int(input())
sec2 = int(input())

total_sec_1 = hours1 * 3600 + min1 * 60 + sec1
total_sec_2 = hours2 * 3600 + min2 * 60 + sec2
print(total_sec_2 - total_sec_1)
