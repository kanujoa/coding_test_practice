def solution(a, b, n):
    result = 0
    while n >= 2 and n // a != 0:     # n // a != 0의 조건이 없을 경우 무한 루프가 되어 시간 초과가 발생할 수 있다.
        result += n // a * b
        n = n - n // a * a + n // a * b
    return result

print(solution(2, 1, 20))
print(solution(3, 1, 20))
print(solution(3, 2, 20))     # 36


# 더 명료한 풀이
def solution(a, b, n):
    answer = 0
    while n >= a:     # 주목! 가지고 있는 병의 개수(n)가 마트에 주어야 하는 병의 개수(a)보다 크거나 같을 때 동안 반복 
        answer += (n // a) * b     # 마트에서 주는 콜라병수 answer에 누적
        n = (n // a) * b + (n % a)     # 남아 있는 병의 수(n)를 구하는 식 주목! (n // a * b는 받은 병의 수, n % a는 묶음에 해당하지 못해 가져가지 못한 병의 수)
    return answer