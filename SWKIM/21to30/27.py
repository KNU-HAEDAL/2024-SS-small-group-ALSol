# 노드 클래스
# 값을 저장하는 data / 현재 노드의 data보다 작다면 left, 크다면 right의 노드로 이동한다.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진트리 클래스
# root를 기준으로 값이 작다면 왼쪽, 크다면 오른쪽에 저장된다.
# 값을 저장, 탐색할 수 있는 기능이 구현되어 있다.
class BinaryTree:
    # 트리 초기화
    def __init__(self):
        self.root = None

    # 이진 트리에 값 삽입
    def insert(self, data):
        # root 노드의 존재 여부에 따라 방식이 다르다.
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root

            # 값이 현재 노드보다 작다면 왼쪽노드로 이동, 크다면 오른쪽으로 이동
            # 만일 현재 노드가 존재하지 않는다면 해당 자리에 노드 생성 후 값 삽입
            while True:
                if data < cur.data:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break                    
                elif data > cur.data:
                    if cur.right != None:
                        cur =cur.right
                    else:
                        cur.right = Node(data)   
                        break
    # 찾는 값이 트리에 존재하는지 탐색
    # 존재한다면 True, 아니라면 False를 반환
    def search(self, target):
        cur = self.root
        
        # 찾는 값이 현재 노드보다 작다면 왼쪽노드, 크다면 오른쪽 노드로 이동
        # 현재 노드의 값이 찾는 값과 동일하면 True, 현재 노드가 존재하지 않는다면 찾는 값이 존재하지 않기에 False 반환 
        while True:
            if cur == None:
                return False

            if target < cur.data:
                cur = cur.left
            elif target > cur.data:
                cur = cur.right
            else:
                return True



def solution(lst, search_lst):
    answer = []
    tree = BinaryTree() # 이진트리 생성

    # lst에 저장된 값 삽입
    for data in lst:
        tree.insert(data)

    # search_lst에 저장된 값이 이진트리에 존재하는지 탐색
    for target in search_lst:
        answer.append(tree.search(target))
    
    return answer

print(solution([5,3,8,4,2,1,7,10], [1,2,5,6]))
print(solution([1,3,5,7,9], [2,4,6,8,10]))
