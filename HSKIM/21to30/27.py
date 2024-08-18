class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, key):
        self.key = key  # 키
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None
    
    def insert(self, key) -> bool:
        """트리에 노드를 삽입하는 함수"""
        def insert_node(node, key) -> bool:
            if key == node.key:  # 이미 같은 키가 존재하면 False 반환
                return False
            elif key < node.key:  # 삽입하려는 키가 현재 노드의 키보다 작을 때
                if node.left is None:  # 왼쪽 자식이 없으면
                    node.left = Node(key)  # 새로운 노드를 생성하여 삽입
                    return True
                else:
                    return insert_node(node.left, key)  # 왼쪽 자식이 있으면 재귀적으로 삽입
            else:  # 삽입하려는 키가 현재 노드의 키보다 클 때
                if node.right is None:  # 오른쪽 자식이 없으면
                    node.right = Node(key)  # 새로운 노드를 생성하여 삽입
                    return True
                else:
                    return insert_node(node.right, key)  # 오른쪽 자식이 있으면 재귀적으로 삽입
        
        if self.root is None:  # 루트가 없으면
            self.root = Node(key)  # 새로운 노드를 루트로 설정
            return True
        else:
            return insert_node(self.root, key)  # 루트가 있으면 삽입 시작
    
    def search(self, key) -> bool:
        """트리에서 특정 키를 찾는 함수"""
        def search_node(node, key) -> bool:
            if node is None:  # 노드가 없으면 False 반환
                return False
            if key == node.key:  # 찾는 키와 현재 노드의 키가 같으면 True 반환
                return True
            elif key < node.key:  # 찾는 키가 현재 노드의 키보다 작으면 왼쪽으로 이동
                return search_node(node.left, key)
            else:  # 찾는 키가 현재 노드의 키보다 크면 오른쪽으로 이동
                return search_node(node.right, key)
        
        return search_node(self.root, key)  # 검색 시작


def solution(lst, search_lst):
    tree = BinarySearchTree()  # 이진 탐색 트리 생성
    
    # lst에 있는 값들을 트리에 삽입
    for key in lst:
        tree.insert(key)
    
    # search_lst에 있는 값들을 트리에서 찾기
    result = []
    for key in search_lst:
        result.append(tree.search(key))  # 찾은 결과를 리스트에 저장
    
    return result


# lst = [1, 3, 5, 7, 9]
# search_lst = [2, 4, 6, 8, 10]
# print(solution(lst, search_lst))  