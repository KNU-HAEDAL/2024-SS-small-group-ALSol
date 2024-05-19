import random

answer = [random.randint(1, 5) for _ in range(100)]
# answer.append(random.randint(1, 5)) 으로 하려고 했는데 list comprehension 하면 더 간결하게 된대서 써봄

patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

# 찍는 패턴 만듦.. 간결하게 될 것 같은데..

def solution(pattern):
    score = [[0] for _ in range(3)]
    
    for i in range(len(pattern)):   #len(pattern) == 3
       for j in range(100):
           if (pattern[i][j % len([pattern])] == answer[j]):
               score[i][0] += 1
    
    max_score = max(score)
    max_score_index = score.index(max_score)


    return max_score_index, max_score[0]

mvp_index, max_score = solution(patterns)

print(f"winner is player {mvp_index + 1} & score is {max_score}")