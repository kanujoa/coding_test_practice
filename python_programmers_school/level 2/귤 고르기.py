# 효율성 테스트 통과가 어려웠던 문제
def solution(k, tangerine):
    result = 0
    array = [0] * (max(tangerine) + 1)
    for x in tangerine:
        array[x] += 1
    array = sorted(array)
    while k > 0:
        k -= array[-1]
        result += 1
        array.pop()
    return result

print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))


# 다른 사람의 풀이 1 (나와 비슷한 방법)
def solution(k, tangerine):
    answer = 0
    l = [0 for i in range(max(tangerine))]
    for i in range(len(tangerine)):
        l[tangerine[i]-1] += 1
    l.sort(reverse = True)

    index = 0   
    while answer<k:
        answer += l[index]
        index += 1     # 여기에서 pop을 사용 안하고 index를 증가시키는 연산을 하는 방법을 사용하였다.
    return index


# 다른 사람의 풀이 2 (collections 모듈 사용)
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)     # 리스트의 원소가 key, 그의 개수가 value가 되는 객체가 생성됨.     

    for v in sorted(cnt.values(), reverse = True):     # cnt 객체의 값들을 내림차순으로 정렬한 리스트의 요소들을 하나씩 살핀다.
        k -= v     # 여기서부터는 위의 것들과 방식 유사.
        answer += 1
        if k <= 0:
            break
    return answer

print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))