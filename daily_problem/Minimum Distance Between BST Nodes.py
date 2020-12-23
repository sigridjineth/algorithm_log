# LEETCODE 783
# Iterating for In-order traversal
class TreeNode:

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:

	def minDiffInBST_iteration(self, root: TreeNode) -> int:
		prev = -sys.maxsize
		result = sys.maxsize
		stack = []
		node = root

		while stack or node:
			while node:
				stack.append(node)
				node = node.left
			node = stack.pop()
			result = min(result, node.val - prev)
			prev = node.val
			node = node.right
		return result

	class Solution_Recursive:
		prev = -sys.maxsize
		result = sys.maxsize

		def minDiffInBST_Recursive(root) -> int:
			if root.left:
				self.minDiffInBST_Recursive(root.left)
			self.result = min(self.result, node.val - self.prev)
			if root.right:
				self.minDiffInBST_Recursive(root.right)
			return self.result

