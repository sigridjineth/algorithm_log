# 이진 트리의 최대 깊이 LEETCODE #104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if (cur_root.left):
                    queue.append(cur_root.left)
                if (cur_root.right):
                    queue.append(cur_root.right)
        
        # BFS 반복한 횟수는 깊이와 같다.
        return depth