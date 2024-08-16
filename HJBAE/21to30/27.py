"""
첫 번째 인수 lst를 이용해서 이진 탐색 트리를 생성하고
두 번째 인수 search_lst에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인하여
True 또는 False를 담은 리스트 result를 반환하는 함수 solution()을 작성
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)    # 트리가 비어있으면 새로운 노드 반환
    if value < root.value:    # 안비어있으면 왼쪽 or 오른쪽에 삽입
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def search_bst(root, value):    # value가 트리에 존재하는지 확인
    if root is None:    # 비어있으면 False
        return False
    if root.value == value:    # 같으면 True
        return True
    elif value < root.value:    # 작으면 왼쪽 서브트리
        return search_bst(root.left, value)
    else:    # 크면 오른쪽 서브트리
        return search_bst(root.right, value)

def solution(lst, search_lst):    # 일단 lst를 이용해서 이진 탐색 트리 생성
    if not lst:    # 비어있는 경우
        return [False] * len(search_lst)    # search_lst 를 이용해서 True 아니면 False 반환
    
    root = None
    for value in lst:
        root = insert_into_bst(root, value)

    result = []
    for value in search_lst:    # search_lst 각 값을 트리에서 검색하고 결과를 result 리스트에 추가
        result.append(search_bst(root, value))

    return result

lst1 = [5, 3, 8, 4, 2, 1, 7, 10]
search_lst1 = [1, 2, 5, 6]
# answer1 = [True, True, True, False]

lst2 = [1, 3, 5, 7, 9]
search_lst2 = [2, 4, 6, 8, 10]
# answer2 = [False, False, False, False, False]

print(solution(lst1, search_lst1))
print(solution(lst2, search_lst2))