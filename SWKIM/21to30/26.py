# 전위 순회
def preorder(tree, idx):
    if(idx < len(tree)):
        search = str(tree[idx]) + " "
        search += preorder(tree, 2 * idx)
        search += preorder(tree, 2 * idx + 1)
        return search
    
    return ""

# 중위 순회
def inorder(tree, idx):
    if(idx < len(tree)):
        search = inorder(tree, 2 * idx)
        search += str(tree[idx]) + " "
        search += inorder(tree, 2 * idx + 1)
        return search
    
    return ""

# 후위 순회
def postorder(tree, idx):
    if(idx < len(tree)):
        search = inorder(tree, 2 * idx)
        search += inorder(tree, 2 * idx + 1)
        search += str(tree[idx]) + " "
        return search
    
    return ""


def solution(nodes):
    answer = []
    tree = [0 for _ in range(len(nodes)+1)]

    # idx가 1일 때 root node인 tree를 만들기 위함
    for i in range(len(nodes)):
        tree[i+1] = nodes[i]

    # 순회한 결과에 마지막 공백을 제거
    answer.append(preorder(tree, 1)[:-1])
    answer.append(inorder(tree, 1)[:-1])
    answer.append(postorder(tree, 1)[:-1])

    return answer

print(solution([1,2,3,4,5,6,7]))
