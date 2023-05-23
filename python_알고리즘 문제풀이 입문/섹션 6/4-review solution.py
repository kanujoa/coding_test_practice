def DFS(L, sum):     # DFS 함수의 인자로 a 리스트를 참조하는 index(L), 부분집합의 합 누적(sum)이 들어감
    if sum > total // 2:     # sum이 total의 절반을 넘어가는 경우 이제 더이상 합이 같아질 가능성이 없기 때문에 (합이 같은 경우는 둘 다 값이 total // 2인 경우밖에 없다.)
        return     # 시간 복잡도 단축!
    if L == n:     # 종료 조건: L과 n이 같을 때
        if sum == (total - sum):      # 내가 만든 부분집합의 합인 sum과 그 집합의 여집합인 total - sum이 같을 때
            print("YES")     # YES 출력 후
            exit()     # 프로그램 아예 종료 (함수 종료가 아닌 전체 프로그램 종료)
    else:
        DFS(L + 1, sum + a[L])     # a 리스트의 L번째 원소를 부분집합으로 사용하는 경우 sum에 누적 (인덱스는 항상 증가해야 함.)
        DFS(L + 1, sum)     # a 리스트의 L번째 원소를 부분집합으로 사용하지 않는 경우 sum에 누적 X (인덱스는 항상 증가) 
          
n = int(input())     # 주어지는 집합의 원소의 개수
a = list(map(int, input().split()))     # 주어지는 집합의 원소를 하나씩 입력받아 리스트로
total = sum(a)      # total은 주어진 집합의 요소들을 모두 더한 것
DFS(0, 0)
print("NO")     # 위에서 YES를 출력하고 프로그램이 종료되지 않는 경우 NO 하나가 출력되고 끝
