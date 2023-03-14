def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
        except:
            return False
        return True
    return False    

# 예외처리 더 깔끔하게 작성하기
# def alpha_string46(s):
#     try:
#         int(s)     # 우선 입력을 int로 변환하는 것 먼저!
#     except:     # 변환에 실패해서 ValueError가 뜨면
#         return False     # False 반환
#     return len(s) == 4 or len(s) == 6     # 예외처리 구문을 잘 빠져나오면 s의 길이 확인, 조건을 만족하면 자동으로 True 반환 

# isdigit을 활용한 풀이
# def alpha_string46(s):
#     return s.isdigit() and len(s) in [4,6]     # isdigit: 문자열이 숫자로만 이루어져 있는지를 확인하는 함수