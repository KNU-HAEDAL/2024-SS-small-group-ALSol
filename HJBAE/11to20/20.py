"""
한 명 제외하고 모든 선수가 완주함
마라톤에 참여한 선수들 이름 담긴 배열 participant
완주한 선수들의 이름이 담긴 배열 completion
완주하지 못한 선수의 이름을 반환하는 solution() 함수

마라톤 경기에 참여한 선수 수는 1명 이상 100000명 이하
completion 길이는 participant 길이보다 1 작음
참가자 이름은 1개 이상 20개 이하의 알파벳 소문자
참가자 중 동명이인 ㄱㄴ
"""

def solution(participant, completion):
    completion_check = {}

    for part in participant:
        if part in completion_check:
            completion_check[part] += 1
        else:
            completion_check[part] = 1
    
    for comp in completion:
        completion_check[comp] -= 1
    
    for athelte in completion_check.keys():
        if completion_check[athelte] > 0:
            return athelte

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
#return = ["leo"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
#return = ["vinko"]
participant3 = ["mislav", "stanko", "mislav", "ana"]    #동명이인 존재 case
completion3 = ["stanko", "ana", "mislav"]
#return = ["mislav"]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))