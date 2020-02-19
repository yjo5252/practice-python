# Tree.py 에서 정의한 이진 탐색 트리에
# 데이터를 삽입하여 트리구조를 완성하고
# 트리안의 데이터 존재 유무 확인과
# 탐색알고리즘을 따라 트리구조의 데이터를 출력한다.

# 데이터 선언

import Tree as T

data = [20, 6, 8, 12, 78, 32, 65, 32, 7, 9]
tree = T.BinarySearchTree()

# 트리구조의 완성
for x in data :
    tree.insert(x)

print(tree.find(9))
print(tree.find(3))
print(tree.delete(78))
print(tree.delete(6))
print(tree.delete(11))

#트리구조의 데이터 출력
print("\n@ @ @ DFS @ @ @ ")
tree.DFTravel() # 20 8 7 12 9 32 32 65
print("\n=======LFS===========")
tree.LFTravel() #7 8 9 12 20 32 32 65
print("\n=======LRS============")
tree.LRTravel() # 7 9 12 8 32 65 32 20
print("\n=======layerS=========")
tree.layerTravel() # 20 8 32 7 12 32 65
print("\n@ @ @ @ @ @ @ @ @ @ @ ")


