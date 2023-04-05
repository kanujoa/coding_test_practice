def solution(X, Y):
    answer = ''
    for i in X:
        if Y.count(i) != 0:
            answer += i
            Y = Y.replace(i, '', 1)
    return answer if answer != '' else -1      

print(solution("100", "2345"))
print(solution("100", "123450"))