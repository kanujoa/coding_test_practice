def DFS(i):
    if i == n:
        for idx in range(n):
            if ch[idx] == 1:
                print(idx + 1, end=' ')
        print()
    else:
        ch[i] = 1
        DFS(i + 1)
        ch[i] = 0
        DFS(i + 1)

# 입력받기, 필요한 리스트 세팅해놓기
n = int(input())
ch = [0] * n     # 각 인덱스 + 1의 숫자가 사용되었는지 여부를 체크하는 체크 리스트
DFS(0)     # 인덱스는 0부터 시작