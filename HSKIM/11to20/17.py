from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.pop()
            goal.pop()
        elif cards2 and cards2[0] == goal[0]:
            cards2.pop()
            goal.pop()
        else:
            break

    return "Yes" if not goal else "No"