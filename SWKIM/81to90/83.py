from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()   # 오름차순으로 정렬
    people = deque(people)

    # 무거운 사람과 가벼운 사람을 묶어 가는 것이 가장 빠름
    while people:
        cur = people.pop() # 무거운 사람 보트에 태움

        # 가벼운 사람도 탈 수 있는 경우
        if people and cur + people[0] <= limit:
            cur += people[0]
            people.popleft()
        
        answer += 1

    return answer

people = [40, 40, 40, 40]
limit = 160
print(solution(people, limit))