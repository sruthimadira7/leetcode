"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

class Solution:
    def reverseList(self, head):
        current_node = head
        prev = None

        while current_node is not None:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next

        return prev


s = Solution()
print(s.reverseList(a))