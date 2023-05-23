def DFS(v):
    if v == n + 1:     # 종료지점
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')     # 부분집합 원소들 출력
        print()
    else:
        ch[v] = 1     # 1은 체크가 되었다는 의미, v를 부분집합으로 사용한다.
        DFS(v + 1)
        ch[v] = 0     # 0은 체크가 안되었다는 의미, v를 부분집합으로 사용하지 않는다.
        DFS(v + 1)


n = int(input())
ch = [0] * (n + 1)     # 원소를 사용했냐 사용하지 않았냐 체크하는 변수
DFS(1)