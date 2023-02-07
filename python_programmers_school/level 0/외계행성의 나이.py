from string import ascii_lowercase

def solution(age):
    alphabet_list = list(ascii_lowercase)
    age_dict = {}
    num = 0
    i = 0
    transform = []
    
    for alphabet in alphabet_list:
        age_dict[num] = list(ascii_lowercase)[i]
        num += 1
        i+= 1
    
    for index in range(len(str(age))):
        transform.append(age_dict[int(str(age)[index])])
    
    return "".join(transform)

print(solution(23))
print(solution(51))
print(solution(100))

# 다른 풀이 1
# def solution(age):
#     return ''.join([chr(int(i)+97) for i in str(age)])  
# --> chr() 함수는 인자로 받은 정수형을 아스키코드 값으로 받고 해당 코드의 문자를 반환해 준다.(알파벳 소문자는 10진수로 97부터 시작)


# 다른 풀이 2
# def solution(age):
#     str_age = str(age)
#     answer = ''
#     lst = ["a","b","c","d","e","f","g","h","i","j"]
#     for ch in str_age:
#         for i in range(0,10):
#             if int(ch) == i:
#                 answer += lst[i]
#     return answer
