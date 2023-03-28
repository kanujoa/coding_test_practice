def solution(numbers):
    array = []
    for i in range(0, len(numbers)-1):     # range(len(numbers))로 적어도 됨.
        for j in range(i+1, len(numbers)):
            array.append(numbers[i] + numbers[j])
    return sorted(list(set(array)))

print(solution([5,0,2,7]))     
# range(len(numbers))로 적는 경우 i가 3이 될 때 j의 범위가 (4, 4)가 되므로 j가 바뀌지 않고 다시 윗줄 for문으로 가게 된다.
# 윗줄 for문에서 i 범위는 3까지이므로 i가 바뀌지 않고 retrun문으로 바로 향하게 된다.