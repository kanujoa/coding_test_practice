def permutation(L):
    global cnt
    if L == m:
        for num in pick:
            print(num, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            # ch 리스트의 i번째 값이 0일 경우는 i가 뽑히지 않은 숫자임을 의미한다.
            if ch[i] == 0:
                # 숫자를 하나 고른 후 (그 숫자는 i이다.)
                pick[L] = i
                # ch 리스트의 해당 숫자에 해당하는 번째에 1 표시
                ch[i] = 1
                # permutation 함수 재귀 호출
                permutation(L + 1)
                # 뽑은 숫자를 다시 back하여 안 뽑은 상태로 돌아가기 (다음 i를 뽑기 위해)
                ch[i] = 0

n, m = map(int, input().split())
pick = [0] * m
ch = [0] * (n + 1)     # 중복을 피하기 위해 체크 리스트를 하나 만듦. 
cnt = 0
permutation(0)
print(cnt)