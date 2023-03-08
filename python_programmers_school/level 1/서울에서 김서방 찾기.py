def solution(seoul):
    kim = seoul.index("Kim")
    return f"김서방은 {kim}에 있다"     # 포맷팅 부분에 seoul.index("Kim")이 그대로 들어가는 것은 불가하다. 따라서 kim 변수에 넣어 그 변수를 사용해 주었다.

# 줄여서 적는 방법
# def findKim(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))     --> {}을 만들어 놓고 뒤에서 .format()메서드 사용하기 (안에 인덱스 찾는 코드 작성)
