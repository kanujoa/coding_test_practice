def solution(s):
    count_dict = {}
    for n in range(len(s)):
        if s[n] != s[n-1]:
            count_dict[s[n]] = s.count(s[n])
        else:
            pass
   
        
print(solution([1, 2, 3, 3, 3, 4]))
