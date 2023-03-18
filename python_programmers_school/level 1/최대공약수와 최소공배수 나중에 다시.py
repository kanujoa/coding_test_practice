def solution(n, m):
    big = max([n, m])
    small = min([n, m])
    gcd = small
    while gcd != 0:
        if small % gcd == 0 and big % gcd == 0:
            break
        else:
            gcd -= 1
    
    lcm = big
    while True:
        if lcm % small == 0 and lcm % small == 0:
            break
        else:
            lcm *= 2
            
    return [gcd, lcm]

print(solution(3, 12))