# _sum : 뽑은 동전의 값 누적하기 위한 변수, cnt : 지금까지 선택한 동전의 개수
def DFS(_sum, cnt):      
    # DFS 함수 밖에 있는 answer 변수를 전역변수로써 사용하기 위해 global 사용
    global answer
    # answer과 cnt가 같아지면 더 이상 탐색할 필요 X
    if cnt == answer:    
        return
    # 뽑은 동전의 값들의 합이 거슬러 줄 금액보다 커질 경우
    elif _sum > m:
        return
    # 뽑은 동전의 값들의 합이 거슬러 줄 금액과 같이질 경우
    elif _sum == m:
        # cnt가 지금까지 가능한 최소 동전 개수인 answer보다 더 작다면  
        if answer > cnt:
            # answer의 값을 cnt로 업데이트
            answer = cnt
    else:
        # 그 이외의 경우 coins 리스트를 0번 index부터 돌며 동전 값과 뽑은 개수 누적해 나가기
        for i in range(0, n):
            DFS(_sum + coins[i], cnt + 1)

n = int(input())     # 동전의 종류 개수 
coins = sorted(list(map(int, input().split())), reverse=True)     # n개의 동전의 종류 (내림차순 정렬)
m = int(input())     # 거슬러 줄 금액
answer = 2147000000     # 거슬러 줄 동전의 최소 개수
DFS(0, 0)
print(answer)