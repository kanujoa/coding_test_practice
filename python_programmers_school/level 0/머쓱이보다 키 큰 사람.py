def solution(array, height):
    result = []
    for i in array:
        if i > height:
            result.append(i)
    return len(result)

# 다른 풀이
# def solution(array, height):
#     array.append(height)     array에 머쓱이의 키인 height를 요소로 추가
#     array.sort(reverse=True)    sort(reverse=True)를 사용하여 array 리스트 요소들을 내림차순으로 정렬
#     return array.index(height)     index(height)를 이용해 array 리스트 내에서 머쓱이의 키인 height 요소의 위치 찾기
# (머쓱이 앞에 존재하는 키 큰 사람 수만큼이 위치가 됨. 역시 숫자 0부터 셈.)
# 위처럼 하면 한명한명 다 비교하지 않아도 한번에 몇 번째 index인지를 알아냄으로써 머쓱이보다 키 큰 사람의 수도 곧 알아내기 가능!