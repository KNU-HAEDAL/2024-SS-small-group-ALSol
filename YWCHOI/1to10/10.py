# p.145

def solution(s):
    correct_brackets = 0
    s_length = len(s)
    brackets_stack = [s]
    # print(brackets_stack) # 스택 생성 확인 코드

    for i in range(s_length):
        brackets_stack.append(s[i])

        if (brackets_stack[-2] == "(" and brackets_stack[-1] == ")") or (brackets_stack[-2] == "{" and brackets_stack[-1] == "}") or brackets_stack[-2] == "[" and brackets_stack[-1] == "]":
            brackets_stack.pop()
            brackets_stack.pop()
            correct_brackets += 1
            
    return correct_brackets

s = input()
print(solution(s))