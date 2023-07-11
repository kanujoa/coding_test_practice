import copy

def combination(L):
    if L == m and ch not in record:
        record.append(copy.deepcopy(ch))
        for num in pick:
            print(num, end=' ')
        print()
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                pick.append(i + 1)
                combination(L + 1)
                ch[i] = 0
                pick.pop()

n, m = map(int, input().split())
record = []
pick = []
ch = [0] * n
combination(0)
print(len(record))