def solution(ary) :
    rary = []
    for i in range (0, len(ary)) :
        for j in range (i + 1, len(ary)) :
            rary.append(ary[i] + ary[j])
    rary.sorted(set(rary)) # set을 sorted의 인자로 넣으면 
    return rary