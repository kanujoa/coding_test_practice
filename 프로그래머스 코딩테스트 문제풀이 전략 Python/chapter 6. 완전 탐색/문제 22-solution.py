from itertools import permutations

# 1. 소수인지 판별하는 함수를 만든다.
# 소수 판별 문제
# - 10만 이하에서 여러 숫자를 비교: 에라토스테네스의 체 방식 사용
# - 단순히 하나의 해당 숫자가 소수인지를 판별: 아래와 같은 제곱근까지 약수가 있는지 확인하는 방법 사용
def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):     # 숫자 자신의 제곱근까지만 나머지가 0인지를 확인하면 불필요한 탐색을 많이 줄일 수 있다.
        if n % i == 0:
            return True
    return False

def solution(numbers):
  # 2. 주어진 종이 조각으로 만들 수 있는 모든 숫자를 찾는다.
  # 나열하는 순서가 각각 하나의 경우로 인정되므로 1개만 선택할 때부터 n개 모두 선택할 때까지의 순열을 만들어야 한다.
    answer = []
    numbers = list(numbers)     # 문자열은 배열로 취급
    num = []

    for i in range(1, len(numbers) + 1):
        num.append(list(permutations(numbers, i)))     # permutations는 tuple을 반환한다.
    num = [int(''.join(y)) for x in num for y in x]     # 맨 앞에 0이 붙은 경우 int형으로 변환시키면 앞의 0이 사라진다.
    
    # 3. 1번과 2번을 사용하여 나온 소수 배열의 길이를 계산한다.
    for i in num:
        if checkPrime(i):
            answer.append(i)
    
    return len(set(answer))

print(solution('011'))
