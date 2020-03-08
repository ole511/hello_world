# -*- coding:utf-8 -*-  
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:             #普通办法，用列表存指针
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:return
        if not pHead.next:return #只有一个结点时，无法成环
        head=pHead
        res=[]
        while head not in res:
            res.append(head)
            head=head.next
        return head
    
    
'''
链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4?f=discussion
来源：牛客网

思路：设置快慢指针，都从链表头出发，快指针每次走两步，慢指针一次走一步，假如有环，一定相遇于环中某点(结论1)。
接着让两个指针分别从相遇点和链表头出发，两者都改为每次走一步，最终相遇于环入口(结论2)。

【证明结论1】设置快慢指针fast和low，fast每次走两步，low每次走一步。
            假如有环，两者一定会相遇（因为low一旦进环，可看作fast在后面追赶low的过程，每次两者都接近一步，最后一定能追上）。     
            
【证明结论2】设：链表头到环入口长度为--a 环入口到相遇点长度为--b 相遇点到环入口长度为--c
            则：相遇时  
                快指针路程=a+(b+c)k+b ，k>=1  
                ——————————其中b+c为环的长度，k为绕环的圈数（k>=1,即最少一圈，不能是0圈，不然和慢指针走的一样长，矛盾）。     
                慢指针路程=a+b     
            快指针走的路程是慢指针的两倍，
                所以：     （a+b）*2=a+(b+c)k+b     
                化简可得：    a=(k-1)(b+c)+c  
                这个式子的意思是：  链表头到环入口的距离=相遇点到环入口的距离+（k-1）圈环长度。其中k>=1,所以k-1>=0圈。
            所以两个指针分别从链表头和相遇点出发，最后一定相遇于环入口。 
'''
class Solution:   # 用快慢双指针，节省空间
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast=pHead
        slow=pHead
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                fast=pHead
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
                return slow
        return
