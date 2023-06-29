t = int(input())

def recursion(s, l, r,cnt):
    if l >= r: 
        print(1, cnt)
    elif s[l] != s[r]: 
        print(0, cnt)
    else:
        return recursion(s, l+1, r-1, cnt + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)
    
for _ in range(t):
    word = input()
    isPalindrome(word)