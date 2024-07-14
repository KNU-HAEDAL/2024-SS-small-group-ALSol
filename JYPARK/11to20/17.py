'''무한 루프를 while True로 돌렸었는데 런타임 에러남
무한루프에서 True로 하면 가능한지 궁금
goal이 빈 덱일 때 goal[0]에서 인덱스 오류가 발생하는지 or goal이 빈 덱이라면 cards1,2도 비었을 것이므로 if cards1, elif cards2만 검사하고도 else로 가는지'''
from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    while True:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        else:
            break
    
    if goal:
        answer = 'No'
    else:
        answer = 'Yes'
    return answer

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]	
#solution(cards1, cards2, goal)
print(solution(cards1, cards2, goal))