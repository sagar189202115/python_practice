from idlelib.tree import TreeNode
from typing import Optional


def sumNumbers(self, root: Optional[TreeNode]) -> int:
    res = []

    def dfs(root, st):
        if root.left == None and root.right == None:
            st += str(root.val)
            res.append(int(st))
            return
        st += str(root.val)
        if root.left != None:
            dfs(root.left, st)
        if root.right != None:
            dfs(root.right, st)

    dfs(root, '')
    return sum(res)