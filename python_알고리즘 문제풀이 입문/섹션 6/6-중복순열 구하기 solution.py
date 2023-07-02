import sys
input = sys.stdin.readline

def DFS(L):
    if L == m:     # res에서의 인덱스를 나타내는 L과 뽑아야 하는 구슬 수를 나타내는 m이 같아지면 하나의 중복순열이 만들어졌다는 뜻!
        global cnt
        for j in range(m):
            print(res[j], end=' ')     # 현재 res에 저장되어 있는 구슬 번호 출력
        print()     # 다음 줄로 넘어가기
        cnt += 1     # 경우의 수의 개수(cnt) 1 증가
    else:
        for i in range(1, n+1):     # i의 범위는 구슬의 번호 모두이다.
            res[L] = i     # res의 L번 인덱스에 구슬 번호 i를 저장
            DFS(L+1)     # res의 인덱스 1 증가
                    

n, m = map(int, input().split())     # n: 1부터 n까지 구슬에 번호가 적혀 있음, m: 구슬을 중복을 허락해 m번 뽑음
res = [0] * m     # res는 구슬을 뽑는 경우의 수를 저장 (요소 하나하나는 구슬의 번호), m개만큼의 0으로 초기화
cnt = 0     # 경우의 수의 개수
DFS(0)     # DFS 함수의 인자는 res의 index번호
print(cnt)