def DFS(L, sum):     # L: 현재 동전의 개수(현재 트리의 level), 동전 금액의 합
    global res     # 6번 줄에서 res를 참조하기 때문에 res를 전역변수로 만들어야 함.
    if L > res:     # res보다 더 깊게 탐색할 필요가 없음.
        return
    if sum > m:     # 금액의 합이 거스름돈보다 커지면
        return     # 함수 그냥 종료
    if sum == m:     # 금액의 합이 거스름돈과 같아지면 
        if L < res:     # L이 이전의 동전의 최소 수인 res보다 작으면 
            res = L     # res를 L로 업데이트
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])
    

n = int(input())     # 동전의 종류의 수
a = list(map(int, input().split()))     # 동전의 종류 
m = int(input())     # 거스름돈
res = 2147000000     # 결과로 출력할 동전의 최소 수
a.sort(reverse=True)     # 내림차순 정렬을 한 이유는 전위순회에서 1부터 시작하여 거스름돈 15원을 채우려면 작업을 매우 많이 반복해야 하므로 큰것부터 먼저 적용하여 깊이를 줄이기 위해서
DFS(0, 0)
print(res)