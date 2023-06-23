def DFS(L, _sum, tsum):     # a 리스트에 접근하기 위한 index 번호, 부분집합의 합, 현재까지 판단을 했던 무게들 (트럭에 태우든 태우지 않든)
    global result     # 바깥에 있는 (전역변수의) result를 사용하는 것이라고 알려주어야 한다.
    if _sum + (total - _sum) < result:     # total-_sum은 지금까지 탐색했던 바둑이 무게 다음으로 남아 있는 바둑이 무게들의 합     
        return     # 지금까지 선택한 바둑이들의 무게 합에 total-sum을 더한 것이 result보다 작다면 더 이상 살펴볼 필요가 없다.     
    if _sum > c:     # _sum이 무게제한인 c를 넘으면 안되므로 
        return      # 아무것도 하지 않고 종료해야 함.
    if L == n:     # 말단 노드에 도착했다는 의미
        if _sum > result:
            result = _sum
    else:
        DFS(L+1, _sum+a[L], tsum+a[L])     # 인덱스와 무게의 합 증가시키기 (a 리스트의 L번째 원소를 부분집합으로 참여)
        DFS(L+1, _sum, tsum+a[L])     # _sum을 그대로 넣어주면 a 리스트의 L번째 원소를 부분집합으로 참여시키지 X

c, n = map(int, input().split())
a = [int(input()) for _ in range(n)]     # 각각의 바둑이의 무게를 담은 리스트
result = -2147000000
total = sum(a)
DFS(0, 0, 0)
print(result)