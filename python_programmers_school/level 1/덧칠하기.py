# 맨 마지막에 칠해진 구간의 번호에만 집중하여 풀면 되는 그리디 문제이다.
# 리스트의 요소를 순차적으로 하나씩 돌면서 해결해 나간다. (오름차순 정렬은 이미 되어있으므로 sort 할 필요 없다.)

def solution(n, m, section):
    result = 0     # 최소로 칠한 횟수
    num = 0     # 마지막으로 칠해진 번호
    for s in section:     # section의 요소 하나씩 순회
        if s > num:     # 만약 s가 num보다 크면 s는 덧칠되지 않은 부분이므로
            num = s + m - 1     # num은 s + m - 1로 업데이트
            result += 1     # 덧칠 횟수 1 증가
    return result 


print(solution(8, 4, [2, 3, 6]))