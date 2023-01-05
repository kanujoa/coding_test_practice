def solution(numbers, direction):
    if direction == "right":
        for i in range(len(numbers)-1):
            numbers[-1], numbers[i] = numbers[i], numbers[-1]
        return numbers
    else:
        i = len(numbers)-1
        while i > 0:
            numbers[0], numbers[i] = numbers[i], numbers[0]
            i -= 1
        return numbers


print(solution([4, 455, 6, 4, -1, 45, 6], "left"))

# 간단한 풀이 (리스트 연산(덧셈) 사용)
# def solution(numbers, direction):
#     return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
# 방향 입력값이 right일 때는 가장 마지막에 있는 요소 + 나머지 요소 (가장 마지막 요소를 가장 처음으로)
# 방향 입력값이 left일 때는 가장 처음에 있는 요소 + 나머지 요소 (가장 처음 요소를 가장 마지막으로)
# 리스트 형태로 반환해야 하므로 []로 감싸주기