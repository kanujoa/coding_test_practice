def DFS(i, _sum):     # elements에서 사용할 인덱스와 포함할 원소를 누적할 _sum이 인자로 들어감
    if _sum > total_sum // 2:     # 현재까지 포함된 원소들의 합이 모든 원소의 합의 절반보다 클 경우
        return     # 과정 종료
    elif i == n:     # 모든 원소들을 다 돌고,
        if _sum == (total_sum - _sum):     # 뽑은 원소들의 합이 나머지 원소들의 합과 같은 경우
            print("Yes")     # Yes 출력 후
            exit()     # 프로그램 자체를 종료
    else:
        DFS(i + 1, _sum + elements[i])     # 현재 i번째 원소를 포함하는 경우 
        DFS(i + 1, _sum)     # 현재 i번째 원소를 포함하지 않는 경우

n = int(input())     # 집합의 원소의 개수
elements = list(map(int, input().split()))     # 집합을 이루는 원소들
total_sum = sum(elements)     # 전체 원소의 합
DFS(0, 0)     # 인덱스는 0부터 하나씩 증가, 원소의 합도 0으로 초기화
print("No")     # 위 DFS 함수에서 프로그램 종료(exit())가 이루어지지 않은 경우 실행됨