def step_1(new_id):
    return new_id.lower()

def step_2(new_id):
    for letter in new_id:
        if letter == '-' or letter == '_' or letter == '.' or letter.isdigit() or letter.islower():
            continue
        else:
            new_id = new_id.replace(letter, '', 1)
    return new_id

def step_3(new_id):
    stack = []
    for letter in new_id:
        if len(stack) == 0:
            stack.append(letter)
        elif stack[-1] == '.' and letter == '.':
            pass
        else:
            stack.append(letter)
    return ''.join(stack)

def step_4(new_id):
    if len(new_id) != 0  and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
    return new_id
    
def step_5(new_id):
    if len(new_id) == 0:
        new_id = 'a'
    return new_id

def step_6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:14]
    return new_id

def step_7(new_id):
    if len(new_id) <= 2:
        new_id += (new_id[-1] * (3 - len(new_id))) 
    return new_id
    
def solution(new_id):
    new_id = step_1(new_id)
    new_id = step_2(new_id)
    new_id = step_3(new_id)
    new_id = step_4(new_id)
    new_id = step_5(new_id)
    new_id = step_6(new_id)
    return step_7(new_id)

print(solution("...!@BaT#*..y.abcdefghijklm"))