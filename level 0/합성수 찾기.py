def solution(n):
    result = []
    for i in range(1, n+1):
        remain = []     # remain은 i가 바뀔 때마다 reset되어야 하므로 for문 위에다 적어주면 안된다. 그렇게 하면 i가 1일때, 2일때, 3일때 ...... 의 나머지가 계속 remain 리스트에 쌓이게 된다.
        for div in range(1, i+1):
            remain.append(i % div)
        if remain.count(0) >= 3:
            result.append(i)
    return len(result)

print(solution(10))

# 다른 풀이 (꼭 필요한 count만 하여 빠르게 작동하는 코드이다.)
# def solution(n):
#     output = 0     --> 결과(합성수의 개수)가 될 ouput은 0부터 시작
#     for i in range(4, n + 1):     --> 어차피 1, 2, 3은 합성수에 해당되지 않기 때문에 이들의 count는 제외하고 합성수인 4부터 시작(i: 나누어지는 수)
#         for j in range(2, int(i ** 0.5) + 1):      --> j는 나누는 수로 1은 어차피 모든 수의 약수이기 때문에 제외하고 시작, 자기 자신도 마찬가지(아래 참조)(2부터가 합성수가 될 수 있는 약수이다.)
#                                                    --> i에 루트씌우고 1을 더하면 약수가 아닌 수들을 빠르게 제외해볼 수 있다. (ex) i=9 라면 j의 범위는 2부터 3까지가 된다. 약수가 되지 못하는 3,4,5,6,7,8 모두 제외 가능)
#             if i % j == 0:     --> 나머지가 0일 경우 j가 i의 약수에 해당되기 때문에 i가 합성수가 될 수 있다. 
#                 output += 1     --> 합성수의 개수에 해당하는 output에 1을 if문이 True일 시 더해준다. (위 조건을 딱 한번만 만족해도 합성수임!)
#                 break     --> 반복문 빠져나가기 (이것이 있어야지 i % j == 0 이 되었을 때 끊고 다음 i로 넘어갈 수 있다.)
#     return output
