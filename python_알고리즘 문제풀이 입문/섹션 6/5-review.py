# i : w 리스트에 접근하기 위한 index
# _sum : 현재까지 승차한 바둑이들의 무게 합
# total_sum : 현재 승차한 바둑이의 바로 뒤 순서부터 모든 바둑이 무게의 합
def DFS(i, _sum, total_sum):    
    global answer
    # 앞으로 포함될 가능성이 있는 바둑이들의 무게들을 모두 현재 _sum에 더했을 때 현재까지의 최대 무게보다 적으면 더 살펴볼 필요 X
    if _sum + (total - total_sum) < answer:     
        return
    # 현재 승차한 바둑이들의 무게가 제한을 넘을 경우
    elif _sum > c:     
        return
    # 마지막 무게까지 다 돌았을 경우 (트리에서 말단 노드에 도착하였을 때)
    elif i == n:     
        # 바둑이 무게의 합이 현재 탑승 가능 최대 무게보다 더 클 경우
        if _sum > answer:
            answer = _sum
    else:
        # 현재 순서의 바둑이를 승차시킬 경우
        DFS(i + 1, _sum + w[i], total_sum + w[i])
        # 현재 순서의 바둑이를 승차시키지 않을 경우
        DFS(i + 1, _sum, total_sum + w[i])
        

c, n = map(int, input().split())     # c : 트럭에 태울 수 있는 최대 무게, n : 철수가 데리고 있는 바둑이들의 수
w = [int(input()) for _ in range(n)]     # 바둑이들의 무게
answer = 0     # 철수가 트럭에 태울 수 있는 가장 무거운 무게
total = sum(w)     # 모든 바둑이들의 무게
DFS(0, 0, 0)
print(answer)