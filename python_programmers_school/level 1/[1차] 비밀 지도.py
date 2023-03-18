def solution(n, arr1, arr2):
    arr1 = list(map(bin, arr1))
    arr2 = list(map(bin, arr2))
    result = []
    for i in range(n):
        arr1[i] = arr1[i][2:]
        arr2[i] = arr2[i][2:]
        if len(arr1[i]) != n:
            arr1[i] = arr1[i].rjust(n, "0")
        if len(arr2[i]) != n:
            arr2[i] = arr2[i].rjust(n, "0")
        decrypt = ""
        for j in range(n):
            if arr1[i][j] == "0" and arr2[i][j] == "0":
                decrypt += " "
            elif arr1[i][j] == "1" or arr2[i][j] == "1":
                decrypt += "#"
        result.append(decrypt)
    return result

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

# 깔끔한 풀이
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):     --> zip으로 묶으면 한번에 처리 가능
#         a12 = str(bin(i|j)[2:])     --> bin(i|j)는 i와 j를 2진변환하고 각 자리에서 모두 0(False)이면 0, 하나라도 1(True)이 있으면 1을 반환한다. 그리고 앞의 0b를 없애야 하므로 [2:]를 한다.
#         a12=a12.rjust(n,'0')     --> 아까 슬라이싱 해줬으므로 문자열 길이가 n이 되게 필요한 만큼 0을 넣어줌.(rstrip)
#         a12=a12.replace('1','#')     --> a12에서 '1' 부분은 모두 '#'(벽)으로 대신함
#         a12=a12.replace('0',' ')     --> a12에서 '0' 부분은 모두 ' '(공백)으로 대신함
#         answer.append(a12)    
#     return answer
# for 문 바로 아래 코드에서 벽인지 공백인지를 구분해내는 것 완료!