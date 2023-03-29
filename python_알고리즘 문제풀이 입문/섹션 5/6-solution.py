from collections import deque
n, m = map(int, input().split())
# pos: 환자 번호(번째), val: 환자의 위험도
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    # x는 pop된 cur을 제외한 Q의 튜플 요소, 그 요소들의 위험도(x[1]) 중 cur의 위험도(cur[1])보다 높은 것이 하나라도 있다면(any 함수) 아래의 코드 실행
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:     # cur[1]이 가장 높은 위험도일 경우
        cnt += 1
        if cur[0] == m:     # cur 환자의 번호가 m이라면
            break     # 반복문 종료
print(cnt)    