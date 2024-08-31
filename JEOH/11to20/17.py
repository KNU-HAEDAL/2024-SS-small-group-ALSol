from collections import deque
def solution(cardsl, cards2, goal):
    cardsl = deque(cardsl)
    cards2 = deque(cards2) 
    goal = deque(goal)
    while goal:
        if cardsl and cardsl[0] == goal[0]: 
            cardsl.popleft() 
            goal.popleftO
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft() 
            goal.popleftO
        else:
            break 
    return "Yes" if not goal else "No" 