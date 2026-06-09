# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes: List[int] = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.nodes
        self.inorderTraversal(root.left)
        self.nodes.append(root.val)
        self.inorderTraversal(root.right)
        return self.nodes