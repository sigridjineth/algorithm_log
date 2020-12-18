# 가장 긴 동일 값의 경로 LEETCODE #687
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            # 존재하지 않는 노드의 경우 0을 리턴
            if (node is None):
                return 0
            # 리프 노드 바로 아래까지 탐색 수행
            left = dfs(node.left)
            right = dfs(node.right)
            # 현재 노드가 자식 노드와 길이가 같다면 left나 right에 1을 각각 추가한다.
            if (node.left) and (node.left.val == node.val):
                left += 1
            else:
                left = 0
            if (node.right) and (node.right.val == node.val):
                right += 1
            else:
                right = 0
            # result는 매 계산마다 갱신해준다. left + right인 이유는 왼쪽 노드를 타고 오른쪽 노드로 갈 수 있기 때문이다.
            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result