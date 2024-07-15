def inorder_traversal(tree, node, result):
    if node != None:
        left_child, right_child = tree[node]
        inorder_traversal(tree, left_child, result)
        result.append(node)
        inorder_traversal(tree, right_child, result)
    return result
    
def preorder_traversal(tree, node, result):
    if node != None:
        left_child, right_child = tree[node]
        result.append(node)
        preorder_traversal(tree, left_child, result)
        preorder_traversal(tree, right_child, result)
    return result

def postorder_traversal(tree, node, result):
    if node != None:
        left_child, right_chile = tree[node]
        postorder_traversal(tree, left_child, result)
        postorder_traversal(tree, right_chile, result)
        result.append(node)
    return result

def solution(nodes):
    answer = []
    result = []
    #key는 node, value는 튜플로 왼쪽자식, 오른쪽자식
    tree = { }
    for i in range(1, len(nodes)+1):
        if i*2 > len(nodes):
            tree[i] = (None, None)
        else:
           tree[i] = (i*2, i*2+1)

    answer.append(" ".join(map(str,preorder_traversal(tree, 1, result))))
    result = []
    answer.append(" ".join(map(str,inorder_traversal(tree, 1, result))))
    result = []
    answer.append(" ".join(map(str,postorder_traversal(tree, 1, result))))
    return answer

nodes = [1, 2, 3, 4, 5, 6, 7] 
print(solution(nodes))