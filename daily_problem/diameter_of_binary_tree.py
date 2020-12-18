# 이진 트리의 직경 LEETCODE #543
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if (not node):
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            # 매번 경신해줄 수밖에 없다. 물론 루트 노드일 때가 최대인 것은 누구나 안다.
            # 하지만 self.left, self.right을 매번 경신하는 것도 비슷한 복잡도이다.
            # 또한 self.left와 self.right을 변수 하나로 할당하면, 매 과정마다 바뀐다.
            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return self.longest

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.left = node_6

print(Solution().diameterOfBinaryTree(node_1))