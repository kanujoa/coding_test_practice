def solution(cards1, cards2, goal):
    one_idx = -1
    two_idx = -1
    for word in goal:
        if one_idx != len(cards1)-1 and word == cards1[one_idx+1]:
                one_idx += 1
        elif two_idx != len(cards2)-1 and word == cards2[two_idx+1]:
                two_idx += 1
        else:
            return "No"
    else:
        return "Yes"        
    
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

# 좀 더 간단한 풀이
# def solution(cards1, cards2, goal):
#     for g in goal:     
#         if len(cards1) > 0 and g == cards1[0]:     
#             cards1.pop(0)       
#         elif len(cards2) >0 and g == cards2[0]:
#             cards2.pop(0)
#         else:
#             return "No"
#     return "Yes"