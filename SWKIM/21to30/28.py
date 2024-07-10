def solution(N, A, B):
    cnt = 0

    # A와 B의 트리노드 인덱스 설정 
    A = N + A - 1
    B = N + B - 1

    # 두 노드의 부모노드가 같다면 두 노드가 만나는 것과 같다.
    while(True):
        A = A // 2
        B = B // 2
        cnt += 1

        if A == B:
            break
    
    return cnt

print(solution(8,4,7))