# 그래프 : 노드와 간선의 집합
# 가중치 방향 그래프 : 간선의 값과 방향이 설정되어 있는 경우
# 무방향 그래프는 양방향이 가능.

# 무방향 그래프의 경우
# 입력 예시 
# 5 5     --> 노드 번호 (노드는 1번부터 5번까지 존재), 간선의 개수
# 1 2     --> 여기서부터는 간선의 정보 (몇 번 노드와 몇 번 노드가 간선으로 연결되어 있는지에 대한 정보)
# 1 3
# 2 4
# 3 4
# 4 5

n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1     # 양방향이므로 g[a][b]와 g[b][a] 모두 기록해줌. (대칭)
    g[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()


# 가중치 방향 그래프의 경우 (문제에 나와 있음.)
n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    g[v1][v2] = w     # 방향이 정해져 있으므로 한 방향에만 기록해줌.

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()