# 진법 변환 함수
def radixChange(num, radix):
    if num == 0: return '0'     # 입력값이 0이면 0 반환
    nums = []
    while num:
        num, digit = divmod(num, radix)     # divmod(숫자, 진법)은 숫자를 진법의 숫자로 나눈 몫과 나머지를 차례로 튜플에 담아서 반환
        nums.append(str(digit))     # nums 리스트에 진법 변화의 과정에 해당하는 digit 수를 str type으로 바꾸어 추가하기
    return ''.join(reversed(nums))     # nums 리스트를 뒤집어 합친 결과가 진법 변환한 결과

def solution(n):
    return int(radixChange(n, 3)[::-1], 3)     
    # n을 3진법으로 변환해 주어야 하므로 radixChange 함수에 n과 3을 인자로 넣어주고, 그 결과를
    # 뒤집은 것을 10진법으로 변환해야 하므로 [::-1]으로 슬라이싱 후 int함수에 3과 함께 인자로 넣었다.