import re     # 파이썬 정규 표현식 지원 모듈

def solution(my_string):
    numbers = re.sub(r'[^0-9]','', my_string)     # sub 메서드: 패턴 대체하기, []: 문자 클래스, r(raw string): 컴파일 해야 하는 정규식이 순수한 문자임을 알려줌. 
                                                   # ^: 문자열의 시작 의미, 0-9: 0부터 9까지의 숫자('and'가 아닌 'or'로 매칭됨.)
                                                   # resub(정규 표현식, 치환 문자, 대상 문자열), 결과로 str type의 숫자들이 나옴.
    return sum([int(i) for i in numbers])

print(solution("aAb1B2cC34oOp"))

# 다른 풀이 1
# def solution(my_string):
#     return sum(int(i) for i in my_string if i.isdigit())     --> isdigit 메서드는 문자열이 숫자로 구성되어 있는지를 판별해주는 함수
                                                             # --> but 음수나 소숫점이 있을 경우에는 숫자임에도 False를 반환한다.

# 다른 풀이 2
# import re

# def solution(my_string):
#     return sum(int(n) for n in re.sub('[^1-9]', '', my_string))     --> 나처럼 리스트에 담아서 sum하지 않아도 된다.
                                                                    # --> sum함수의 인자로 iterable한 자료형(리스트, 튜플 등)만 들어갈 수 있다.