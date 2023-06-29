n = int(input())

def DFS(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return DFS(num - 1) + DFS(num - 2)

print(DFS(n))