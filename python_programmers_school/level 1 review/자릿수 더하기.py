def solution(number):
    answer = 0
    for s in str(number):
        answer += int(s)
    return answer


# 다른 사람의 풀이 1 (map 사용)
def sum_digit(number):
    return sum(map(int, str(number)))     

# 다른 사람의 풀이 2 (재귀 사용)
# 321%10은 123을 10으로 나눈 나머지 3을 반환합니다. 123//10은 123을 10으로 나눈 몫 12를 반환합니다. 따라서 12를 다시 함수에 넣고 
# 돌리겠죠. (return 123%10 + sum_disgit(123//10) -> return 3 + sum_digit(12)).2번째 돌릴땐 return에는 이전에 반환한 3 에다가 
# + 12%10 + sum_digit(12//10). 즉 2번째에는 return 3+2+sum_digit(1)이 됩니다. 3번째에는 if문에서 1이 10보다 작으므로 return 1을 
# 해주고 최종적으로 return 3+2+1이 됩니다.
def sum_digit(number):
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)