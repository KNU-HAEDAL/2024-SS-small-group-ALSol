from collections import deque

def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)

    # 문장 완성이 정상적으로 되지 않으면 "No"를 반환
    for i in goal:
        if len(c1) > 0 and i == c1[0]:
            c1.popleft()
        elif len(c2) > 0 and i == c2[0]:
            c2.popleft()
        else:
            return "No"
    
    # 정상적으로 문장이 완성되므로 "Yes" 반환
    return "Yes"

# print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))