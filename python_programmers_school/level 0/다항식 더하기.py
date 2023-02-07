def solution(polynomial):
    b = polynomial.split(" + ")
    
    for i in range(len(b)):
        if b[i] == "x":
            b[i] = "1x"
            
    c = 0
    d = 0
    for i in b:
        if "x" in i:
            i = i.replace("x", "")
            c += int(i)
        else:
            d += int(i)
    
    if c == 0:
        if d == 0:
            return 0
        else:
            return (f"{d}")
    elif c == 1:
        if d == 0:
            return "x"
        else:
            return (f"x + {d}")
    else:
        if d == 0:
            return (f"{c}x")
        else:
            return (f"{c}x + {d}")