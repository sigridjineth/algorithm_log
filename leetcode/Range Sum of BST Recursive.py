# 이진 탐색 트리(BST) 합의 범위
# LEETCODE 938 Range Sum of BST
# 반복 구조 DFS로 필요한 노드를 탐색하는 풀이

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ret = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val:
                    stack.append(node.left)
                if node.val <= R:
                    stack.append(node.right)
                if (L <= node.val <= R):
                    self.ret += node.val
        return self.ret

    def rangeSumBST_BFS_recursive(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while stack:
            node = stack.pop(0)
            if node:
                if node.val >= L:
                    stack.append(node.left)
                if node.val <= R:
                    stack.append(node.right)
                if (L <= node.val <= R):
                    self.ret += node.val
        return self.ret

node_ten = TreeNode(10)
node_five = TreeNode(5)
node_fifteen = TreeNode(15)
node_three = TreeNode(3)
node_seven = TreeNode(7)
node_eighteen = TreeNode(18)

node_ten.left = node_five
node_ten.right = node_fifteen
node_five.left = node_three
node_five.right = node_seven
node_fifteen.right = node_eighteen

print(Solution().rangeSumBST(node_ten, 7, 15))