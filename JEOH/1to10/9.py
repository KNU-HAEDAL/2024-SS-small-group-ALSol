def solution(num):
    stack=[]
    while num>1:
        a=num%2
        num=num//2
        stack.append(str(a))
    stack.append(str(num))
    stack.reverse()
    bin=''.join(stack)
    return bin
