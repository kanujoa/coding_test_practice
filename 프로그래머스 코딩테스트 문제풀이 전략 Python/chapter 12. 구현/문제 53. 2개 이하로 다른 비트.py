# 아래처럼 규칙을 찾지 않고 일일이 살펴보는 식으로 진행하면 시간초과가 난다.
def solution(numbers):
    answer = []
    for num in numbers:
        binary = str(bin(num)[2:])
        add = 1
        while True:
            new_num = str(bin(num + add))[2:]
            if len(new_num) > len(binary):
                binary = '0' * (len(new_num) - len(binary)) + binary
            cnt = 0
            for i in range(len(binary)):
                if new_num[i] != binary[i]:
                    cnt += 1
            if cnt <= 2:
                answer.append(int(new_num, 2))
                break
            else:
                add += 1
    return answer
    
print(solution([2, 7]))

# 다음 코드처럼 주어진 수가 홀수인 경우와 짝수인 경우를 나누어 각각의 경우에서 주어진 숫자와 각 숫자보다 크면서 비트가 1~2개 다른 수들 중에서 제일 작은 수 사이의 규칙을 찾아야 한다.
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            num = f'0{bin(num)[2:]}'
            num = f"{num[:num.rindex('0')]}10{num[num.rindex('0') + 2:]}"
            answer.append(int(num, 2))
    return answer