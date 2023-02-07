def solution(my_string):
    return my_string[::-1]


# 만약에 reverse를 쓰고 싶다면 다음과 같이 사용해야 한다. list.reverse()(동작) 자체를 반환하면 결과로 None이 나온다.
# def solution(num_list):
#     num_list.reverse()    
#     return num_list     --> 동작의 결과를 반환해야 한다.(특정한 값이 있는 것을 return해야 우리가 원하는 답이 나온다.)