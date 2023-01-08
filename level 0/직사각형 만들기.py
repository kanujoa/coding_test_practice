def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots] 
    width = max(x) - min(x)
    height = max(y) - min(y)
    return width * height
    
# 비슷한 풀이 (내 풀이 한줄로 적는 법)
# def solution(dots): 
#     return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])     
# max(dots) 하면 dots 리스트에서 두 요소가 모두 최대인 리스트가 나온다. 반대로 min(dots) 하면 두 요소가 모두 최소인 리스트가 나온다.
