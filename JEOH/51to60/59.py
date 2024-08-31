import functools
def compare(a,b):
    tl = str(a) + str(b)
    t2 = str(b) + str(a)
    return (int(tl) > int(t2)) - (int(tl) < int(t2))
def solution(numbers):
    sorted_nums = sorted(
        numbers, key=functools.cmp_to_key(lambda a, b: compare(a, b)), reverse=True
    )
    answer = "".join(str(x) for x in sorted_nums)
    return "0" if int(answer) == 0 else answer