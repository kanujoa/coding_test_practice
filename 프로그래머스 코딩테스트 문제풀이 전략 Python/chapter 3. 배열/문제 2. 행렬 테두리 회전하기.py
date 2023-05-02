from collections import deque

def solution(rows, columns, queries):
    matrix = [[(i) * columns + (j + 1) for j in range(columns)]for i in range(rows)]
    result = []
    
    for query in queries:
        y1, x1 = query[0], query[1]
        y2, x2 = query[2], query[3]
        rotate = deque()
        if x1 > x2:
            y1, x1 = query[2], query[3]
            y2, x2 = query[0], query[1]
        for x in range(x1-1, x2):
            rotate.append(matrix[y1-1][x])
        for y in range(y1, y2-1):
            rotate.append(matrix[y][x2-1])
        for x in range(x2-1, x1-2, -1):
            rotate.append(matrix[y2-1][x])
        for y in range(y2-2, y1-1, -1):
            rotate.append(matrix[y][x1-1])
        result.append(min(rotate))
        rotate.appendleft(rotate.pop())
        
        i = 0
        for x in range(x1-1, x2):
            matrix[y1-1][x] = rotate[i]
            i += 1
        for y in range(y1, y2-1):
            matrix[y][x2-1] = rotate[i]
            i += 1
        for x in range(x2-1, x1-2, -1):
            matrix[y2-1][x] = rotate[i]
            i += 1
        for y in range(y2-2, y1-1, -1):
            matrix[y][x1-1] = rotate[i]
            i += 1
    return result

print(solution(6, 6, [[5, 4, 2, 2], [6, 6, 3, 3], [5, 1, 6, 3]]))
# print(solution(3, 4, [[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]))



# 케이스 2번 실패..
# 첫번째로 나오는 if문이 문제였다. 실행문대로 min_num.append(min(query))만 하고 끝내면 matrix에 회전한 후의 배열이 들어가질 않으므로
# 틀린 풀이이다. (queries의 길이가 1로 끝나면 몰라도)
# 따라서 첫번째로 나오는 조건문 부분을 아예 지워주어야 한다. (위 풀이 참고)
# def solution(rows, columns, queries):
#     matrix = [[n for n in range(num, num+columns)] for num in range(1, rows*columns+1, columns)]
#     min_num = []
#     for query in queries:
#         if query[0] == 1 and query[1] == 1 and query[2] == rows and query[3] == columns:
#             min_num.append(min(query))
#         else:
#             moving_box = []
#             start_row, start_column = query[0] - 1, query[1] - 1
#             end_row, end_column = query[2] - 1, query[3] - 1
#             # 행렬 돌리는 것까지 생각해야 하므로 맨 윗줄부터 시계방향으로 요소를 탐색하였음.
#             for column in range(start_column, end_column+1):     # 맨 윗줄 의미
#                     moving_box.append(matrix[start_row][column])
#             for row in range(start_row+1, end_row):     # 왼쪽에 끼어 있는 줄 의미
#                     moving_box.append(matrix[row][end_column])    
#             for column in range(end_column, start_column-1, -1):     # 맨 아래줄 의미
#                     moving_box.append(matrix[end_row][column])
#             for row in range(end_row-1, start_row, -1):     # 오른쪽에 끼어 있는 줄 의미
#                     moving_box.append(matrix[row][start_column])
#             min_num.append(min(moving_box))
#             # 행렬 시계방향으로 돌리기
#             rotate = [moving_box[-1]]
#             for i in range(len(moving_box)-1):
#                 rotate.append(moving_box[i])
#             rotate_i = 0
#             for column in range(start_column, end_column+1):     # 맨 윗줄 의미
#                     matrix[start_row][column] = rotate[rotate_i]
#                     rotate_i += 1
#             for row in range(start_row+1, end_row):     # 왼쪽에 끼어 있는 줄 의미
#                     matrix[row][end_column] = rotate[rotate_i]
#                     rotate_i += 1
#             for column in range(end_column, start_column-1, -1):     # 맨 아래줄 의미
#                     matrix[end_row][column] = rotate[rotate_i]
#                     rotate_i += 1
#             for row in range(end_row-1, start_row, -1):     # 오른쪽에 끼어 있는 줄 의미
#                     matrix[row][start_column] = rotate[rotate_i]
#                     rotate_i += 1
#     return min_num





