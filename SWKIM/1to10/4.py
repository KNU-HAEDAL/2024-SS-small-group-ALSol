def solution(answer):
    result = []

    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]

    for i in range(len(answer)):
        if answer[i] == person1[i % 5]:
            score[0] += 1
        
        if answer[i] == person2[i % 8]:
            score[1] += 1
        
        if answer[i] == person3[i % 10]:
            score[2] += 1
    
    max_score = max(score)

    for i in range(3):
        if score[i] == max_score:
            result.append(i+1)
    
    return result
        

