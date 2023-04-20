# 꼭 citations에 h값이 들어가 있지 않다는 것을 인지하고 넘어가기!
# 아래 풀이는 테스트 케이스 통과 못한 풀이
def solution(citations):
    citations.sort()
    h_index = 0
    cur_index = 0
    if min(citations) >= len(citations):
        return len(citations)
    else:
        for h in range(max(citations) + 1):
            if h not in citations:
                if len(citations) - cur_index > h:
                    h_index = h
                else:
                    break
            else:
                if len(citations) - citations.index(h) > h:
                    h_index = h
                    cur_index = citations.index(h)
                else:
                    break
        return h_index

# print(solution([6, 5, 5, 5, 3, 2, 1, 0]))
# print(solution([1, 4, 5]))
# print(solution([5, 6, 7]))
# print(solution([25, 8, 5, 3, 3]))
# print(solution([15, 12, 10, 8, 6, 3, 2, 1]))
# print(solution([2]))
# print(solution([0]))
# print(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20]))
print(solution([10, 10, 10, 10, 10]))


# 다른 사람의 풀이 1
def solution(citations):
    citations.sort(reverse=True)     # citations 배열을 내림차순으로 정렬한다.
    answer = max(map(min, enumerate(citations, start=1)))     # 인덱스(1부터 시작으로 설정)와 citations 요소 중 더 작은 것을 골라 모아 놓은 것(h값의 집합) 중 가장 큰 숫자가 정답이 된다.
    return answer

# 다른 사람의 풀이 2
def solution(citations):
    citations = sorted(citations)     # citations 배열을 오름차순으로 정렬한다.
    l = len(citations)     # l은 citations 리스트의 요소 개수
    for i in range(l):     # 0부터 l-1까지 h가 될 수 있는지를 하나하나 따져보기
        if citations[i] >= l-i:     # 만약 citations[i](인용 횟수 = h)가 l-i(h번 이상 인용된 논문 수, citations[i]와 citations[i] 이후에 위치해 있는 요소들의 수)보다 크거나 같은 경우
            return l-i     # 바로 return (i가 작을수록 l-i 값이 큰데, 가장 큰 l-i값을 반환해야 하므로 위 조건을 만족하자마자 반환해야 한다.)
    return 0     # 위에서 return되지 않고 넘어온 경우 (ex) [0, 0, 0]) 0 반환