n, m = map(int, input().split())     # n = 바구니의 개수, m = 바구니 순서 회전 횟수
basket = [a for a in range(1, n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())     # i = 시작 바구니, j = 끝 바구니, k = 회전 기준 바구니
    for _ in range(k-i):
        basket.insert(j-1, basket.pop(i-1))     # pop 메서드 안에는 요소가 아닌 '인덱스'!!! 를 작성해 주어야 한다.
for x in basket:
    print(x, end=' ')

# 리스트 슬라이싱과 연산을 활용하여 해결할 수도 있다.
# N, M = map(int, input().split())
# B = [i for i in range(1, N + 1)]
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     B[i-1:j] = B[k-1:j] + B[i-1:k-1]     --> 시작과 끝 범위에서만 슬라이싱으로 mid 기준으로 나누고 그것을 +해주면 된다.
# print(*B)