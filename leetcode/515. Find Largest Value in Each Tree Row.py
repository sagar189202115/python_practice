import math


def maxinlevelbt(root):
    if root == None:
        return []
    q = []
    q.append(root)
    res = []
    while q:
        l = len(q)
        s = -math.inf
        ll = l
        while l > 0:
            node = q.pop(0)
            if node != None:
                s = max(s, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            l -= 1
        res.append(s)
    return res