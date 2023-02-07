def solution(array, n):
    array.sort()     # 주어지는 array는 오름차순이 아닐수도 있으므로 먼저 오름차순으로 배열시키기!
    gap = [abs(i-n) for i in array]
    return array[gap.index(min(gap))]     # 이미 오름차순으로 배열시켰으므로 gap 앞부분으로 갈수록 array의 작은 수와 매치됨.

# a = [1, 2, 2, 2]
# print(a.index(2))     --> index 메소드는 리스트에 중복된 요소가 있을 경우에는 가장 앞 요소의 index값을 반환함.

# 중요한 전제: 주어지는 array는 오름차순이 아닐수도 있음! (문제에 오름차순이라는 말이 나와있지 않으면 그렇지 않은 경우가 있을 수 있음을 염두해 두어야 함.)