def solution(answers):
    answer = []
    name=[1,2,3]
    score=[0,0,0]
    result1=[1,2,3,4,5]
    result2=[2,1,2,3,2,4,2,5]
    result3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==result1[i%len(result1)]:
            score[0]+=1 
        if answers[i]==result2[i%len(result2)]:
            score[1]+=1
        if answers[i]==result3[i%len(result3)]:
            score[2]+=1
    for k in range(len(score)):
        if score[k]==max(score):
            answer.append(k+1)
    return answer