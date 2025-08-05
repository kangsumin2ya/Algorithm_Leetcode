# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []

        def dfs(node, path, total):
            if not node:
                return
            # 노드 값 누적합 계산
            path.append(node.val)
            total += node.val

            # 노드 끝까지 왔을 경우
            if not node.left and not node.right:
                # 합이 같다면 이동 경로를 정답 리스트에 넣기
                if total == targetSum:
                    result.append(path[:])

            # dfs 재귀적 진행
            dfs(node.left, path, total)
            dfs(node.right, path, total)
            
            # 백트래킹
            path.pop()
        
        dfs(root, [], 0)
        return result