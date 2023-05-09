# 재귀는 공식을 코드로 그대로 작성한다고 생각하기!
def hanoi(n, start, to, mid, answer):
    if n == 1:     # 원판을 옮기는 과정을 진행하는 것은 n-1에서 1개씩 옮길 원판이 줄어드는 것이므로 결국은 원판 1개만 옮기는 과정으로 작아질 것이다.
        # 이해하기 어려우면, 원반 1개를 옮기는 문제의 경우 그냥 옮긴다고 생각하면 됨.
        return answer.append([start, to])     # answer에 현재 [start, to]를 추가하여 반환하기
    hanoi(n - 1, start, mid, to, answer)     # 가장 큰 원반을 제외한 n-1개의 원반들을 모두 보조 기둥에 배치하기
    answer.append([start, to])     # 원반의 이동 경로 추가
    hanoi(n - 1, mid, to, start, answer)     # 보조 기둥의 n-1개의 원반들을 모두 목적 기둥으로 옮기기

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)     # 인자는 원반의 수, 시작 기둥, 목적 기둥, 보조 기둥, 정답 배열 순임. 
    return answer