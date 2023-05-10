# 포인트 1
# 한 딕셔너리에서 key값은 할당된 방 번호로, value값은 중복되는 방 번호가 나왔을 경우 다음에 할당될 
# 방 번호로 정하였다.


# 포인트 2
# visit 배열을 생성해 방문한 방들은 모두 배열에 넣어 나중에 그 key들의 값을 모두 할당된 새 방 번호 + 1로
# 업데이트하였다. (마지막에 할당된 방은 새 방이므로 value 업데이트가 아닌 room_dic에 새로 추가되는 것)

def solution(k, room_number):
    room_dic = {}     # 할당된 방 dic
    ret = []
    for i in room_number:
        n = i
        visit = [n]     # 방문한 방 번호 배열
        while n in room_dic:     # 현재 room number가 할당된 방 dic에 존재할 동안
            n = room_dic[n]     # 현재 방(n)은 room_dic[n](현재 방 번호의 값으로 저장된 다음 방번호)으로 업데이트 
            visit.append(n)     # visit 배열에 n 추가 
        ret.append(n)     # 현재 room number가 할당된 방 dic에 존재하지 않을 경우
        for j in visit: room_dic[j] = n + 1     # room_dic에 현재 방을 key로, 현재 방 번호 + 1을 값으로, 즉 다음 방으로 지정
    return ret

print(solution(10, [1,3,4,1,3,1]))