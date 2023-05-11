# 반복문 (주어진 배열에서 가능한 순열을 만듦.)
def permutation(arr):
    result = [arr[:]]     # 처음 인덱스 생성 (주어진 배열인 arr을 그대로 넣으면 얕은 복사 발생, 배열 안에 배열 들어감)
    c = [0] * len(arr)     # 배열끼리 위치를 바꾸기 위한 인덱스 배열
    i = 0
    while i < len(arr):     # 배열 조작을 위한 반복문 (result 배열 안에 있는 주어진 배열 arr에 대해 조작)
        if c[i] < i:     
            if i % 2 == 0:     # 짝수 인덱스
                arr[0], arr[i] = arr[i], arr[0]     # 데이터 교체
            else:      # 홀수 인덱스
                arr[c[i]], arr[i] = arr[i], arr[c[i]]     # 데이터 교체
            result.append(arr[:])     # 새로운 초기 데이터 생성 (주어진 배열 arr 그대로 result에 추가)
            c[i] += 1     # 다음 바꿀 인덱스 추가
            i = 0     # 초기화
        else:
            c[i] = 0
            i += 1
    return result

print(permutation([1, 2, 3]))

# 다음과 같이 스택 자료구조를 이용해서도 구현이 가능하다. (아래의 재귀를 반복문으로 구현한 것)
def permutations(lst):
    stack = [(lst, [])]
    result = []
    while stack:
        items, perm = stack.pop()
        if not items:
            result.append(perm)
        else:
            for i in range(len(items)):
                new_items = items[:i] + items[i+1:]
                new_perm = perm + [items[i]]
                stack.append((new_items, new_perm))
    return result


# 재귀로 구현 (하노이의 탑 원리와 비슷!)
# 숫자 하나를 골라 (여기서는 for문을 이용하여 인덱스 0번부터 숫자 탐색) 그것을 맨 앞에 둠.
# 그리고 그 숫자를 제외한 나머지 숫자들은 다시 permutations에 인자(리스트)로 넣어 같은 원리로 배치를 한다.
# 나머지 숫자가 1개가 되어 permutations에 들어가는 인자의 길이가 1이 되면 더 이상 위와 같은 작업을 할 수 없으므로
# [lst(그 인자)] 반환, result에 들어가는 것은 현재 [element] + 아까 반환된 인자 리스트
# lst의 길이가 0일 수도 있으므로 이때는 빈 배열 반환
# 맨 앞에 위치하는 숫자는 for i in range(len(lst))에 의해 바뀜!
def permutations(lst):
    # base case
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    result = []
    for i in range(len(lst)):
        elem = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for p in permutations(remaining):
            result.append([elem] + p)
    return result