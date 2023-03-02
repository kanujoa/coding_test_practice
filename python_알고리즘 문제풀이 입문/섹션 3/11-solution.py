board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]     # 가로 부분 슬라이싱을 이용하면 내가 작성한 풀이처럼 append를 사용하지 않아도 리스트 생성 가능 (1차원 리스트는 가로만 슬라이싱 가능 세로는 불가능)
        if tmp == tmp[::-1]:     # 슬라이싱(-1)을 이용해 tmp reverse 시키기 (뒤집은 것과 원래 tmp가 같으면 회문!)
            cnt += 1     # cnt 1 추가하기
        for k in range(2):     # 세로 부분 슬라이싱을 위해 변수 k를 생성
            if board[i+k][j] != board[i+5-k-1][j]:     # 바깥 부분부터 안으로 좁혀가면서 숫자 비교하기 (열 고정, 행만 바뀜)
                break
        else:     # break 걸리지 않고 넘어가면
            cnt += 1     # cnt 1 추가하기

print(cnt)        