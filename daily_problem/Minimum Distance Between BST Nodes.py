# 이진 탐색 트리(BST) 노드 간 최소 거리
# 리트코드 783번
import sys

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        if (root.left):
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        if (root.right):
            self.minDiffInBST(root.right)
        return self.result