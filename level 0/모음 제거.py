def solution(my_string):
    vowel = ["a", "e", "i", "o", "u"]
    for i in my_string:
        if i in vowel:
            my_string = my_string.replace(i, "")     # 행동만 하는 것이 아니라 행동으로 인해 변경된 값도 넣어주어야 한다. (else pass는 안적어도 됨.)
    return my_string

print(solution("bus"))

# 간단한 풀이
# def solution(my_string):
#   return "".join([i for i in my_string if(i in "aeiou")])
