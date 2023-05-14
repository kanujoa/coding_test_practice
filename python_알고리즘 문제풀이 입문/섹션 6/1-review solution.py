# 재귀를 작성할 때에는 if else (조건문)을 이용하여 작성하겠다.
def DFS(x):
    if x == 0:     # 무한반복하면 안되기 때문에 x를 계속 2로 나누어서 0이 될 때가 오면 
        return    # return 을 입력하여 재귀를 종료
    else:     # x가 0이 아니면 계속 재귀를 호출해야 하므로
        DFS(x // 2)     # 재귀함수를 돌리고
        print(x % 2, end='')     # x 0까지 다 돌리면 print가 실행됨.
# 재귀함수를 통해 나머지를 아래에서부터 위로 출력할 수 있게 되었다.

def main():
    n = int(input())
    DFS(n)

main()