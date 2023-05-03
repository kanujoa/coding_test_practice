def solution(arr1, arr2):
    result = []
    for row_1 in range(len(arr1)):
        tmp = []
        for col_2 in range(len(arr2[0])):
            tmp_num = 0
            for row_2 in range(len(arr2)):
                tmp_num += arr1[row_1][row_2] * arr2[row_2][col_2]
            tmp.append(tmp_num)
        result.append(tmp)
    
    return result
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))