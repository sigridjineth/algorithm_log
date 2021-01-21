# 이진 트리 반전 LEETCODE #26
# 반복 구조로 DFS 후위 순회 풀이
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # post-order 순으로 풀이한다. 오른쪽 노드 -> 왼쪽 노드 -> 루트
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left # post-order
        return root

    # pre-order 순으로 풀이한다. 루트 -> 왼쪽 노드 -> 오른쪽 노드
    def invertTree_pre_order(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.left, node.right
                stack.append(node.left)
                stack.append(node.right)
        return root

    def invertTree_bfs(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root