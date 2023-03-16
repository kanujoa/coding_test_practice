# 실패...

l = int(input())     # 창고 가로의 길이
box = list(map(int, input().split()))     # 각 열의 상자 높이(상자 개수)
m = int(input())     # 높이 조정 횟수

box.sort(reverse=True)     # 박스 개수가 많은 순으로 정렬
lt = 0
rt = l-1

for _ in range(m):
    if box[lt] == box[lt+1]:
        lt += 1
    if box[rt] == box[rt-1]:
        rt -= 1
    box[lt] -= 1
    box[rt] += 1
print(max(box) - min(box))