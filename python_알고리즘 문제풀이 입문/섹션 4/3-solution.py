# 구해야 할 것은 dvd의 '최소' 용량 크기!
import sys
input = sys.stdin.readline

def Count(capacity):
    cnt = 1     # dvd 장수(최소 1번은 저장되므로 1부터 시작, 용량이 초과될 때마다 1씩 증가시킬 것임.)
    sum = 0     # 노래들의 길이를 합함
    for x in Music:     
        if sum + x > capacity:     # sum에 x를 더했는데 capacity(mid)보다 크게 되면 dvd 용량 초과이므로 불가하다.
            cnt += 1     # 따라서 dvd 장수를 하나 더 늘리고
            sum = x     # 거기에 x를 저장한다. (--> sum은 x부터 시작한다.)
        else:     # sum에 x를 더했는데 capacity보다 작거나 같으면 
            sum += x     # 계속 더해나감
    return cnt     # 필요한 dvd의 개수 반환

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)     # 노래들 중 가장 긴 용량의 노래
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:     # 필요한 dvd의 개수가 m보다 작거나 같으면 (ex) m이 3인데 Count(mid)가 2인 경우, 2장 안에 다 저장할 수 있으므로 당연히 3장에도 저장이 된다.) 
    # 그리고 mid >= maxx를 해 줌으로써 mid는 최소한 maxx 한 곡을 다 담을 수 있을 만한 용량이라는 조건도 작성해 주었다. 
        res = mid
        rt = mid - 1     # 최소 용량을 찾아야 하므로 mid가 감소해야 하니까 rt를 mid 바로 앞 숫자로 옮긴다.
    else:     # 필요한 dvd의 개수가 m보다 크거나 mid가 maxx 용량보다 작으면
        lt = mid + 1     # 용량(노래의 길이)이 증가해야 하므로 lt를 mid 바로 뒤 숫자로 옮긴다.

print(res)