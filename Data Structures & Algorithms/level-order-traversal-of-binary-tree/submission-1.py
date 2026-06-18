# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        level = 0
        tree_arr = []

        if root:
            queue.append(root)
        
        while len(queue)>0:
            level_arr = []
            for i in range(len(queue)):
                node = queue.popleft()
                level_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            tree_arr.append(level_arr)
            level += 1
        return tree_arr


        
        
        