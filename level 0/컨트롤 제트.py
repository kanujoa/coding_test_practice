def solution(s):
    rmv_blank = s.split()
    a = 0
    for i in range(len(rmv_blank)):
        if rmv_blank[i] != 'Z':
            a += int(rmv_blank[i])
        elif rmv_blank[i] == 'Z':
            a -= int(rmv_blank[i-1])
    return a

# 더 좋은 코드
# def solution(s):
#     arr = s.split(' ')
#     result =[]
#     for i in arr :
#         if i=='Z':
#             result.pop()     pop 함수는 리스트의 인덱스를 받아서 삭제하는 기능을 한다. (Z가 나오면 가장 최근에 저장했던 리스트 요소 하나 삭제)
#         else:
#             result.append(int(i))     Z가 나오지 않을 시 리스트에 해당 숫자 추가하기
#     return sum(result)     리스트에 남은 숫자들만 다 더하기