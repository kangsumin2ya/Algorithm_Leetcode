# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 원하는 값이 없으면 빈 값 반환
        if not root:
            return None
        
        # 노드 값이 원하는 값과 같으면 반환
        if root.val == val:
            return root
        
        # 노드 값이 원하는 값보다 크면 왼쪽 이동
        elif root.val > val:
            return self.searchBST(root.left, val)
        # 노드 값이 원하는 값보다 작으면 오른쪽 이동
        elif root.val < val:
            return self.searchBST(root.right, val)

        