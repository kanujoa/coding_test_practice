# 전체 원소의 합을 total이라고 하고 부분집합의 원소의 합인 sum을 total에서 빼면 여집합의 원소의 합이 나온다. 
# 여집합의 합과 선택한 부분집합의 합이 같을 때 YES를 출력하고 종료하면 된다.

def DFS(L, sum):     # DFS 함수에 원소(L, 인덱스 번호)와 부분집합의 합(sum) 이렇게 2개의 parameter를 설정하였다.
    if sum > total // 2:     # sum이 total의 절반을 넘어가는 경우 이제 더이상 합이 같아질 가능성이 없기 때문에
        return     # return하기
    if L == n:     # 인덱스가 n과 같아질 때
        if sum == (total - sum):     # sum(부분집합의 합)과 total-sum(여집합의 합)이 같을 경우 
            print("YES")     # YES를 출력하고
            exit()     # exit로 프로그램을 종료시킴.
    else:
        DFS(L + 1, sum + a[L])     # 원소를 포함하는 경우
        DFS(L + 1, sum)     # 원소를 포함하지 않는 경우

n = int(input())
a = list(map(int, input().split()))
total = sum(a)
DFS(0, 0)     
print("NO")