def hasPathSum( root, targetSum):
    if root == None:
        return False

    def dfs(root, s):

        if root == None:
            return False
        if root.left == None and root.right == None:
            return s + root.val == targetSum
        if dfs(root.left, root.val + s):
            return True
        elif dfs(root.right, root.val + s):
            return True
        return False

    if dfs(root, 0):
        return True
    else:
        return False
