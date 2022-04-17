class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.res = TreeNode(0)
        self.re = self.res

        def bst(r):
            if r:
                bst(r.left)
                self.res.right = TreeNode(r.val)
                self.res = self.res.right
                print(self.res)

                bst(r.right)

        bst(root)
        return self.re.right

