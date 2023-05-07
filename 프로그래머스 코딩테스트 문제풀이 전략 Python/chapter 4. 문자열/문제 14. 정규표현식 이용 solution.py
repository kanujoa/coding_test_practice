# 1. 조건문 이후 정규표현식 사용
import re

def solution(s):
    return len(s) in {4, 6} and bool(re.match('^[0-9*$]', s))
# 첫 문자(^)가 숫자 중 하나([0-9])리고, 그 숫자가 반복되어(*) 끝까지 유지됨.($)

# 2. 조건문을 사용하지 않고 정규표현식 사용
import re

def solution(s):
    return bool(re.match('^(\d{4}|\d{6})$', s))
# 주어진 문자열이 숫자 4개(\d{4}) 또는(|) 6개(\d{6})인지 판단하는 그룹을 생성

# 둘 다 시작(^)과 끝($)을 적어주기