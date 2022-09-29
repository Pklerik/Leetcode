
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass     

    def list_length(self):
        "returns the number of list items"
        
        count = 0
        current_node = self.head
        
        while current_node is not None:
            count = count + 1
            
            current_node = current_node.next
            
        return count

    def extract(self, head: Optional[ListNode], nth_node:int) -> None:
        counter = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if counter == nth_node:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return

            previous_node = current_node
            current_node = current_node.next
            counter += 1
        return 


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.head = head
        count = self.list_length()
        pointer_to_extract = count - n + 1
        self.extract(head, pointer_to_extract)
        return self.head



s = Solution()
head = ListNode(val= 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val= 4, next= ListNode(val= 5, next= None)))))
n = 2
print(s.removeNthFromEnd(head,n))
        
