class Solution:
    def minValue(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_node = root
        while curr_node and curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.minValue(root.right)
                root.val = minVal.val
                root.right = self.deleteNode(root.right, minVal.val)
        return root
