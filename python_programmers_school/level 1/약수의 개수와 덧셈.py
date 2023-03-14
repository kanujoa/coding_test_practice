def solution(left, right):
    res = 0
    for num in range(left, right+1):
        cnt = 1     # cnt는 num이 바뀌면 다시 1로 초기화 되어야 하므로 맨 위쪽이 아닌 여기에 넣는다.
        for i in range(1, num//2+1):
            if num % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            res += num
        else:
            res -= num
    return res

print(solution(13, 17))

# 다른 풀이 (제곱수의 약수는 홀수개이고, 제곱수가 아닌 수들의 약수는 짝수개임을 이용!)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:     # int(i**0.5)(i에 루트씌운 값을 정수형으로 변환)와 그냥 i**0.5가 같으면 제곱수!
            answer -= i
        else:
            answer += i
    return answer