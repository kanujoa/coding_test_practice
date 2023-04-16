# 유클리드 호제법 사용
# 수가 여러개일 경우 일단 임의로 2개를 잡아서 유클리드 호제법으로 최대공약수를 구한 후 그 최대공약수와 다음 숫자의 최대공약수를 구하는
# 식으로 진행한다.

def GCD(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
        return a
    
def solution(arr):
    result = 1
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = GCD(gcd, arr[i])
    for j in arr:
        result *= j // gcd
    return result * gcd

# print(solution([2, 6, 8, 14]))

def solution(arr):
    arr.sort()
    result = 1
    divisor = 1
    while divisor <= arr[0]:
        divisor += 1
        for i in range(1, len(arr)):
            if arr[i] % divisor != 0:
                break
        else:
            result *= divisor
            arr = [arr[i] // divisor for i in range(1, len(arr))]
    for x in arr:
        result *= x
    return result

print(solution([12, 32, 45, 67, 72]))