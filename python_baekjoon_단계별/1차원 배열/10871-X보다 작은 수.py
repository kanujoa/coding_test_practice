import sys
input = sys.stdin.readline
n, x = map(int, input().split())
a = list(map(int, input().split()))

for num in a:
    if num < x:
        print(num, end=" ")

# 더 효율적인 풀이
# n, x = map(int, input().split())
# answer = ' '.join([i for i in input().split() if int(i) < x])     # 리스트 컴프리핸션으로 한번에 x보다 작은 수 걸러내어 리스트에 담기
# # join 시에는 공백을 한 칸 두어 정답의 형태 만들기
# print(answer, end='')
