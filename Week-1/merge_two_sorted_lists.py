# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode()  # Create a dummy node to act as the starting point of the merged list.
        tail_pointer = dummy_node  # Tail pointer keeps track of the last node in the merged list.

        while list1 and list2:  # Iterate while both lists are non-empty.
            if list1.val < list2.val:  # If list1's value is smaller, append it to the merged list.
                tail_pointer.next = list1  # Link the current node of list1 to the merged list.
                list1 = list1.next  # Move to the next node in list1.
            else:  # If list2's value is smaller or equal, append it instead.
                tail_pointer.next = list2  # Link the current node of list2 to the merged list.
                list2 = list2.next  # Move to the next node in list2.

            tail_pointer = tail_pointer.next  # Move the tail pointer to the last node in the merged list.

        # At this point, one of the lists is empty. Attach the remaining nodes of the non-empty list.
        if list1:  # If list1 still has nodes left, attach them.
            tail_pointer.next = list1  
        elif list2:  # If list2 still has nodes left, attach them.
            tail_pointer.next = list2  

        return dummy_node.next  # Return the merged list, skipping the dummy node.
