def solution(participant, completion):
    marathon = {}
    answer = ""

    # 완주자들을 dict에 추가, 동명이인은 value 값 증가로 구분
    for i in completion:
        if i in marathon:
            marathon[i] += 1
        else:
            marathon[i] = 1      

    # 참여자가 dict에 없거나 value 값이 0인 경우 미완주자로 결정
    for i in participant:
        if i not in marathon or marathon[i] == 0:
            answer = i
            break
        else:
            marathon[i] -= 1

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["mislav", "stanko", "ana"]))