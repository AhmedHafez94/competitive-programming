# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(self, head: ListNode) -> ListNode:
    if head.next == None:
        return 
    else:
        current_node = head.next 
        head.next = current_node.next 
        current_node.next = head 
        head = current_node
        head.next.next = self.swapPairs(head.next.next)
        return head



node1 = ListNode(val = 1, next = None)
node2 = ListNode(val = 2, next = None) 
node3 = ListNode(val = 3, next = None) 
node4 = ListNode(val = 4, next = None) 
node1.next = node2
node2.next= node3
node3.next = node4
swapPairs(node1)
