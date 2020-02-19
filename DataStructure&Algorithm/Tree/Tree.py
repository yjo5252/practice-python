# 트리구조의 자료에 특정 자료 우므 확인 코드
# 탐색방법은 DFS & BFS 알고리즘을 응용

class Node(object) : # 노드의 형식을 정의하는 부분
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # 이진트리에 데이터를 넣는 부분
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    def _insert_value(self, node, data):
        if node is None:
            node = Node (data)
        else :
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key): #이진트리에서 데이터를 찾는 부분
        return self._find_value(self.root, key)
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # 이진트리에서 데이터를 지우는 부분
    def delete(self, key) :
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    def _delete_value(self, node, key):
        if node is None:
            return node, False
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left #node.left 의 데이터를 node.right.left에 연결시킴
                if parent != node :
                    parent.left = child.right
                    parent.right = child.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else : node = None
        elif key <node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else :
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    # 데이터를 출력하는 부분
    def DFTravel (self): # 깊이 우선 탐색 중 전위순회 : 뿌리 > 왼쪽 트리 > 오른쪽 트리
        def _DFTravel (root) :
            if root is None :
                pass
            else:
                print(root.data, end = ' ')
                _DFTravel(root.left)
                _DFTravel(root.right)
        _DFTravel(self.root)

    def LFTravel (self) : # 깊이 우선 탐색 중 중위 순회 : 왼쪽 트리 > 뿌리 > 오른쪽 트리
        def _LFTravel (root) :
            if root is None:
                pass
            else:
                _LFTravel(root.left)
                print(root.data, end=' ')
                _LFTravel(root.right)
        _LFTravel(self.root)

    def LRTravel (self): # 깊이 우선 탐색 중 후위 순회 : 왼쪽 트리 > 오른쪽 트리 > 뿌리
        def _LRTravel (root) :
            if root is None :
                pass
            else:
                _LRTravel(root.left)
                _LRTravel(root.right)
                print(root.data, end=' ')
        _LRTravel(self.root)

    def layerTravel (self): # 너비 우선 탐색 : 뿌리 노드부터 깊이 순으로 방문
        def _layerTravel (root) :
            queue  = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data, end=' ')
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _layerTravel(self.root)