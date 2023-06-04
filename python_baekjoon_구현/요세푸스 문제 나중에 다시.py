from collections import deque
n, k = map(int, input().split())     # 사람의 수, 제거될 번째

people = deque(i for i in range(1, n+1))
result = []
while len(people) >= k:
    for _ in range(k-1):
        people.append(people.popleft())
    result.append(people.popleft())
if len(result) != 0:
    for person in people:
        result.append(person)
print('<' + str(result)[1:-1] + '>')