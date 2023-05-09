# 등비수열의 합으로 구하는 방법
# solution 2에서의 781, 156, 31, 6, 1의 간격 순서를 이용
# 1 + 5^2 + 5^3 + 5^4 을 하면 781이 나오므로 위 수열은 등비수열임을 알 수 있다.
# 등비수열 합의 공식을 이용하면 (5^(5-i) - 1) / 4의 식을 얻을 수 있다.
# 문자열이 몇 번째 위치하는지에 대한 i만 알면 미리 수치를 계산할 수 있다.

def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / 4 * "AEIOU".index(n) + 1
    return answer