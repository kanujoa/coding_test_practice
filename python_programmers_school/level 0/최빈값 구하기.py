def solution(array):
    count_dict = {}
    
    for i in array:
        count_dict[i] = array.count(i)    # 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨. (맨 마지막 것으로 됨.)
    
    count_list = list(count_dict.values())
    
    if count_list.count(max(count_list)) >= 2:
        return -1
    else:             
        for key, value in count_dict.items():     # count_dict.items()는 count_dict에서의 Key, Value 쌍을 얻을 수 있게 해 준다.
            if value == max(count_dict.values()):
                return key
    
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))


# 다른 좋은 풀이
# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1


# enumerate 함수: 리스트의 원소에 순서값을 부여해 주는 함수
# >>> item = ["First", "Second", "Third"] 
# >>> for val in enumerate(item): 
# ... 	print(val) 

# (0, 'First') 
# (1, 'Second') 
# (2, 'Third') 