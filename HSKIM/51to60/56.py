def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(['abce','abcd', 'cdx'],1))