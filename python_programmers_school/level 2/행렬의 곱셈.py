def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        j = 0
        tmp1 = []
        while j < len(arr2[0]):
            tmp2 = []
            for x in range(len(arr2)):
                tmp2.append(arr1[i][x] * arr2[x][j])
            tmp1.append(sum(tmp2))
            j += 1
        result.append(tmp1)
    return result

# print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))


# 다른 풀이 1
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
# 이차원 리스트로 선언된 B를 언패킹하여 1차원으로 만들고 zip하여 열로 나타내었다.


# 다른 풀이 2
def productMatrix(A, B):
    answer = []

    for i in range(len(A)):     # i는 A의 일차원 리스트를 가리키는 인덱스
        arr = []
        for j in range(len(B[0])):     # j는 B의 일차원 리스트 안의 요소를 가리키는 인덱스
            tmp = 0
            for k in range(len(A[0])):     # k는 A의 일차원 리스트 안의 요소를 가리키는 인덱스
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer