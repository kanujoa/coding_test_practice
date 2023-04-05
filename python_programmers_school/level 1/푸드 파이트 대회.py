def solution(food):
    result = []
    idx = 0
    for i in range(1, len(food)):
        if food[i] % 2 == 1:
            food[i] -= 1
        for _ in range(food[i]):
            result.insert(idx, i)
        idx += food[i] // 2
    result.insert(idx, 0)
    return ''.join(map(str, result))

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))


# 간단한 풀이
def solution(food):
    answer = ''
    for f in range(1, len(food)):     
         answer += str(f)*(food[f]//2)     # 0 기준으로 이전에 놓일 숫자들을 먼저 answer에 채움.  // 는 몫만 반환하기 때문에 food[f]가 홀수인 경우도 자동 처리 가능
    return answer + '0' + ''.join(list(answer)[::-1])     # answer 문자열 + '0' + answer(string)을 list화시켜 그것을 뒤집은 배열을 다시 string화 시킨 값