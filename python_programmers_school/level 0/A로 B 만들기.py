def solution(before, after):
    if sorted(before) == sorted(after):     # 정렬해서 같으면 순서만 바꾸면 같은 문자열로 만들 수 있다는 뜻(즉, 존재하는 문자의 종류와 개수만 같으면 됨.)
        return 1
    else:
        return 0

# if-else문 한줄로 적기
# def solution(before, after):
#     return 1 if sorted(before)==sorted(after) else 0