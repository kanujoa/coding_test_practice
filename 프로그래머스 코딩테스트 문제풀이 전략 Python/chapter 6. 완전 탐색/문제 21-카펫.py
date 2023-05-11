# 1. 전체 카펫의 넓이(total_area) (brown 개수 + yellow 개수)를 구한다.
# 2. total_area 넓이를 만들 수 있는 width x height를 탐색한다.
# 3. 만약 (a - 2) x (b - 2)가 yellow의 수와 같으면 반복문을 중단하고 그 [a, b]를 반환한다.

def solution(brown, yellow):
    total_area = brown + yellow
    for height in range(2, total_area):
        width  = total_area // height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]
        
print(solution(10, 2))