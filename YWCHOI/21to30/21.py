# p.226

def solution(want, number, discount):
    want_dictionary = {}
    for i in range(len(want)):
        want_dictionary[want[i]] = number[i]

    result = 0
    for j in range(len(discount) - 9):
        dis = {}

        for k in range(j, j + 10):
            if discount[k] in want_dictionary:
                dis[discount[k]] = dis.get(discount[j], 0) + 1
        
        if dis == want_dictionary:
            result += 1

    return result