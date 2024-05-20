'''
def solution(answers) :
    b = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * 3  # 이거랑 s = [[0],[0],[0]] 이거랑 다른건가..?

    for i, answer in enumerate(answers) :
        for j, b in enumerate(b) :
            if answer == b[i % len(b)] :
                s[j] += 1
    
    max = max(s)
    ss = []

    for i, sc in enumerate(s) :  # 갑자기 다른 변수가..?
        if sc == max :
            ss.append(i + 1)
        
    return ss
    '''

def solution(answers) :
    betting = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]
    res = []

    for i, a in enumerate(answers) :
        for j, b in enumerate(betting) : 
            if a == betting[j][i % len(betting[j])] :
                scores[j] += 1


    for i, s in enumerate(scores) :
        if s == max(scores) :
            res.append(i + 1)

    return res