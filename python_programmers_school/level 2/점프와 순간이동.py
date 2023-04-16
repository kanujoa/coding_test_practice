def solution(n):
    result = 1
    if n != 1:     # n이 1일 경우는 아래의 반복문이 실행되지 않고 바로 결과를 return해주어야 함.
        while True:
            if n % 2 != 0:
                n -= 1
                result += 1
            else:
                n //= 2
                if n == 1:
                    break
    return result

print(solution(5))


# 더 간단한 풀이
def solution(n):
    answer = 1
    while n > 1:     # n이 2로 나누어진 몫이 1보다 클 동안만 반복
        answer += n % 2     # 나누어지지 않는 만큼 1칸씩 이동해야 하므로 answer에 n을 2로 나눈 나머지를 추가
        n = n // 2     # n은 절반으로 감소 (수트를 입으면 지금까지의 거리에서 2배 이동이기 때문에 2로 나눔.)
    return answer