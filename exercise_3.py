"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class Solution:

# LC173: Insertion Sort List: 
# Sort a linked list using insertion sort
    def insertionSortList(self, head):
        dummy = ListNode(0)
        cur = head
        while cur is not None:
            pre = dummy
            # scan from the beginning of sorted part of this LinkedList, 
            # if find appropriate positon for cur, insert cur between pre and prev.next
            # otherwise keep scaning
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
        
        return dummy.next

# LC206. Reverse Linked List
    def reverseLinkedList_iter(self, head):
        if head is None or head.next is None:
            return head
        else:
            pre = None #if pre = ListNode(None) then can not pass test case
            cur = head
            while cur is not None:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
    
    def reverseLinkedList_recursive(self, head):
        # base case
        if head is None or head.next is None:
            return head
        else:
        # use itself
            new_head = self.reverseLinkedList_recursive(head.next)
            head.next.next = head
            head.next = None
            return new_head
    