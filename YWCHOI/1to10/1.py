def solution1(ary) :
    ary.sort()
    return ary

def solution2(ary):
    slist = list(sorted(ary))
    return slist

print(solution1([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
print(solution1([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution1([1,6,7])) # 반환값 : [1, 6, 7]

print(solution2([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
print(solution2([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution2([1,6,7])) # 반환값 : [1, 6, 7]