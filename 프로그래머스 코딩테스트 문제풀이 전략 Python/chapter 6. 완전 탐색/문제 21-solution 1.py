# 공식을 모른다고 가정하고 풀기
def solution(brown, yellow):
    # 1. 전체 넓이를 구한다.
    grid = brown + yellow
    # 2. 전체 넓이를 만들 수 있는 가로와 세로의 길이를 구한다.
    for n in range(3, int(grid ** 0.5) + 1):     # 최소 길이부터 정사각형까지 (카펫의 세로의 길이는 가로의 길이와 같거나 작아야 한다.)
        if grid % n != 0: continue
        m = grid // n
        if (n - 2) * (m - 2) == yellow:
            return [m, n]