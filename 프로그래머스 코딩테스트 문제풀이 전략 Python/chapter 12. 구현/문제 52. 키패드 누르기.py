def distance(num, l, r):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    n_row, n_column = 0, 0     # num의 keypad에서의 위치
    l_row, l_column = 0, 0     # 왼쪽 엄지의 keypad에서의 위치
    r_row, r_column = 0, 0     # 오른쪽 엄지의 keypad에서의 위치
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == num:
                n_row, n_column = i, j
            if keypad[i][j] == l:
                l_row, l_column = i, j
            if keypad[i][j] == r:
                r_row, r_column = i, j
    l_distance =  abs(n_row - l_row) + abs(n_column - l_column)    # 왼손이 num 까지 움직이는 데 필요한 거리
    r_distance =  abs(n_row - r_row) + abs(n_column - r_column)   # 오른손이 num 까지 움직이는 데 필요한 거리
    if l_distance == r_distance:
        return 'same'
    elif l_distance > r_distance:     # 거리가 더 적게 나가는 쪽을 반환
        return 'R'
    else:
        return 'L'

def solution(numbers, hand):
    l = '*'     # 왼손의 위치
    r = '#'     # 오른손의 위치
    answer = []
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer.append('L')
            l = num
        elif num == 3 or num == 6 or num == 9:
            answer.append('R')
            r = num
        else:
            near = distance(num, l, r)     # 함수는 한 번 실행하고 변수에 담아주어야 된다. 아니면 if, elif에서 2번 실행될 수 있다. 따라서 r = num 변환 이후에도 실행될 수 있기 때문에 이상한 결과가 나올 수 있음.
            if near == 'R':     # 오른쪽 엄지가 num에 더 가까운 경우
                answer.append('R')
                r = num
            elif near == 'L':     # 왼쪽 엄지가 num 에 더 가까운 경우 
                answer.append('L')
                l = num
            else:     # 오른쪽 엄지와 왼쪽 엄지의 num까지의 거리가 같은 경우
                if hand == 'right':
                    answer.append('R')
                    r = num
                else:
                    answer.append('L')
                    l = num
    return ''.join(answer) 

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))    

# 딕셔너리를 이용한 풀이
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer