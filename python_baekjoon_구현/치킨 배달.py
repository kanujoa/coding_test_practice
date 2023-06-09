# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
from itertools import combinations

def chicken_distance(houses, chickens):
    distances = []
    for house in houses:
        distance = 10000000
        for chicken in chickens:
            new_distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            if new_distance < distance:
                distance = new_distance
        distances.append(distance)
    return sum(distances)     # 치킨집 집합 한 세트당 도시의 치킨 거리 반환

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
houses = []
chickens_tmp = [] 

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            houses.append([i, j])
        elif maps[i][j] == 2:
            chickens_tmp.append([i, j])

distance_cases = []
for cnt in range(1, m+1):
    chickens = list(combinations(chickens_tmp, cnt))
    for chicken in chickens:
        distance_cases.append(chicken_distance(houses, chicken))

print(min(distance_cases))