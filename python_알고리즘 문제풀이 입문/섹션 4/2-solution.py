# 앞서 배운 '이분검색'은 '결정 알고리즘'을 위해 사용한다.
# 결정 알고리즘으로 풀 수 있는 문제들은 답이 특정 범위 안에 있다는 것을 바로 볼 수 있다.
# ex) 1000이라는 입력이 주어졌을 때, 1000의 mid는 500이다. 500cm로 N개의 랜선을 모두 나누어 개수를 세면 총 M개의 랜선이 생성되는지
# 확인하는 코드를 짜면 된다.  

import sys
input = sys.stdin.readline

def Count(len):     # mid의 길이씩 잘라서 만들 수 있는 랜선 토막의 개수를 구하는 함수
    cnt = 0
    for x in Line:
        cnt += x // len
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)     # 기존 값인 largest와 새로운 값인 tmp를 비교해서 더 큰 값을 largest 변수에 넣어줌.
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2     # mid = 잘라서 만들어진 랜선의 길이
    if Count(mid) >= n:      # 랜선 개수가 n보다 크거나 같으면 res가 될 수 있는 길이이다.
        res = mid
        lt = mid + 1
    else:     # 랜선 개수가 n보다 작을 경우 (랜선 토막의 개수가 더 많아져야 하므로 토막낼 길이가 더 짧아져야 한다.)
        rt = mid - 1     # mid를 더 작은 값들 중에서 찾아본다.
print(res)
        
        