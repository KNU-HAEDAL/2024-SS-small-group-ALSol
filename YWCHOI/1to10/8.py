def solution():
    parenthesis_stack = []
    s = input()
    # parenthesis_stack.append(s)
    s_length = len(s)
    # print(parenthesis_stack)

    for letter in range(0, s_length):
        if s[letter] == '(':
            parenthesis_stack.append(s[letter])
        if s[letter] == ')':
            if len(parenthesis_stack) != 0:
                parenthesis_stack.pop()
            else:
                return False
    
    if len(parenthesis_stack) == 0:
        return True
    else:
        return False

print(solution())