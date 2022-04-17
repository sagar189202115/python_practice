from idlelib.tree import TreeNode
from typing import Optional


def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    temp = root
    sum = 0

    def gbst(node, val):
        if not node: return val

        node.val += gbst(node.right, val)
        return gbst(node.left, node.val)

    gbst(root, 0)
    return temp