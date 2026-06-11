# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, k, cnt):
        if node is None:
            return -1

        left = self.dfs(node.left, k, cnt)

        if left != -1:
            return left
        
        cnt[0] += 1

        if cnt[0] == k:
            return node.val
        
        right = self.dfs(node.right, k, cnt)

        return right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = [0]
        return self.dfs(root, k, cnt)
        