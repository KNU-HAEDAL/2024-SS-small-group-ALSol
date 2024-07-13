def solution(participant, completion):
    hash_table = dict()
    #key값은 이름, value는 0으로 초기화
    for i in participant:
        if i not in hash_table:
            hash_table[i] = 0
        else:
            hash_table[i] += 1
        
    '''for j in range(len(completion)):
        if  completion[j] in hash_table:
            hash_table[completion[j]] += 1'''
    
    for j in completion:
        hash_table[j] += 1

    for key in hash_table:
        if hash_table[key] != 1:
            return key
  
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
#solution(participant, completion)