# 실제 채점에서 실패

def check(i, j, room):
# 맨해튼 거리 1일 경우
    if i != 4:
        if room[i + 1][j] == "P":    # 바로 한 칸 아래에 사람이 있는지 확인
            return False
    if j != 4:
        if room[i][j + 1] == "P":     # 바로 한 칸 오른쪽에 사람이 있는지 확인
            return False

# 맨해튼 거리 2일 경우
    # 1. 현재 사람이 있는 위치에서 아래, 오른쪽으로 2칸 떨어져 있는 곳에 사람이 있을 경우 그 사이에 파티션이 있는지 확인
    if i < 3:
        if room[i + 2][j] == "P":     # 두 칸 아래에 사람이 있는지 확인
            if room[i + 1][j] != "X":     # 그 사이에 파티션이 있는지 확인
                return False
    if j < 3:
        if room[i][j + 2] == "P":     # 두 칸 오른쪽에 사람이 있는지 확인
            if room[i][j + 1] != "X":     # 그 사이에 파티션이 있는지 확인
                return False
    
    # 2. 현재 사람이 있는 위치에서 왼쪽 바로 아래 대각선과 오른쪽 바로 아래 대각선에 사람이 있을 경우
    # 인접 반대 대각선 위치에 모두 파티션이 존재하는지 확인하기
    if i != 4 and j != 4:   
        if room[i + 1][j + 1] == "P":     # 오른쪽 대각선 바로 아래에 사람이 있는지 확인
            if room[i + 1][j] != "X" or room[i][j + 1] != "X":      # 그 사람 왼쪽과 현재 사람 위치 오른쪽에 파티션이 있는지 확인
                return False
    if i != 4 and j != 0:
        if room[i + 1][j - 1] == "P":     # 왼쪽 대각선 바로 아래에 사람이 있는지 확인
            if room[i + 1][j] != "X" or room[i][j - 1] != "X":     # 그 사람 오른쪽과 현재 사람 위치 왼쪽에 파티션이 있는지 확인
                return False
    
    return True

def solution(places):
    result = []
    for place in places:
        room = [[s for s in state] for state in place]
        for i in range(5):
            if len(result) == places.index(place) + 1:
                break
            for j in range(5):
                if room[i][j] == "P":
                    # 맨해튼 거리 1일 경우
                    if i != 4:
                        if room[i + 1][j] == "P":    # 바로 한 칸 아래에 사람이 있는지 확인
                            result.append(0)
                            break
                    if j != 4:
                        if room[i][j + 1] == "P":     # 바로 한 칸 오른쪽에 사람이 있는지 확인
                            result.append(0)
                            break
                        
                    # 맨해튼 거리 2일 경우
                    # 1. 현재 사람이 있는 위치에서 아래, 오른쪽으로 2칸 떨어져 있는 곳에 사람이 있을 경우 그 사이에 파티션이 있는지 확인
                    if i < 3:
                        if room[i + 2][j] == "P":     # 두 칸 아래에 사람이 있는지 확인
                            if room[i + 1][j] != "X":     # 그 사이에 파티션이 있는지 확인
                                result.append(0)
                                break
                    if j < 3:
                        if room[i][j + 2] == "P":     # 두 칸 오른쪽에 사람이 있는지 확인
                            if room[i][j + 1] != "X":     # 그 사이에 파티션이 있는지 확인
                                result.append(0)
                                break
                            
                    # 2. 현재 사람이 있는 위치에서 왼쪽 바로 아래 대각선과 오른쪽 바로 아래 대각선에 사람이 있을 경우
                    # 인접 반대 대각선 위치에 모두 파티션이 존재하는지 확인하기
                    if i != 4 and j != 4:   
                        if room[i + 1][j + 1] == "P":     # 오른쪽 대각선 바로 아래에 사람이 있는지 확인
                            if room[i + 1][j] != "X" or room[i][j + 1] != "X":      # 그 사람 왼쪽과 현재 사람 위치 오른쪽에 파티션이 있는지 확인
                                result.append(0)
                                break
                    if i != 4 and j != 0:
                        if room[i + 1][j - 1] == "P":     # 왼쪽 대각선 바로 아래에 사람이 있는지 확인
                            if room[i + 1][j] != "X" or room[i][j - 1] != "X":     # 그 사람 오른쪽과 현재 사람 위치 왼쪽에 파티션이 있는지 확인
                                result.append(0)
                                break
        else:
            result.append(1)
    return result

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["PXOOO", "XPXOO", "OXPXO", "OOXPX", "OOOXP"]]))
# print(solution([["PXXXX", "XPXXX", "XXXPP", "XXXXX", "XXXXX"]]))

