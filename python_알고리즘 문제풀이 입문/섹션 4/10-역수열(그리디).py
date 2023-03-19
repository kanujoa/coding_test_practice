# 역수열을 이용해 원래 수열을 구해야 한다.
n = int(input())
seq = list(reversed(list(map(int, input().split()))))     # 역수열 입력 후 뒤집기 (n부터 1까지 차례대로 매칭 가능)
s = sorted(list(range(1, n+1)), reverse=True)     # n+1부터 1까지 내림차순 정렬된 리스트 s
res = sorted(list(range(1, n+1)))     # 정답이 될 리스트 (1부터 n까지 오름차순 정렬된 리스트)

for i in range(1, n):
    p = res.index(s[i])     # res에서의 현재 숫자의 인덱스
    res.insert(p+seq[i], res.pop(p))     # res 리스트에서 현재 숫자의 위치에서 seq[i]를 더한 위치로 움직임(삽입)
for x in res:
    print(x, end=" ")

# 역수열 구하는 법
# for i in range(n+1):
#     cnt = 0
#     for j in range(seq.index(s[i])):
#         if seq[j] > s[i]:
#             cnt += 1
#     s[i] = cnt 
# for x in s:
#     print(x, end=" ")   