from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if (list1.val <= list2.val):
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    
    return dummy.next

l13 = ListNode(4, None)
l12 = ListNode(2, l13)
l1 = ListNode(1, l12)

l23 = ListNode(4, None)
l22 = ListNode(3, l23)
l2 = ListNode(1, l22)


result = mergeTwoLists(l1, l2)
while (result):
    print(result.val)
    result = result.next

        