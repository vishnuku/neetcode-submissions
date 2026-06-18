# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        level = 0
        right_arr = []
        
        if root:
            queue.append(root)
        
        while len(queue)> 0:
            r = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                r = node.val
            right_arr.append(r)
            level += 1
        
        return right_arr