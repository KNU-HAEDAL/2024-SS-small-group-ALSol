def solution(n, m, x, y, r, c, k):
    answer = ""
    distance = abs(x-r) + abs(y-c)
    
    # 현재 위치와 도착지점 사이의 거리와 k를 비교
    # k가 더 크다면 최대한 사전이 빠른 순으로 되도록 (n,1)을 향해 가도록 함
    while distance < k:
        if x != n:
            x += 1
            answer += 'd'
        elif y != 1:
            y -= 1
            answer += 'l'
        else:
            y += 1
            answer += 'r'
        
        distance = abs(x-r) + abs(y-c)
        k -= 1
    
    # 거리와 k가 같지 않다면 도착점까지 갈 수 없다
    if distance  != k:
        return "impossible"
    
    # 사전 순으로 최대한 빠르게 되도록 함
    if r - x > 0:
        answer += 'd' * abs(x - r)
    
    if c - y < 0:
        answer += 'l' * abs(c - y)
    
    if c -y > 0:
        answer += 'r' * abs(c - y)

    if r - x < 0:
        answer += 'u' * abs(x - r)

    return answer