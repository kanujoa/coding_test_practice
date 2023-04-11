def solution(k, score):
    honor = []
    result = []
    for i in range(len(score)):
        if i < k:
            honor.append(score[i])
            result.append(min(honor))
        else:
            if min(honor) < score[i]:
                honor[honor.index(min(honor))] = score[i]
            result.append(min(honor))
    return result



# 더 간단한 풀이
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer


# 자료구조 heap을 이용한 풀이 (heap은 최솟값, 최댓값을 빠르게 찾아낼 수 있는 완전이진트리 기본 자료구조이다.)
import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])     # max_heap 리스트에서 k번째로 작은 요소의 1번째 값을 answer에 append함.

    return answer
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))