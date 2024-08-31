'''
from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)   # 오호.. 자기자신을 인자로 deque 만드는 게 가능하구나..
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        if cards1[0] == goal[0] and len(cards1) != 0:
            goal.popleft()
            cards1.popleft()
        elif cards2[0] == goal[0] and len(cards2) != 0:
            goal.popleft()
            cards2.popleft()
        else:
            return "No"


    return "Yes"
'''
'''
# 왜 2개 중에 하나만 성공했을까?

비어있는지 먼저 확인해야 하군요..
'''

from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while goal:
        if  len(cards1) != 0 and cards1[0] == goal[0]:
            goal.popleft()
            cards1.popleft()
        elif len(cards2) != 0 and cards2[0] == goal[0]:
            goal.popleft()
            cards2.popleft()
        else:
            return "No"


    return "Yes"

'''
# 다른 사람 풀이

def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
'''