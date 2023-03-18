def solution(arr):
    cur = arr[0]
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != cur:
            cur = arr[i]
            result.append(arr[i])
    return result
print(solution([1,1,3,3,0,1,1]))

# 간단한 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue     # a[-1:]은 a 리스트의 가장 뒤의 값을 list로 만든 것! 즉, 앞뒤가 같을 경우 그냥 pass, 다를 경우 i를 a 리스트에 추가! 
        a.append(i)
    return a