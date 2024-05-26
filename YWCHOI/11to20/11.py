def solution(s) :
    i = 0
    while len(s) :
        if i == len(s) : break
        if s[i] == s[i + 1] :
            s[i].pop()
            s[i + 1].pop()
            continue
        else : i += 1
    
    if s :
        return 1
    else :
        return 0