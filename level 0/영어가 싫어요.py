def solution(numbers):
    num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key in num.keys():
        if key in numbers:
            numbers = numbers.replace(key, num[key])
    return numbers

print(solution("onefourzerosixseven"))

# 효율적인 코드
# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):     --> enumerate를 이용해 num에 index를, enf에 리스트 안의 string들을 할당함. (0부터 인덱싱됨.)
#         numbers = numbers.replace(eng, str(num))     --> 문자열 부분을 해당 인덱스로 치환함.
#     return int(numbers)