# 1. solution 함수에서의 break가 문제였다.
# 2. 


# 맨해튼 거리 1일 경우의 함수
# def distance_1(i, j, room):
#     if i != 0:
#         if room[i - 1][j] == "P":    # 바로 한 칸 위에 사람이 있는지 확인
#             return False
#     if i != 4:
#         if room[i + 1][j] == "P":     # 바로 한 칸 아래에 사람이 있는지 확인
#             return False
#     if j != 0:
#         if room[i][j - 1] == "P":     # 바로 한 칸 왼쪽에 사람이 있는지 확인
#             return False
#     if j != 4:
#         if room[i][j + 1] == "P":     # 바로 한 칸 오른쪽에 사람이 있는지 확인
#             return False
#     return True

# 맨해튼 거리 2일 때의 함수
# def distance_2(i, j, room):
#     # 1. 현재 사람이 있는 위치에서 위, 아래, 왼쪽, 오른쪽으로 2칸 떨어져 있는 곳에 사람이 있을 경우 그 사이에 파티션이 있는지 확인
#     if i > 1:
#         if room[i - 2][j] == "P":     # 두 칸 위에 사람이 있는지 확인
#             if room[i - 1][j] != "X":     # 그 사이에 파티션이 있는지 확인
#                 return False
#     if i < 3:
#         if room[i + 2][j] == "P":     # 두 칸 아래에 사람이 있는지 확인
#             if room[i + 1][j] != "X":     # 그 사이에 파티션이 있는지 확인
#                 return False
#     if j > 1:
#         if room[i][j - 2] == "P":     # 두 칸 왼쪽에 사람이 있는지 확인
#             if room[i][j - 1] != "X":     # 그 사이에 파티션이 있는지 확인
#                return False
#     if j < 3:
#         if room[i][j + 2] == "P":     # 두 칸 오른쪽에 사람이 있는지 확인
#             if room[i][j + 1] != "X":     # 그 사이에 파티션이 있는지 확인
#                 return False
    
#     # 2. 현재 사람이 있는 위치에서 왼쪽 바로 위 대각선과 오른쪽 바로 아래 대각선, 혹은 오른쪽 바로 위 대각선과 왼쪽 바로 아래 대각선에 사람이 있을 경우 
#     # 인접 반대 대각선 위치에 모두 파티션이 존재하는지 확인하기
#     if i != 0 and j != 0:
#         if room[i - 1][j - 1] == "P":     # 왼쪽 대각선 바로 위에 사람이 있는지 확인
#             if room[i - 1][j] != "X" or room[i][j - 1] != "X":     # 그 사람 오른쪽과 현재 사람 위치 왼쪽에 파티션이 있는지 확인
#                 return False
#     if i != 4 and  j != 4:   
#         if room[i + 1][j + 1] == "P":     # 오른쪽 대각선 바로 아래에 사람이 있는지 확인
#             if room[i + 1][j] != "X" or room[i][j + 1] != "X":      # 그 사람 왼쪽과 현재 사람 위치 오른쪽에 파티션이 있는지 확인
#                 return False
#     if i != 0 and j != 4:
#         if room[i - 1][j + 1] == "P":     # 오른쪽 대각선 바로 위에 사람이 있는지 확인
#             if room[i - 1][j] != "X" or room[i][j + 1] != "X":     # 그 사람 왼쪽과 현재 사람 위치 오른쪽에 파티션이 있는지 확인
#                 return False
#     if i != 4 and  j != 0:
#         if room[i + 1][j - 1] == "P":     # 왼쪽 대각선 바로 아래에 사람이 있는지 확인
#             if room[i + 1][j] != "X" or room[i][j - 1] != "X":     # 그 사람 오른쪽과 현재 사람 위치 왼쪽에 파티션이 있는지 확인
#                 return False
#     return True

# def solution(places):
    # result = []
    # for place in places:
    #     room = [[s for s in state] for state in place]
    #     i = 0
    #     for j in range(5):
    #         if room[i][j] == "P":
    #             if distance_1(i, j, room) == False:
    #                 result.append(0)
    #                 i += 1
    #                 break
    #             if distance_2(i, j, room) == False:
    #                 result.append(0)
    #                 i += 1
    #                 break
    #     else:
    #         result.append(1)
    #         i += 1
    # return result
                    

# print(solution([["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))