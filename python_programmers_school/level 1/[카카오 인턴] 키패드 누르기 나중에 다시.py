def solution(numbers, hand):
    result = ""
    L_cur_pos = "*"
    R_cur_pos = "#"
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            result += "L"
            L_cur_pos = i
        elif i == 3 or i == 6 or i == 9:
            result += "R"
            R_cur_pos = i
        else:     # i == 2, i == 5, i == 8, i == 0
            i_tmp = i
            R_tmp = R_cur_pos
            L_tmp = L_cur_pos
            if i == 0:
                i_tmp = 11
            if R_cur_pos == "#":
                R_tmp = 10
            elif R_cur_pos == 0:
                R_tmp = 11
            if L_cur_pos == "*":
                L_tmp = 12
            elif L_cur_pos == 0:
                L_tmp = 11
            L_distance = (abs(i_tmp-L_tmp))//3 + (abs(i_tmp-L_tmp))%3     # 눌러야 할 번호 위치와 현재 왼손 위치한 번호 사이 거리
            R_distance = (abs(i_tmp-R_tmp-2))//3 + (abs(i_tmp-R_tmp))%3     # 눌러야 할 번호 위치와 현재 오른손 위치한 번호 사이 거리
            if L_distance == R_distance:
                if hand[0] == "r":
                    R_cur_pos = i
                else:     # hand[0] == "l"
                    L_cur_pos = i
                result += hand[0].upper()
            elif L_distance < R_distance:
                L_cur_pos = i
                result += "L"
            else:     # R_distance < L_distance
                R_cur_pos = i
                result += "R"
    return result

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))