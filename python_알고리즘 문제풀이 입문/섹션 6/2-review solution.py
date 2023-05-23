# 트리(tree) 구조를 탐색하는 방법에는 깊이 우선 탐색 (DFS)이 있고, 넓이 우선 탐색 (BFS)가 있다.

# 전위순회 방식 (대표적)
def DFS1(v):
    if v > 7:
        return
    else:
        print(v, end=' ')     # DFS1 함수 본연의 일을 먼저 하고
        DFS1(v * 2)     # 왼쪽 자식 탐색
        DFS1(v * 2 + 1)     # 오른쪽 자식 탐색

# 중위순회 방식
def DFS2(v):
    if v > 7:
        return
    else:
        DFS2(v * 2)     # 왼쪽 자식 먼저 탐색 후
        print(v, end=' ')     # 더 나아갈 수 없으면 출력
        DFS2(v * 2 + 1)     # 그리고 오른쪽 자식 탐색

# 후위순회 방식
# 대표적으로 병합정렬에 많이 쓰인다. 왼쪽과 오른쪽 자식들을 모두 처리 뒤 병합정렬을 해야 제대로 정렬 가능
def DFS3(v):
    if v > 7:
        return
    else:
        DFS3(v * 2)     # 왼쪽 자식 먼저
        DFS3(v * 2 + 1)     # 그 다음 오른쪽 자식 탐색
        print(v, end= ' ')     # 출력은 마지막에

DFS1(1)
DFS2(1)
DFS3(1)