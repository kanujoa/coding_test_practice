# 두 리스트의 길이 차이가 1이므로 두 리스트 정렬하여 순서를 똑같이 만든 후 요소가 달라지는 부분에서 완주 못한 1명을 찾아내는 방법을 사용하였다.
def solution(participant, completion):
    participant.sort()     # participant 참가자 이름 알파벳 순서대로 정렬     
    completion.sort()     # completion 참가자 이름 알파벳 순서대로 정렬
    for i in range(len(completion)):     # i는 인덱스
        if participant[i] != completion[i]:     # participant[i]와 completion[i]가 달라지는 부분은 participant[i]가 완주를 하지 못했다는 의미이므로
            return participant[i]     # participant[i]를 return하고 끝낸다.
    else:     # 인덱스 i는 participant보다 길이가 1 짧은 completion의 길이 이전까지의 범위이므로 위 for문을 그냥 통과한 경우
        return participant[-1]     # participant의 마지막 참가자가 완주를 하지 못한 것이므로 participant[-1]을 return하고 끝낸다.

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


# 효율성 테스트 통과해야 하므로 아래의 코드는 불가!
# def solution(participant, completion):
#     while len(participant) != 1:
#         for p in participant:
#             if p in completion:
#                 participant.remove(p)
#                 completion.remove(p)
#     return participant[0]


# 다른 풀이 1 (Collection 모듈 사용하기)
# Counter 함수에 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 된다.
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)     # 연산 가능!
    # print(collections.Counter(participant))     --> Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    # print(collections.Counter(completion))     --> Counter({'stanko': 1, 'ana': 1, 'mislav': 1})
    # print(answer)     --> Counter({'mislav': 1})
    return list(answer.keys())[0]


# 다른 풀이 2 (dictionary 이용)
# python에서는 Dictionary라는 자료구조를 통해 해시를 구현할 수 있다.
# List에 비해 Dictionary가 매우 빠른 시간복잡도를 가져 원소를 넣거나 삭제, 찾는 일이 많을 때에는 딕셔너리를 사용하는 것이 좋다.
# hash() 함수 : 개체에 해시 값이 있는 경우 해당 개체의 해시 값을 반환, dictionary를 보면서 빠르게 dictionary 키를 비교하는 데 사용되는 '정수'
# but 이 방법은 찾아야 하는 사람이 1명인 경우에만 사용 가능 (해시 충돌 때문에)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part     # 문자열 part(participant 요소 하나하나)의 hash 값이 키가 되고 part가 값이 되어 dic의 원소로 추가됨.
        temp += int(hash(part))     # temp에는 dic의 키 값인 해시 값을 하나씩 모두 더한다.
    for com in completion:     
        temp -= hash(com)     # completion에 있는 요소들(문자열, 참가자)의 해시 값을 temp에서 하나씩 뺀다. (같은 문자열일 경우, 해시값이 같다.)
    answer = dic[temp]     # 마지막에는 완주에 실패한 사람의 키인 해시값 하나만 남게 되는데 그것으로 정답을 구한다.

    return answer
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
