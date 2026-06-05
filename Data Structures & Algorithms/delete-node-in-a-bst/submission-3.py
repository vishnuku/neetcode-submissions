class Solution:

    def minValue(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            successor = self.minValue(root.right)

            root.val = successor.val

            root.right = self.deleteNode(
                root.right,
                successor.val
            )

        return root