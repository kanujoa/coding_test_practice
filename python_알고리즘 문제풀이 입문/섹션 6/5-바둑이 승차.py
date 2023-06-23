# 실패

c, n = map(int, input().split())     # 트럭에 태울 수 있는 최대 무게, 바둑이 마리수
w = [int(input()) for _ in range(n)]     # 바둑이들의 무게
ch = [0] * len(w)     # 해당 바둑이를 트럭에 태울 것인지의 여부를 기록하는 리스트 (태울 바둑이는 1이 됨.)
result = 0     # 가장 무거운 무게

def get_sum(result):
    _sum = 0
    for i in range(n):
        if ch[i] == 1:
            _sum += w[i]
    if result < _sum <= c:
        result = _sum

def DFS(v):     # ch 리스트에 이용할 인덱스인 v가 인자      
    if v == n:
        return
    else:
        ch[v] = 1
        get_sum(result)
        DFS(v + 1)
        ch[v] = 0
        get_sum(result)
        DFS(v + 1)
                   
DFS(0)
print(result)