# 이진 탐색 트리(BST) 합의 범위
# LEETCODE 938 Range Sum of BST
# DFS를 활용하여 브루트 포스 이용 모든 노드를 탐색하는 풀이
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ret = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # traverse given node
        self.dfs(root, L, R)
        return self.ret
    
    def dfs(self, node: TreeNode, L: int, R: int) -> int:
        if not node:
            return
        if (L <= node.val <= R):
            self.ret += node.val
            self.dfs(node.left, L, R)
            self.dfs(node.right, L, R)
        elif (node.val >= R):
            self.dfs(node.left, L, R)
        else: # (node.val <= L)
            self.dfs(node.right, L, R)
