# 모든 경우의 수의 합을 구한 후 확인하는 방식이 아닌 solution의 방식을 사용하여 YES 또는 NO를 출력하게 하였다.

def DFS(i):
    if i == n:
        sum = 0
        for j in range(n):
            if ch[j] == 1:
                sum += element[j]
        if sum == (total - sum):
            print("YES")
            exit()
    else:
        ch[i] = 1
        DFS(i + 1)
        ch[i] = 0
        DFS(i + 1)

n = int(input())
element = list(map(int, input().split()))
total = sum(element)
ch = [0] * n
if DFS(0) != "YES":
    print("NO")