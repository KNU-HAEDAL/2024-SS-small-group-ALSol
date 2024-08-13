def solution(computers, n):
    answer = 0
    visited = [0 for i in range(n)]
    stack = []

    for node in range(n):
        if visited[node] == 0:              #방문하지 않은 노드라면
            visited[node] = 1
            stack.append(node)
            answer += 1

        while stack:                        #해당 노드에 연결된 모든 노드를 방문할 것이다
            current_node = stack.pop()

            for i in range(n):
                if computers[current_node][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
                    
    return answer

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
print(solution(computers, n))