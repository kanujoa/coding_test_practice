# 하나의 부분집합이 완성되면 그 집합의 여집합과 합이 같은지 비교하면 효율적으로 비교할 수 있다!
# (비교 과정을 반만 거쳐도 되기 때문!)

def DFS(v, comparision):
    if v == n:
        subset_sum = 0
        for i in range(len(ch)):
            if ch[i] == 1:
                subset_sum += elements[i]
        if subset_sum == sum(elements) - subset_sum:
            print("YES")
            exit()
        comparision += 1
        if comparision > n ** 2 // 2:
            exit()
    else:
        ch[v] = 1
        DFS(v + 1, comparision)
        ch[v] = 0
        DFS(v + 1, comparision)

n = int(input())
elements = list(map(int, input().split()))
ch = [0] * n
comparision = 0
DFS(0, 0)
print("NO")