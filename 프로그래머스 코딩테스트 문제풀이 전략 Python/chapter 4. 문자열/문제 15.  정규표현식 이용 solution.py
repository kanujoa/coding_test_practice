import re

def solution(phone_number):
    return re.sub('\d(?=\d{4})', '*', phone_number)
# 긍정형 전방 탐색을 이용해 sub() 함수로 탐색된 단어 이외의 모든 단어를 *로 치환하였다.
# \d는 해당하는 모든 숫자를 검색하고, 곧이어 긍정 전방 탐색으로 검색된 결과의 마지막 4글자를 제외해서
# 글자 길이에 상관없이 정확히 나머지를 *로 치환한다.