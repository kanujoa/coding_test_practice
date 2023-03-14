def solution(arr1, arr2):
    res = []
    for i in range(len(arr1)):
        n = []
        for j in range(len(arr1[i])):
            n.append(arr1[i][j] + arr2[i][j])
        res.append(n)
    return res

# 다른 풀이
# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
#     return answer
# zip(): 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 
# 있는 반복자(iterator)를 반환 (A와 B에는 arr1, arr2가 들어가고, a와 b에는 (arr1[i], arr2[i]) 이렇게 들어감
# 그리고 c, d에는 (arr1[i][j], arr2[i][j])가 들어가서 그거 2개가 더해진 값을 이차원 리스트 안에 넣음.)