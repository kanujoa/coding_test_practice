# 둘 다 효율성 테스트에서 통과 X
def solution(k, room_number):
    result = []
    assign = {}
    for num in room_number:
        if num in assign:
            while num <= k:
                num += 1
                if num not in assign:
                    assign[num] = 1
                    break
        else:
            assign[num] = 1
        result.append(num)
    return result

# 반복문 solution과 비슷한 풀이!
# 아래의 코드에서 visit 배열을 생성해 방문한 방들을 모아 그것들의 값을 똑같이 업데이트 시키면 됨. (이걸 놓침...)
# 그리고 딕셔너리 1개로 처리하는게 더 편함.

def solution(k, room_number):
    result = []
    assign = {}
    next_assign = {}
    for num in room_number:
        if num in assign:
            check = next_assign[num]
            while True:
                if check in assign:
                    check = next_assign[check]
                else:
                    assign[check] = 1
                    next_assign[check] = check + 1
                    result.append(check)
                    break
        else:
            assign[num] = 1
            next_assign[num] = num + 1
            result.append(num)
    return result

print(solution(10, [1,3,4,1,3,1]))