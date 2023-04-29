def solution(rows, columns, queries):
    matrix = [[n for n in range(num, num+columns)] for num in range(1, rows*columns+1, columns)]
    min_num = []
    for query in queries:
        if query[0] == 1 and query[1] == 1 and query[2] == rows and query[3] == columns:
            min_num.append(min(query))
        else:
            moving_box = []
            start_row, start_column = query[0] - 1, query[1] - 1
            end_row, end_column = query[2] - 1, query[3] - 1
            # 행렬 돌리는 것까지 생각해야 하므로 맨 윗줄부터 시계방향으로 요소를 탐색하였음.
            for column in range(start_column, end_column+1):     # 맨 윗줄 의미
                    moving_box.append(matrix[start_row][column])
            for row in range(start_row+1, end_row):     # 왼쪽에 끼어 있는 줄 의미
                    moving_box.append(matrix[row][end_column])    
            for column in range(end_column, start_column-1, -1):     # 맨 아래줄 의미
                    moving_box.append(matrix[end_row][column])
            for row in range(end_row-1, start_row, -1):     # 오른쪽에 끼어 있는 줄 의미
                    moving_box.append(matrix[row][start_column])
            min_num.append(min(moving_box))
            # 행렬 시계방향으로 돌리기
            rotate = [moving_box[-1]]
            for i in range(len(moving_box)-1):
                rotate.append(moving_box[i])
            rotate_i = 0
            for column in range(start_column, end_column+1):     # 맨 윗줄 의미
                    matrix[start_row][column] = rotate[rotate_i]
                    rotate_i += 1
            for row in range(start_row+1, end_row):     # 왼쪽에 끼어 있는 줄 의미
                    matrix[row][end_column] = rotate[rotate_i]
                    rotate_i += 1
            for column in range(end_column, start_column-1, -1):     # 맨 아래줄 의미
                    matrix[end_row][column] = rotate[rotate_i]
                    rotate_i += 1
            for row in range(end_row-1, start_row, -1):     # 오른쪽에 끼어 있는 줄 의미
                    matrix[row][start_column] = rotate[rotate_i]
                    rotate_i += 1
    return min_num

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3, 4, [[1, 1, 2, 2], [1, 2, 2, 3], [1, 3, 2, 4], [2, 3, 3, 4]]))




# def solution(rows, columns, queries):
#     matrix = [[n for n in range(num, num+rows)] for num in range(1, rows*columns, rows)]
#     min_num = []
#     for query in queries:
#         if query[0] == 1 and query[1] == 1 and query[2] == rows and query[3] == columns:
#             min_num.append(min(query))
#         else:
#             moving_box = []
#             query = [(query[0], query[1]), (query[2], query[3])]
#             query.sort()
#             start_row, start_column = query[0][0] - 1, query[0][1] - 1
#             end_row, end_column = query[1][0] - 1, query[1][1] - 1
            
#             for column in range(start_column, end_column+1):     
#                 moving_box.append(matrix[start_row][column])
#             for row in range(start_row+1, end_row):     
#                 moving_box.append(matrix[row][end_column])    
#             for column in range(end_column, start_column-1, -1):    
#                 moving_box.append(matrix[end_row][column])
#             for row in range(end_row-1, start_row, -1):     
#                 moving_box.append(matrix[row][start_column])
#             min_num.append(min(moving_box))
            
#             rotate = [moving_box[-1]]
#             for i in range(len(moving_box)-1):
#                 rotate.append(moving_box[i])
#             rotate_i = 0
#             for column in range(start_column, end_column+1):     
#                 matrix[start_row][column] = rotate[rotate_i]
#                 rotate_i += 1
#             for row in range(start_row+1, end_row):     
#                 matrix[row][end_column] = rotate[rotate_i]
#                 rotate_i += 1
#             for column in range(end_column, start_column-1, -1):     
#                 matrix[end_row][column] = rotate[rotate_i]
#                 rotate_i += 1
#             for row in range(end_row-1, start_row, -1):     
#                 matrix[row][start_column] = rotate[rotate_i]
#                 rotate_i += 1
#     return min_num