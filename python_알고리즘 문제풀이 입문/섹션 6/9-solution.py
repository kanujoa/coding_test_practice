# 파스칼 삼각형 : 수학에서 이항계수를 삼각형 모양으로 배열한 것
# 따라서 합을 구할 때 재귀함수 돌릴 필요 없이 이항정리 공식 이용해서 풀면 됨.
# ex) 예제로 나온 것을 이용하면 3 * 3C0 + 1 * 3C1 + 2 * 3C2 + 4 * 3C3 = 16 이 됨.
# 가능한 순열의 숫자 순서대로 n-1C0부터 n-1Cn 까지 곱한 것을 모두 더하여 f와 같아지면 해당 순열을 정답으로 하고 출력하고 끝내면 됨.

def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + p[L] * b[L])
                ch[i] = 0


n, f = map(int, input().split())     # n은 맨 윗줄 숫자의 개수 (숫자의 범위는 1부터 n까지), f는 가장 맡 줄에 있는 수
p = [0] * n     # 순열
b = [1] * n     # 순서대로 곱할 이항계수 리스트(n-1C?의 형태를 숫자로 나타낸 것)
ch = [0] * (n+1)     # 순열 만들 때 사용할 체크리스트
for i in range(1, n):     # n-1C?에서 ?는 0부터 n-1까지가 된다.어차피 0에서는 이항계수가 1이기 때문에 0은 제외함.
    b[i] = b[i-1] * (n-i) // i
DFS(0, 0)