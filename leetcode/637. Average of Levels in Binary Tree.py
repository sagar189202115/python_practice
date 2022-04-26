def avgoflevel(root):
    q = []
    q.append(root)
    res = []
    while q:
        l = len(q)
        s = 0
        ll = l
        while l > 0:
            node = q.pop(0)
            s += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            l -= 1
        res.append(s / ll)
    return res