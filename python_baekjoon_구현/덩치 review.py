# 등수를 판정할 때 자신과 다른 사람의 자신보다 더 덩치가 큰 사람의 수를 비교하는 것이 아니라 그냥 자신보다 덩치가 큰 사람의 수가 곧 등수가 된다!
# 즉, 등수 구할때 자신만 생각하면 됨!

n = int(input())     # 전체 사람의 수 
bodies = [list(map(int, input().split())) for _ in range(n)]     # 덩치 입력받기 ([몸무게, 키])
bigger = []     # 본인보다 더 큰 덩치를 가지는 사람의 수를 저장하는 리스트

for i in range(len(bodies)):     # 자신보다 더 큰 덩치를 가진 사람이 몇 명인지를 살펴볼 사람 탐색
    body = bodies[i]
    cnt = 0     # 본인보다 더 큰 덩치를 가지는 사람의 수 
    for other in bodies:     # 비교할 다른 사람을 탐색
        if body != other and body[0] < other[0] and body[1] < other[1]:     # 현재 other이 본인이 아니고 다른 사람의 키와 몸무게보다 본인의 키와 몸무게가 더 크다면
            cnt += 1
    bigger.append([cnt, i])

bigger.sort(key=lambda x:x[1])     # bigger 리스트를 입력 순서인 i를 기준으로 오름차순 정렬
for item in bigger:
    print(item[0] + 1, end=' ')     # 등수는 자신보다 더 큰 덩치의 사람의 수 + 1이므로 cnt에 1을 더하여 출력
    