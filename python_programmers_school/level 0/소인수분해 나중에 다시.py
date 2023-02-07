def solution(n):
    prime_factor = []
    
    for num in range(2, n+1):     
        if n % num == 0:
            prime_factor.append(num)
        else:
            pass
    
    if len(prime_factor) == 1:
        return prime_factor
    else:
        for i in prime_factor:
            prime_num = []
            for num2 in range(i, i+1):
                if i % num2 == 0:
                    prime_num.append(i)
                    if len(prime_num) == 1:
                        pass
                    else:
                        prime_factor.remove(i)
                else:
                    prime_factor.remove(i)
        return prime_factor
            
print(solution(12))

# def solution(n):
#     prime_factor = []
#     for num in range(2, n+1):
#         if n % num == 0:
#             prime_factor.append(num)
#             if len(prime_factor) == 2:
#                 return [n]
#             else:
#                 pass
#         else:
#             pass
#             # while n % num == 0:
#             #     prime_factor.append(num)
#             #     n // num
#             #     if n // num == 1:
#             #         break
#             #         return prime_factor
