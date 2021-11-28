from collections.abc import Iterable
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        if self == None: return ''
        curr = self
        result = ''
        while curr != None:
            result = "{} --> ".format(result + str(curr.val))
            curr = curr.next
        
        result = result + "None"
        return result
    
    def reverse(self, head):
        # Handle edge cases
        # If the node is Null or does not have next node
        if head == None or head.next == None: return head

        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def removeNthFromEnd(self, head, index):
        # Handle edge cases
        if head == None: return head

        leader = trailer = head
        counter = 0
        while counter < index:
            leader = leader.next
            counter += 1
        
        while leader != None:
            leader = leader.next
            trailer = trailer.next
        
        if head == trailer: head = head.next
        else: trailer.next = trailer.next.next
            
        return head

def build_singlylist(source: iter) -> ListNode:
    if source is None: return None
    if not isinstance(source, Iterable): return None
    length = len(source)
    if length == 0: return None

    node: ListNode = None

    for index in range(-1, -length-1, -1):
        node = ListNode(source[index], node)
    
    return node
