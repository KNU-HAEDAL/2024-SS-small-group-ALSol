from itertools import permutations # 순열

def solution(n, weak, dist):
    # weak 리스트의 길이 (취약 지점의 개수)
    size = len(weak)
    # 최솟값을 찾기 위해 초기값을 무한대로 설정
    answer = float('inf')
    
    # weak 리스트를 두 배로 늘려서 원형 문제를 선형으로 변환
    for i in range(size):
        weak.append(weak[i] + n)

    # 친구들이 움직일 수 있는 거리(dist)에 대한 모든 순열 계산
    for friends in permutations(dist):
        # weak의 각 취약 지점을 시작점으로 설정
        for start in range(size):
            cnt = 1
            # 첫 번째 친구가 커버할 수 있는 최대 거리 설정
            position = weak[start] + friends[cnt - 1]
            
            # 각 취약 지점을 순회하면서 친구들이 커버할 수 있는지 확인
            for index in range(start, start + size):
                if position < weak[index]:
                    # 친구를 추가로 사용해야 하는 경우
                    cnt += 1
                    if cnt > len(dist):
                        break
                    # 새 친구가 커버할 수 있는 최대 거리 설정
                    position = weak[index] + friends[cnt - 1]
            
            # 현재 순열로 가능한 최소 인원수를 answer와 비교하여 업데이트
            answer = min(answer, cnt)
    
    return answer if answer <= len(dist) else -1


weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(12, weak, dist))
