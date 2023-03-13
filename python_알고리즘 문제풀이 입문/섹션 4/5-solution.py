# 그리디 알고리즘: 문제를 해결하는 단계에서 가장 최적의 것을 어떻게 찾느냐가 관건
# 보통의 그리디 문제들은 정렬 후 선택해 나가면 됨.
# 회의실 문제에서는 회의가 끝나는 시간을 기준으로 정렬해야 함. 

import sys
input = sys.stdin.readline
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))     # meeting 리스트에 튜플 형태로 시작과 끝나는 시간 대입
meeting.sort(key=lambda x:(x[1], x[0]))     # 회의가 끝나는 시간 기준으로 정렬
# 람다 함수의 매개변수인 x에 meeting 리스트의 요소 하나하나가 들어감.

et = 0     # 끝나는 시간
cnt = 0      # 가능한 회의 수
for s, e in meeting:     # 이렇게 변수 2개를 사용하면 편하다.
    if s >= et:     # 시작하는 시간이 끝나는 시간과 같거나 더 큰 경우
        et = e     # 끝나는 시간은 e
        cnt += 1     
print(cnt)