# 윤년은 2월이 29일까지 있다.

def solution(a, b):
    m = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8 : 31, 9: 30, 10: 31, 11: 30, 12: 31}
    d = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    if a == 1:
        return d[b % 7 - 1]      
    else:
        s = 0      
        for i in range(1, a):
            s += m[i]
        s += b
        return d[s % 7 - 1]     
print(solution(1, 2))
print(solution(5, 24))
print(solution(12, 31))


# 간단하게 작성하기 (month와 day를 모두 리스트로 만들었다.)
# def getDayName(a,b):
#     month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     return day[(sum(month[:a-1])+b-1)%7]     # month[:a-1]로 슬라이싱하여 그 범위의 날들을 모두 더하고 b를 더한 후 1을 뺀 값을 7로 나눈 나머지를 day의 index로 하면 된다.
# a-1이 0인 경우 sum값이 0이기 때문에 1월도 한번에 계산 가능

# 모듈 불러오기 (datetime)
# import datetime

# def getDayName(a,b):
#     t = 'MON TUE WED THU FRI SAT SUN'.split()     --> t는 요일들을 요소로 하는 리스트
#     return t[datetime.datetime(2016, a, b).weekday()]     --> datetime.datetime(2016(년), a(입력받은 월), b(입력받은 일)).weekday()를 t의 인덱스로 한 값을 반환
# weekday() 메서드는 각 요일의 번호를 반환 (Monday 부터 Sunday 까지 차례대로 0 ~ 6)