n, m = map(int, input().split())     # 구슬의 번호 수, 뽑을 구슬의 수

def DFS(L):
    global cnt
    if L == m:
        cnt += 1
        for num in pick:
            print(num, end=' ')
        print()
    else:
        for i in range(n):
            if beads[i] != 1:
                beads[i] = 1
                pick.append(i + 1)
                DFS(L + 1)
                beads[i] = 0
                pick.pop()

cnt = 0
beads = [0] * n     # beads 리스트는 어느 구슬이 선택되었는지를 체크하는 리스트이다. 그냥 순열에서는 중복 선택이 허용되지 않으므로 이를 확인하기 위해 작성하였다.
pick = []     # pick 리스트를 따로 만든 이유는 순열은 단순히 어느 구슬이 뽑혔는지 뿐만 아니라 어느 순서로 뽑혔는지까지 고려해야 하기 때문에 순서대로 구슬을 담기 위해서이다.
DFS(0)
print(cnt)