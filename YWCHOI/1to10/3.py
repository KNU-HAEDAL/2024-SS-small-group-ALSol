def solution(ary) :
    rary = []
    for i in range (0, len(ary)) :
        for j in range (i + 1, len(ary)) :
            rary.append(ary[i] + ary[j])
    rary.sorted(set(rary))
    return rary