# 중복을 피하기 위해 체크 리스트를 하나 만들어야 한다. (ch[i] == 0일 경우에만 상태트리가 뻗어나가야 함.)
def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                # 작업 후 (숫자를 하나 고른 후)
                ch[i] = 1
                res[L] = i
                # DFS 함수 호출
                DFS(L + 1)
                # 작업한 숫자를 (뽑은 숫자를) 다시 back하기 (안 뽑은 상태로 돌아가기)
                ch[i] = 0

n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n + 1)
cnt = 0
DFS(0)
print(cnt)