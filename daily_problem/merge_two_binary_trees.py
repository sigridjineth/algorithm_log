# 두 이진 트리 병합 LEETCODE #617
# DFS를 이용한 반복 재귀 탐색
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (t1 and t2):
            node = TreeNode(t1.val + t2.val) # root -> left node -> right node
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2 # if nothing, return None