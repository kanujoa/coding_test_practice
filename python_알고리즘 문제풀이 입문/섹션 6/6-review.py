# L : 트리의 레벨 (현재 뽑아서 나열한 구슬 수)
def repeated_permutation(L):
    # cnt를 전역변수 선언 해주기 (함수 밖에 있는 cnt의 값을 변화시키기 위해)
    global cnt
    # 뽑혀서 나열되어 있는 현재 구슬 수가 m과 같을 경우
    if L == m:
        # 구슬 번호 출력하기
        for num in pick:
            print(num, end=' ')
        print()
        # 순열 개수 1 증가
        cnt += 1
    else:
        # 구슬의 번호만큼 반복
        for i in range(1, n + 1):
            # 현재 순서인 L번째로 뽑히는 구슬로 i번 구슬 기록
            pick[L] = i
            # L + 1번째로 뽑힐 구슬을 위해 재귀 호출
            repeated_permutation(L + 1)

# n : 구슬의 번호 (1부터 n까지), m : 뽑아야 하는 구슬 수
n, m = map(int, input().split())
# 숫자를 뽑아서 나열하기 위한 리스트, 초깃값은 모두 0, 길이는 m
pick = [0] * m     
# 가능한 순열의 개수
cnt = 0    

repeated_permutation(0)
print(cnt)