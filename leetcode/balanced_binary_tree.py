# 균형 이진 트리 LEETCODE #110
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right) # traverse into the leaf nodes
            if (left == -1 or right == -1 or abs(left-right) > 1):
                return -1
            return max(left,right)+1
        return check(root) != -1