"""
원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용
한 번 사용한 카드는 다시 사용 X
카드 사용하지 않고 다음 카드로 못넘어감
기존에 주어진 카드 뭉치 단어 순서 못바꿈
"""

from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    for i in range(len(goal)):
        if cards1 and (cards1[0] == goal[0]):   #cards1의 원소와 먼저 비교
            cards1.popleft()
            goal.popleft()
        elif cards2 and (cards2[0] == goal[0]):    #그 다음 cards2의 원소와 비교
            cards2.popleft()
            goal.popleft()
        else:
            break
    return "Yes" if not goal else "No"  #이 부분 체크
 # 첫 실행때 밑에 부분 복붙해오느라 쉼표 그대로 들어왔더니 리스트가 아니라 튜플이 되어서 오류가 떠버림
 # cards1, cards2, goal과 같이 리스트 정의할 때 쉼표 들어가서 튜플이 되어버리는 것 주의.. 근데 왜인지 알아봐야 함ㅎ
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))

cards11 = ["i", "water", "drink"]
cards22 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards11, cards22, goal))
#입출력 예
# cards1 = ["i", "drink", "water"], cards2 = ["want", "to"], goal = ["i", "want", "to", "drink", "water"], result = "Yes"
# cards1 = ["i", "water", "drink"], cards2 = ["want", "to"], goal = ["i", "want", "to", "drink", "water"], result = "No"