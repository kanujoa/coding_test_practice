# 1. 주어진 직선에서 교점을 구한다. (문제 설명에서 주어진 교점 공식으로)
# combinations를 사용하지 않고 line[i]의 직선과 i보다 인덱스가 큰 직선들을 2중 for문을 통해 짝을 짓는 방식
# 으로 풀이한다.
def solution(line):
    pos, answer = [], []
    n = len(line)

    x_min = y_min = int(1e15)     # 초깃값을 큰 수인 int(1e15) (== 100000, 입력으로 들어가는 값 중 가장 큰 값)으로 설정
    x_max = y_max = -int(1e15)     # 초깃값을 작은 수인 -int(1e15) (== -100000, 입력으로 들어가는 값 중 가장 작은 값)으로 설정

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if a * d == b * c: continue     # a * d와 b * c가 같으면 두 직선은 평행이므로 아래에 있는 코드 실행 X
            
            # 여기서부터는 a * d != b * c 인 경우만 실행됨.
            x = (b * f - e * d) / (a * d - b * c)     # 교점의 x좌표
            y = (e * c - a * f) / (a * d - b * c)     # 교점의 y좌표
            
            # 2. 교점이 정수인지를 검사하고 정수라면 해당 교점을 변수로 만들어서 저장한다.
            if x == int(x) and y == int(y):
                # 나누기를 해서 만들어진 실수는 부동소수점 표시의 한계로 소수점끼리 더하면 값이 바뀐다.
                # ex) 이진법에서, 1/10은 무한히 반복되는 소수 
                # float끼리 적극적으로 계산해서 두 값을 비교하는 문제가 나오면, 내장 라이브러리인 fractions나 decimal 라이브러리를 사용해서 오차를 제거한 상태에서
                # 값을 비교해야 한다.
                # 그리고 int() 함수로 정수로 변환 시에는 소수점이 버려지는데 예상과는 다른 결과가 나올 수도 있다. 
                x = int(x)
                y = int(y)
                pos.append([x, y])
                # 3. 교점을 모두 표현할 수 있는 최소한의 사각형을 알아낸다.
                # 교점인 좌표들 중 영점으로부터 가장 멀리 떨어져 있는 좌표를 찾아 최댓값, 최솟값을 알아내면 된다.
                if x_min > x: x_min = x
                if y_min > y: y_min = y
                if x_max < x: x_max = x
                if y_max < y: y_max = y

    # 모든 교점을 *로 찍어서 표현한다.
    x_len = x_max - x_min + 1     # 최소 사각형의 x축 안의 요소 개수
    y_len = y_max - y_min + 1     # 최소 사각형의 y축 안의 요소 개수
    coord = [['.'] * x_len for _ in range(y_len)]     # 우선, 최소 사각형을 모두 '.'으로 초기화함.

    for star_x, star_y in pos:     # star_x는 교점의 x좌표, star_y는 교점의 y좌표
        # 최소 사각형에서 가장 작은 x좌표(x_min)가 0보다 작으면 star_x + abs(x_min) 값을 nx에 할당, x좌표(x_min)가 0보다 크거나 같으면 star_x - x_min 값을 nx에 할당
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min     
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min     # 위와 같은 방식
        # nx와 ny는 별을 찍기 위한 인덱스를 작성하기 위해 만들었다. --> coord[ny][nx]의 방식으로 별을 찍을 위치를 정함.
        coord[ny][nx] = '*'     

    # 5. 배열을 거꾸로 뒤집어 반환하기
    # coords의 앞쪽에는 y좌표가 음수인 *이 찍히고, coords의 뒤쪽에는 y좌표가 양수인 *이 찍힌다. 따라서 배열을 뒤집어 반환해야 한다. 
    for result in coord: answer.append(''.join(result))

    return answer[::-1]