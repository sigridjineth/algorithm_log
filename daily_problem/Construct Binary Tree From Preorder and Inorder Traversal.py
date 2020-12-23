# LEETCODE 105
# Using pre-order result to divide and conquer in-order result
class TreeNode:

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		if inorder:
			index = inorder.index(preorder.pop(0))
			node = TreeNode(inorder[index])
			node.left = self.buildTree(preorder, inorder[0:index])
			node.right = self.buildTree(preorder, inorder[index+1:])
		return node
