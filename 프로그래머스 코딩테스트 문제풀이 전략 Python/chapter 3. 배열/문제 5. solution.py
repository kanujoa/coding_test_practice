# 행렬의 곱셈은 3중 for문으로!

def solution(arr1, arr2):
    # 1. 피연산자(arr1)와 연산자(arr2)의 크기만큼 행렬을 생성한다.
    # arr1의 row 수만큼 []가 생성이 되어야 하며 그 안에는 arr2의 column 수만큼의 요소가 들어가야 한다. (요소는 0으로 초기화)
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):     # 2. i는 arr1의 row에 해당
        for j in range(len(arr2[0])):     # 3. j는 arr2의 column에 해당
            for k in range(len(arr1[0])):     # 4. k는 arr1의 column에 해당 (동시에 arr2의 row에 해당한다.)
                # 5. 행렬의 곱셈 결과의 크기는 arr1의 row X arr2의 column이 되므로 answer[i][j]에 값을 할당한다. 
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer