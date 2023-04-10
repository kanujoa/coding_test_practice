def DFS(x):
    if x == 0:     # x가 0일 때 재귀함수의 종료를 위해
        return     # return만 딱 써놓으면 함수 종료의 의미로 받아들인다.
    else:
        DFS(x // 2)
        print(x % 2, end='')
n = int(input())
DFS(n)