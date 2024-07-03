# 아직 덜 됐어요.. 계속 [6, 3, 4, 2, 1, 5] 가 떠요..

# <문제 파악>
# stages의 원소 중 i 이상 숫자의 개수를 분모로,
# i 이하 숫자의 개수를 분자로 하는 분수를 표현하면 됨

def solution(stages) :
    # 결과를 담을 리스트 선언
    res = []
    index_res = []

    # 단계는 1 ~ max(stages)까지 존재
    for i in range (1, max(stages) + 1) :
        cnt_denominator = 0
        cnt_numerator = 0

        # stages의 원소를 순회하면서 검사
        for j in stages :
            if j >= i :
                cnt_denominator += 1  # 다 좋은데 왜 파이썬에는 ++가 없을까..
            if j == i :
                cnt_numerator += 1

        # 0으로 나누는 경우 
        if cnt_denominator > 0 : 
            res.append(cnt_numerator / cnt_denominator)
        else :
            res.append(0)

        index_res.append(i)
        
    sorted_index = sorted(range(len(res)), key = lambda x : (-res[x], index_res[x]))
    sorted_res = [index_res[i] for i in sorted_index]
    
    return sorted_res

# tester
print(solution([2, 1, 2, 6, 2, 4, 3, 3]))