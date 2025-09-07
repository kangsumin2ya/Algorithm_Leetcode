# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 노드 없으면 깊이 0
        if root is None:
            return 0

        # 왼쪽과 오른쪽 중 깊이가 더 큰 값에 +1해 반환 -> DFS를 재귀함수로 구현
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
