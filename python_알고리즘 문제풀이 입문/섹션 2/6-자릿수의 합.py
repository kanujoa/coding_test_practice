N = int(input())     # 자연수 개수 N 입력
nums = list(map(int, input().split()))     # 입력받은 N개의 자연수들을 리스트로 만듦  

def digit_sum(x):     # 각 자연수의 자릿수의 합을 구하는 함수(인수로 들어갈 것은 위에서 만든 숫자 '리스트' x)
  sum_res = -2147000000     # sum_res 초깃값 설정 (가장 작은 값)
  index = 0     # index 초깃값 설정 (맨 앞부분인 0으로 설정)
  for idx, num in enumerate(x):     # idx는 x 리스트의 인덱스, num은 x 리스트에서의 idx 부분의 값
    sum = 0     # 자릿수 합 sum의 초깃값 0
    for i in str(num):     # x의 요소 하나인 num을 str로 형변환해 i 변수에 하나씩 넣음.
      sum += int(i)     # sum에 str에서 int로 형변환한 i를 하나씩 누적해서 더해줌.
      if sum > sum_res:     # sum이 이전 sum 값인 sum_res보다 크면
        sum_res = sum     # sum_res를 sum으로 업뎃
        index = idx     # index도 현재 인덱스인 idx로 업뎃
# 자릿수의 합이 같을 경우 위에서 만족되는 조건이 없으므로 자동으로 pass되게 됨.

  return x[index]     # 반환되는 값은 x 리스트에서의 최종 index번째 요소

print(digit_sum(nums))