def DFS(v):     # v는 노드 번호
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i] = 0
                path.pop()

n, m = map(int, input().split())     # 정점의 수 n, 간선의 수 m
g = [[0] * (n + 1) for _ in range(n + 1)]     # 그래프 정보를 기록할 이차원 리스트
ch = [0] * (n + 1)     # 해당 노드가 사용되었는지를 체크하는 리스트
for i in range(m):
    a, b = map(int, input().split())     # 간선으로 연결된 노드 입력받기
    g[a][b] = 1     # g에다 기록하기 (방향 그래프이므로 주어진 노드에서 한 방향(행 -> 열)에만 기록해야 함.) 
cnt = 0
path = []     # 경로를 기록할 리스트
ch[1] = 1     # 1번 노드는 무조건 방문하게 되어 있으므로 미리 체크하고 시작
path.append(1)
DFS(1)
print(cnt)