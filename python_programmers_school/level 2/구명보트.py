# 보트에는 최대 2명만이 탈 수 있음에 주목!
# 그리고 가벼운 사람들끼리 먼저 태우는 것이 최선은 아니다.
# ex) [90, 50, 70, 100, 60](limit = 140) 의 경우 가벼운 사람들끼리 먼저 태우면 (50, 60), (70), (90), (100) 으로 필요한 보트 수가 4가 되지만 무거운 사람을 먼저 태우고
# 가벼운 사람들 중에 태울 수 있는 사람이 있는지 보면 (100), (90, 50), (70, 60) 이렇게 필요한 보트 수가 3개로 최적해가 된다.

from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    
    boat = 0
    weight_sum = 0
    
    while people:
        weight_sum += people[0]
        if len(people) != 1 and weight_sum + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        boat += 1
        weight_sum = 0
        
    return boat

print(solution([86, 95, 107, 67, 38, 49, 116, 22, 78, 53], 150))


# 다른 풀이 (이진 탐색으로 풀기, 더 빠르다.)
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0     # 왼쪽 포인터
    b = len(people) - 1     # 오른쪽 포인터
    while a < b :     # a가 b보다 작을 동안만 수행
        if people[b] + people[a] <= limit :     # 무거운 사람과 가벼운 사람의 무게를 합쳐 limit 보다 적거나 같게 나갈 경우 (짝이 지어졌을 경우에만)
            a += 1     # a 한칸 옆으로
            answer += 1     # 짝이 하나 지어졌으므로 answer에 1 추가
        b -= 1     # b는 항상 1 감소 (짝이 지어지지 않았을 경우에도)
    return len(people) - answer     # 전체 인원에서 짝지은 수만큼 빼주면 보트의 수가 나온다.