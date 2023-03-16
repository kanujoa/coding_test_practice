l = int(input())     # 창고 가로 길이
box = list(map(int, input().split()))     # 각 열에에서의 상자 높이(상자 개수)
m = int(input())     # 높이 조정 횟수

for _ in range(m):
    big = max(box)
    small = min(box)
    box[box.index(big)] = big - 1
    box[box.index(small)] = small + 1
print(max(box) - min(box))