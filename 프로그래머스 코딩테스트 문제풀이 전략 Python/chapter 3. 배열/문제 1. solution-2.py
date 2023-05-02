def solution(line):
    meet = list()     # meet는 교점을 담을 리스트
    x_max = y_max = -float('inf')     # x_max와 y_max는 가장 작은 값으로 초기화
    x_min = y_min = float('inf')     # float이 문자열 'inf'를 실수형으로 변환하였다. --> x_min과 y_min은 가장 큰 값으로 초기화

    # 1. 주어진 직선에서 교점을 알아낸다.
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            # 계산 실수를 방지하기 위해 괄호를 사용했다.
            if ((a * d) - (b * c)) == 0:
                continue
    
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            # 2. 그 중 정수 교점만 기억하고, x축에서의 최소, 최대와 y축에서의 최소, 최대의 크기를 알아낸다.
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                meet.append([x, y])
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)

    # 3. 교점을 모두 표현할 수 있는 최소한의 사각형을 알아낸다.
    width = abs(x_max - x_min) + 1    # 최소 사각형의 가로의 길이 ([] 하나에 들어 있는 '.'의 수)
    height = abs(y_max - y_min) + 1   # 최소 사각형의 세로의 길이 (answer 리스트에 들어 있는 리스트의 수)
    answer = [['.'] * width for _ in range(height)]
    # 4. 모든 교점을 *로 찍어서 반환한다.
    # 이전 풀이에서 마지막에 결과를 역순으로 출력해 주었는데, 이를 여기서는 역순 정렬로 미리 처리함. (y좌표에 -를 붙인 값을 기준으로 오름차순 정렬함.))
    # 정렬의 시간 복잡도(O(nlogn)를 고려하면 이전 풀이보다 느려지는 것은 맞지만 실수할 가능성을 낮췄다.
    meet = sorted(meet, key=lambda i: -i[-1])     

    for x, y in meet:
        ny = y_max - y     # 현재 y는 원래 교점의 부호와 반대로 되어 있다. y_max에서 y를 빼면 무조건 양수가 나오고, 그것이 점을 찍어야 할 index가 된다.
        nx = x - x_min     # x는 그대로 x이다. nx 역시 점을 찍어야 할 index가 된다.
        answer[ny][nx] = '*'

    return list(map(''.join, answer))      # answer 리스트에 map 함수를 사용하여 answer 안의 모든 리스트에 join을 적용하고, 그것을 새로운 리스트에 담았다.