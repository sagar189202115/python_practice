from idlelib.tree import TreeNode
from typing import Optional


def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    if root == None:
        return None
    elif low <= root.val <= high:
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root

    elif root.val > high:
        return self.trimBST(root.left, low, high)
    elif root.val < low:
        return self.trimBST(root.right, low, high)
    return root