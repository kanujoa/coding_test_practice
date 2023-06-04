x, y = map(int, input().split())

# 그냥 리스트 인덱싱으로 작성해도 됨.
dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days_of_week = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
days = 0
for i in range(1, x):
    days += dic[i]
days += y
print(days_of_week[days % 7])
