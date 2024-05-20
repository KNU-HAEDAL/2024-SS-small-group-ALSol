def solution(ary):
    s_list = list(set(ary))
    s_list.sort(reverse = True)
    return s_list

print(solution([1, 1, 7, 3, 4, 6, 2, 3]))