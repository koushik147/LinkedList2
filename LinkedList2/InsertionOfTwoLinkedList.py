#Time_Complexity: O(n) 
#Space_Complexity : O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # edge case
        if headA == None and headB == None:
            return None
        
        lenA = 0 # assigning lenA to 0
        lenB = 0 # assigning lenB to 0
        pa = headA # assigning pa pointer to headA
        pb = headB # assigning pb pointer to headB
        
        while pa!=None: # calculating the length of headA
            lenA+=1 # incrementing lenA
            pa = pa.next
            
        while pb!=None: # calculating the length of headB
            lenB+=1 # incrementing lenB
            pb = pb.next
            
        pa = headA # assigning pa pointer to headA
        pb = headB # assigning pb pointer to headB
        
        while lenA>lenB: # traversing thorugh the linked list headA until the equal point
            pa = pa.next
            lenA-=1
            
        while lenA<lenB: # traversing thorugh the linked list headB until the equal point
            pb = pb.next
            lenB-=1
            
        while pa!=pb: # run until pa not equl to pb
            pa = pa.next # incrementing 1 node
            pb = pb.next # incrementing 1 node
            
        return pa
