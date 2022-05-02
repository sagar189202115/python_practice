from idlelib.tree import TreeNode
from typing import Optional, List


def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []

    def dfs(root, st):
        if root.left == None and root.right == None:
            st += str(root.val)
            res.append(st)
            return
        st += str(root.val)
        st += '->'
        if root.left != None:
            dfs(root.left, st)
        if root.right != None:
            dfs(root.right, st)

    dfs(root, '')
    return res