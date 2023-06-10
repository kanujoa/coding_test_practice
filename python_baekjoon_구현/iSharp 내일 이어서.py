declare = input().split()
for i in range(1, len(declare)):
    declare[i] = declare[i][:-1]
for i in range(1, len(declare)):
    basic_var = declare[0] 
    item = list(declare[i])
    var = ''
    var_type = []
    for i in item:
        if  97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
            var += i
        else:
            break
    if len(var) != len(item):
        for i in range(len(item) - 1 , len(var) - 1, -1):
            if item[i] == '[':
                var_type[-1] = '['
                var_type.append(']') 
            else:
                var_type.append(item[i])
    else:
        var_type = ''
    print(f'{basic_var}{"".join(var_type)} {var};')