import sys
# 재귀 한도가 기본 1000에서 10000으로 변경
# 제한사항에서 길이가 1~10000이라서 확장해줘야함
sys.setrecursionlimit(10**5)   

# 노드 클래스
class Node:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.left = None
        self.right = None

# 트리 클래스
class BinaryTree:
    # 트리 초기화
    def __init__(self):
        self.root = None

    # 이진 트리에 값 삽입
    def insert(self, data, x, y):
        # root 노드의 존재 여부에 따라 방식이 다르다.
        if self.root == None:
            self.root = Node(data, x, y)
        else:
            cur = self.root

            # x값이 작으면 왼쪽노드, 아니면 오른쪽 노드로 이동
            while True:
                if x < cur.x:
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = Node(data, x, y)
                        break                    
                elif x > cur.x:
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = Node(data, x, y)   
                        break

def preorder(root, arr):
    if root is not None:
        arr.append(root.data) 
        preorder(root.left, arr)
        preorder(root.right, arr)
    return

def postorder(root, arr):
    if root is not None:
        postorder(root.left, arr)
        postorder(root.right, arr)
        arr.append(root.data)
    return
        
def solution(nodeinfo):
    answer = [[],[]]
    arr = []
   
    tree = BinaryTree()

    # idx, x, y값 넣기
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        arr.append([i+1, x, y])

    # y 값 기준으로 내림차순 정렬
    key = sorted(arr, key= lambda x: x[2], reverse=True)

    
    for idx, x, y in key:
        tree.insert(idx, x, y)

    preorder(tree.root, answer[0])
    postorder(tree.root, answer[1])

    return answer

    
    
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))