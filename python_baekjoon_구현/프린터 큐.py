from collections import deque

t = int(input())     # 주어지는 테스트 케이스 개수

for _ in range(t):
    n, m = map(int, input().split())     # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 큐에 몇 번째에 놓여 있는지
    importance = list(map(int, input().split()))    # n개의 문서의 중요도
    document = deque()
    for a, b in enumerate(importance):     # a는 importance의 index값, b는 중요도값
        document.append([b, a])     # 중요도값 기준으로 판단하기 쉽게 하기 위해 b를 앞에 위치시킴.
    while len(document) != 0:
        _max = max(document)[0]
        if document[0][0] < _max:
            document.append(document.popleft())
        else:
            if document[0][1] == m:
                print(n - len(document) + 1)
                break
            else:
                document.popleft()