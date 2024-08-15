"""
이진 트리를 표현한 리스트 nodes를 인자로 받음
해당 이진 트리에 대하여 전위 순회, 중위 순회, 후위 순회 결과를 반환하는 solution() 함수를 구하시오
"""
def preorder(nodes, idx):    # 전위 순회
    if idx >= len(nodes):
        return []
    return [nodes[idx]] + preorder(nodes, 2 * idx + 1) + preorder(nodes, 2 * idx + 2)

def inorder(nodes, idx):    # 중위 순회
    if idx >= len(nodes):
        return []
    return inorder(nodes, 2 * idx + 1) + [nodes[idx]] + inorder(nodes, 2 * idx + 2)  

def postorder(nodes, idx):
    if idx >= len(nodes):
        return []
    return postorder(nodes, 2 * idx + 1) + postorder(nodes, 2 * idx + 2) + [nodes[idx]]

def solution(nodes):
    pre_order = preorder(nodes, 0)
    in_order = inorder(nodes, 0)
    post_order = postorder(nodes, 0)
    return [" ".join(map(str, pre_order)), " ".join(map(str, in_order)), " ".join(map(str, post_order))]

nodes = [1, 2, 3, 4, 5, 6, 7]
# return = ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]

result = solution(nodes)
print(result)