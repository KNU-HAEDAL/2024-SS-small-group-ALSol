#노드 생성하는 클래스
class Node:
    def __init__(self, key):
        if key != None:
            self.val = key
            self.left = None
            self.right = None
#이진탐색트리
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        #루트 노드가 없는 경우 노드를 만들고 시작
        if self.root == None:
            self.root = Node(key)
        #루트 노드가 있는 경우 
        else:
            curr = self.root
            while True:
                if curr.val > key:
                    if curr.left == None:
                        curr.left = Node(key)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = Node(key)
                        break
                    else:
                        curr = curr.right

    def search(self, key):
        curr = self.root
        while True:
            if curr.val == key:
                return True
            elif curr.val > key:
                #트리에 찾는 값이 없는 경우
                if curr.left == None:
                    return False
                else:
                    curr = curr.left
            else:
                #트리에 찾는 값이 없는 경우
                if curr.right == None:
                    return False
                else:
                    curr = curr.right

def solution(lst, search_lst):
    answer = []
    #BST 객체 생성
    bst = BST()
    for key in lst:
        bst.insert(key)
    for key in search_lst:
        if bst.search(key) == False:
            answer.append(False)
        else:
            answer.append(True)
    return answer

lst = [1, 3, 5, 7, 9]
search_lst = [2, 4, 6, 8,10] 
print(solution(lst, search_lst))