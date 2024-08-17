def solution(amount):
    answer = []

    # 100, 50, 10, 1 단위로 구분해 화폐가 가장 적게 쓰이도록 함
    while amount > 0:
        if amount >= 100:
            amount -= 100
            answer.append(100)
        elif amount >= 50:
            amount -= 50
            answer.append(50)
        elif amount >= 10:
            amount -= 10
            answer.append(10)
        else:
            amount -= 1
            answer.append(1)
    
    return answer

print(solution(350))
        