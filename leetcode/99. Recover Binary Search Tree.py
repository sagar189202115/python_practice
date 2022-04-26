in_order = []


def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    in_order.append(node)
    inOrder(node.right)


inOrder(root)

sorted_order = sorted(in_order, key=lambda x: x.val)
for i in range(len(in_order)):
    if in_order[i] != sorted_order[i]:
        in_order[i].val, sorted_order[i].val = sorted_order[i].val, in_order[i].val
