def pre_order(nodes, index, result):
    if index >= len(nodes):
        return
    result.append(str(nodes[index]))  # 현재 노드 방문
    pre_order(nodes, 2 * index + 1, result)  # 왼쪽 서브트리
    pre_order(nodes, 2 * index + 2, result)  # 오른쪽 서브트리

def in_order(nodes, index, result):
    if index >= len(nodes):
        return
    in_order(nodes, 2 * index + 1, result)  # 왼쪽 서브트리
    result.append(str(nodes[index]))  # 현재 노드 방문
    in_order(nodes, 2 * index + 2, result)  # 오른쪽 서브트리

def post_order(nodes, index, result):
    if index >= len(nodes):
        return
    post_order(nodes, 2 * index + 1, result)  # 왼쪽 서브트리
    post_order(nodes, 2 * index + 2, result)  # 오른쪽 서브트리
    result.append(str(nodes[index]))  # 현재 노드 방문

def solution(nodes):
    pre_result = []
    in_result = []
    post_result = []
    
    pre_order(nodes, 0, pre_result)
    in_order(nodes, 0, in_result)
    post_order(nodes, 0, post_result)
    
    return [''.join(pre_result), ''.join(in_result), ''.join(post_result)]

print(solution([1, 2, 3, 4, 5, 6, 7])) 
