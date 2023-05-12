import itertools

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = [number for number in numbers]
    cases = []
    for i in range(1, len(nums) + 1):
        # 조합을 사용하지 않고 순열만 사용하여 풀 수 있다.
        combination = list(itertools.combinations(nums, i))
        for c in combination:
            if len(c) > 1:
                permutation = list(itertools.permutations(c, len(c)))
                for p in permutation:
                    cases.append(''.join(list(p)).lstrip('0'))
            else:
                cases.append(c[0])
    cases = set(cases)
    
    cnt = 0
    for case in cases:
        if case != '':
            if check_prime(int(case)):
                cnt += 1
    return cnt

# 런타임 에러 반례! (옆과 같이 입력이 주어진다면, case에 ''(빈 문자열)이 포함되어 있어28번줄에서 int(case)가 불가하므로 오류가 남!)
print(solution('00'))     