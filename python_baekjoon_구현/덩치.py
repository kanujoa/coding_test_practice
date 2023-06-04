# 자신보다 더 큰 덩치의 사람이 k명이면 그 사람의 덩치 등수는 k+1이 된다!
# 즉, 자신보다 더 큰 덩치의 사람만 신경쓰면 되는 것이고 다른 사람의 등수는 전혀 신경쓰지 않아도 된다. 자신만 신경쓰면 된다.

n = int(input())
people = []

for _ in range(n):
    people.append(list(map(int, input().split())))     # 입력은 문자열이므로 int로 바꾸어 주는 것 잊지 않기! 문자열 크기 비교와 int형 크기 비교는 다르다.

i = 0
bigger = []
while i != len(people):
    cnt = 1
    for j in range(len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    people[i].append(cnt)
    i += 1

for person in people:
    print(person[-1], end=' ')