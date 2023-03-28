def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in num:
        if i in s:     # 이 if 문을 굳이 쓰지 않아도 된다.
            s = s.replace(i, str(num.index(i)))
    return int(s)

# enumerate 사용하기기
# def solution(s):
#     words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

#     for i, j in enumerate(words):
#         s = s.replace(j, str(i))

#     return int(s)