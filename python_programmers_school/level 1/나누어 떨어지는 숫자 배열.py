def solution(arr, divisor):
    arr.sort()
    d = [num for num in arr if num % divisor == 0]
    if len(d) == 0:
        return [-1]
    else:
        return d
    
# 매우 간단한 풀이
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
# or은 앞의 것이 거짓일 때 뒤의 것인 [-1]이 출력되게 해 준다. (앞의 것은 값이 없으면 False가 되게 된다.)