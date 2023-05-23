def DFS(cur, check, n):
    if cur > n:
        for i in range(1, len(check)):
            if check[i] == 1:
                print(i, end=' ')
        print()     # 아무것도 출력하지 않으면 바로 다음 줄로 넘어갈 수 있다.
        return
    else:
        check[cur] = 1
        DFS(cur + 1, check, n)
        check[cur] = 0
        DFS(cur + 1, check, n)
    
def main():
    n = int(input())
    check = [0 for _ in range(n+1)]     # 가지를 뻗어나가면서 해당 숫자를 포함하는지 포함하지 않는지를 체크하기 위한 리스트 (0이면 포함 X, 1이면 포함!)
    DFS(1, check, n)

main()