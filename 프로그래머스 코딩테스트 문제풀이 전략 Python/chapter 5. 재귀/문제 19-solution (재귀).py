import sys
sys.setrecursionlimit(2000)

def find_emptyroom(chk, rooms):
    if chk not in rooms:     # 해당 방 데이터가 없음, 새 방 할당이 가능함.
        rooms[chk] = chk + 1     # 다음 방이 비었다고 명시
        return chk     # 현재 위치를 반환
    empty = find_emptyroom(rooms[chk], rooms)  
    rooms[chk] = empty + 1     # 앞서 병시한 다음 방을 똑같이 따라감
    return empty


def solution(k, room_number):
    rooms = dict()     # 방 정보를 모두 담는 것이 아니라, 할당된 방 정보만 저장
    for num in room_number:     # 모든 고객이 요구하는 방을
        chk_in = find_emptyroom(num, rooms)     # 탐색하여 결괏값을 기록
    return list(rooms)     # 모든 결과를 반환