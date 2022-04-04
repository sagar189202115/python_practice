from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #Iterative
    p1 = head
    p2 = head
    while k > 1:
        p1 = p1.next
        print(p1.val)
        k -= 1
    temp = p1
    p1 = p1.next
    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    print(temp.val, p2.val)
    t = p2.val
    p2.val = temp.val
    temp.val = t
    return head

    #recursive
    # temp = head
    # p1 = head
    # p2 = head
    #
    # def swap(temp, p1, p2, idx):
    #     if temp == None:
    #         t = p1.val
    #         p1.val = p2.val
    #         p2.val = t
    #         return
    #     if idx == k:
    #         swap(temp.next, p1, p2, idx + 1)
    #     elif idx > k:
    #         swap(temp.next, p1, p2.next, idx + 1)
    #
    #     else:
    #         swap(temp.next, p1.next, p2, idx + 1)
    #
    # swap(temp, p1, p2, 1)
    # return head
