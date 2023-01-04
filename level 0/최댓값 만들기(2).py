def solution(numbers):
    s = sorted(numbers)     # 일단 리스트 오름차순으로 정렬
    if s[-1]*s[-2] > s[0]*s[1]:     # 왼쪽은 양수 중 첫 번째로 큰 수와 두 번째로 큰 수를 곱한 값, 오른쪽은 음수 중에 가장 작은 값과 그 다음으로 작은 값을 곱한 값
        return s[-1]*s[-2]      # 곱하면 양수가 되는 경우(양수*양수, 음수*음수 를 모두 생각해 주어야 함.)
    else:
        return s[0]*s[1]
# 곱하는 모든 경우의 수를 담기 위해 for문 쓰면 런타임 에러 발생

# 비슷한 풀이
# def solution(numbers):
#     numbers = sorted(numbers)
#     return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])     --> 내가 사용한 if문, else문 내용을 한 줄로 작성할 수 있는 방법